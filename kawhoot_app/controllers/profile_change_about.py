# This controller handles edit profile and about routes

from kawhoot_app import app
from kawhoot_app.models.user_model import User

from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/edit_profile')
def edit_profile(): 
    if User.validate_session(session):
        return render_template('/edit_profile.html')
    return redirect('/')

@app.route('/edit_profile/username', methods=['post'])
def update_username(): 
    if User.validate_session(session):
        data = {
            'username': request.form['username'], 
            'user_id': session['logged_in_user_id']
        }
        if User.validate_new_username(data): 
            User.update_username(data)
            return redirect('/edit_profile')
        return redirect('/edit_profile')
    return redirect('/')

@app.route('/edit_profile/password', methods=['post'])
def update_password():
    if User.validate_session(session):
        data = {
            'user_id': session['logged_in_user_id'], 
            'current_password': request.form['current_password'], 
            'new_password': request.form['new_password'], 
            'confirm': request.form['confirm']
        }
        current_user = User.get_user_by_id(data)
        plain_password = data['current_password']
        hashed_password = current_user.password
        
        if not bcrypt.check_password_hash(hashed_password, plain_password):
            flash("Password is incorrect", "current_password")
            return redirect('/edit_profile')
        elif not User.validate_new_password(data): 
            return redirect('/edit_profile')
        encrypted_password = bcrypt.generate_password_hash(data['new_password'])
        User.update_password({'new_password': encrypted_password, 'user_id': data['user_id']})
        return redirect('/edit_profile')
    return redirect('/')

@app.route('/about')
def about(): 
    return render_template('about.html')

@app.route('/about/reflection')
def about_reflection(): 
    return render_template('about_reflection.html')