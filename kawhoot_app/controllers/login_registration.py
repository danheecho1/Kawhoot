# This controller handles login, logout, and registration routes

from kawhoot_app import app
from kawhoot_app.models.user_model import User
from kawhoot_app.models.userSummary_model import UserSummary
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def main(): 
    return redirect('/login')

@app.route('/login')
def login(): 
    return render_template('login.html')

@app.route('/login', methods=['post'])
def login_post(): 
    existing_user = User.get_user_by_username({'username': request.form['username']})
    if not existing_user: 
        flash("We do not recognize the username", 'invalid_username')
        return redirect('/')
    else: 
        plain_password = request.form['password']
        hashed_password = existing_user.password
        if not bcrypt.check_password_hash(hashed_password, plain_password):
            flash("Password is incorrect", 'wrong_password')
            return redirect('/')
        else: 
            session['logged_in_user_id'] = existing_user.id
            return redirect('/dashboard')

@app.route('/logout')
def logout(): 
    session.clear()
    return redirect('/')

@app.route('/register')
def register(): 
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register_post(): 
    if not User.validate_registration(request.form): 
        return redirect('/register')
    encrypted_password = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'username': request.form['username'],
        'password': encrypted_password, 
        'confirm': request.form['confirm']
    }
    User.register_user(data)
    logged_in_user = User.get_user_by_username({'username': request.form['username']})
    session['logged_in_user_id'] = logged_in_user.id
    UserSummary.create_user_summary({'user_id': session['logged_in_user_id']})
    return redirect('/dashboard')