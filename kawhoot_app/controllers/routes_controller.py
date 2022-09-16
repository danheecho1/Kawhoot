from kawhoot_app import app
from kawhoot_app.models.user_model import User
from kawhoot_app.models.quiz_model import Quiz

from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def main(): 
    return redirect('/login')

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
    return redirect('/dashboard')

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


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/my_quizzes')
def my_quizzes(): 
    return render_template('myQuizzes.html')

@app.route('/new_quiz')
def new_quiz(): 
    return render_template('create_quiz_title.html')

@app.route('/new_quiz/title', methods=['POST'])
def new_quiz_title_post(): 
    data = {
        'title': request.form['title'], 
        'description': request.form['description'], 
        'user_id': session['logged_in_user_id']
    }
    Quiz.create_blank_quiz(data)
    return redirect('/new_quiz/question')

@app.route('/new_quiz/question')
def new_quiz_question(): 
    return render_template('create_quiz__question.html')

@app.route('/edit_profile')
def search(): 
    return render_template('/edit_profile.html')