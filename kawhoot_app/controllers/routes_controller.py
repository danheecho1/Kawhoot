from kawhoot_app import app
from kawhoot_app.models.user_model import User
from kawhoot_app.models.quiz_model import Quiz
from kawhoot_app.models.question_model import Question
from kawhoot_app.models.choice_model import Choice

import math
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
    data = {
        'user_id': session['logged_in_user_id']
    }
    user = User.get_user_by_id(data)
    return render_template('dashboard.html', user = user)

@app.route('/my_quizzes', defaults={'page': 1})
@app.route('/my_quizzes/<int:page>')
def my_quizzes(page): 
    limit = 10
    offset = page * limit - limit
    data = {
        'user_id': session['logged_in_user_id'],
        'limit': limit, 
        'offset': offset
    }
    my_quizzes = Quiz.get_paginated_quizzes(data)
    number_of_quizzes = Quiz.get_quiz_count(data)
    total_pages = math.ceil(number_of_quizzes / limit)
    next = page + 1
    prev = page - 1
    user_id = session['logged_in_user_id']
    return render_template('myQuizzes.html', my_quizzes = my_quizzes, pages = total_pages, next = next, prev = prev, user_id = user_id)

@app.route('/quiz/<int:user_id>/<int:quiz_id>')
def select_quiz(user_id, quiz_id): 
    data = {
        'quiz_id': quiz_id
    }
    quiz = Quiz.select_quiz(data)
    quiz_owner_id = user_id
    logged_in_user_id = session['logged_in_user_id']
    return render_template('select_my_quiz.html', quiz = quiz, quiz_owner_id = quiz_owner_id, logged_in_user_id = logged_in_user_id)

@app.route('/quiz/<int:user_id>/<int:quiz_id>/delete', methods = ['POST'])
def delete_quiz(user_id, quiz_id): 
    data = {
        'user_id': user_id,
        'quiz_id': quiz_id
    }
    Quiz.delete_quiz(data)
    return redirect('/my_quizzes')

@app.route('/quiz/<int:user_id>/<int:quiz_id>/edit')
def edit_quiz(user_id, quiz_id): 
    data = {
        'user_id': user_id,
        'quiz_id': quiz_id
    }
    quiz = Quiz.grab_quiz_to_edit(data)
    return render_template('edit_quiz.html', quiz = quiz, user_id = user_id, quiz_id = quiz_id)

@app.route('/quiz/<int:user_id>/<int:quiz_id>/edit', methods=['POST'])
def edit_quiz_post(user_id, quiz_id): 
    data_for_updating_quiz = {
        'title': request.form['title'],
        'description': request.form['description'], 
        'quiz_id': quiz_id, 
    }
    Quiz.update_quiz(data_for_updating_quiz)
    question_ids = [a['id'] for a in Question.get_most_recent_question_ids(data_for_updating_quiz)]
    data_for_updating_prompts = {
        'quiz_id': quiz_id, 
        'question1_id': question_ids[9],
        'question2_id': question_ids[8],
        'question3_id': question_ids[7],
        'question4_id': question_ids[6],
        'question5_id': question_ids[5],
        'question6_id': question_ids[4],
        'question7_id': question_ids[3],
        'question8_id': question_ids[2],
        'question9_id': question_ids[1],
        'question10_id': question_ids[0],
        'prompt1': request.form['prompt1'], 
        'prompt2': request.form['prompt2'], 
        'prompt3': request.form['prompt3'], 
        'prompt4': request.form['prompt4'], 
        'prompt5': request.form['prompt5'], 
        'prompt6': request.form['prompt6'], 
        'prompt7': request.form['prompt7'], 
        'prompt8': request.form['prompt8'], 
        'prompt9': request.form['prompt9'], 
        'prompt10': request.form['prompt10']
    }
    Question.update_questions(data_for_updating_prompts)
    data_for_answers = {
        'quiz_id': quiz_id,
        'question1_id': question_ids[9],
        'question2_id': question_ids[8],
        'question3_id': question_ids[7],
        'question4_id': question_ids[6],
        'question5_id': question_ids[5],
        'question6_id': question_ids[4],
        'question7_id': question_ids[3],
        'question8_id': question_ids[2],
        'question9_id': question_ids[1],
        'question10_id': question_ids[0],
        '1answer': request.form['1answer'], 
        '2answer': request.form['2answer'], 
        '3answer': request.form['3answer'], 
        '4answer': request.form['4answer'], 
        '5answer': request.form['5answer'], 
        '6answer': request.form['6answer'], 
        '7answer': request.form['7answer'], 
        '8answer': request.form['8answer'], 
        '9answer': request.form['9answer'], 
        '10answer': request.form['10answer'], 
        '1a': request.form['1a'], 
        '2a': request.form['2a'], 
        '3a': request.form['3a'], 
        '4a': request.form['4a'], 
        '5a': request.form['5a'], 
        '6a': request.form['6a'], 
        '7a': request.form['7a'], 
        '8a': request.form['8a'], 
        '9a': request.form['9a'], 
        '10a': request.form['10a'], 
        '1b': request.form['1b'], 
        '2b': request.form['2b'], 
        '3b': request.form['3b'], 
        '4b': request.form['4b'], 
        '5b': request.form['5b'], 
        '6b': request.form['6b'], 
        '7b': request.form['7b'], 
        '8b': request.form['8b'], 
        '9b': request.form['9b'], 
        '10b': request.form['10b'], 
        '1c': request.form['1c'], 
        '2c': request.form['2c'], 
        '3c': request.form['3c'], 
        '4c': request.form['4c'], 
        '5c': request.form['5c'], 
        '6c': request.form['6c'], 
        '7c': request.form['7c'], 
        '8c': request.form['8c'], 
        '9c': request.form['9c'], 
        '10c': request.form['10c'], 
        '1d': request.form['1d'], 
        '2d': request.form['2d'], 
        '3d': request.form['3d'], 
        '4d': request.form['4d'], 
        '5d': request.form['5d'], 
        '6d': request.form['6d'], 
        '7d': request.form['7d'], 
        '8d': request.form['8d'], 
        '9d': request.form['9d'], 
        '10d': request.form['10d'], 
        '1e': request.form['1e'], 
        '2e': request.form['2e'], 
        '3e': request.form['3e'], 
        '4e': request.form['4e'], 
        '5e': request.form['5e'], 
        '6e': request.form['6e'], 
        '7e': request.form['7e'], 
        '8e': request.form['8e'], 
        '9e': request.form['9e'], 
        '10e': request.form['10e']
    }
    Choice.update_choices(data_for_answers)
    return redirect('/my_quizzes')

@app.route('/new_quiz')
def new_quiz(): 
    return render_template('create_quiz.html')

@app.route('/new_quiz', methods=['POST'])
def new_quiz_post(): 
    data_for_title_description = {
        'user_id': session['logged_in_user_id'], 
        'title': request.form['title'], 
        'description': request.form['description'], 
    }
    Quiz.create_blank_quiz(data_for_title_description)
    quiz_id = Quiz.get_most_recent_quiz_id(data_for_title_description).id
    data_for_questions = {
        'quiz_id': quiz_id,
        'prompt1': request.form['prompt1'], 
        'prompt2': request.form['prompt2'], 
        'prompt3': request.form['prompt3'], 
        'prompt4': request.form['prompt4'], 
        'prompt5': request.form['prompt5'], 
        'prompt6': request.form['prompt6'], 
        'prompt7': request.form['prompt7'], 
        'prompt8': request.form['prompt8'], 
        'prompt9': request.form['prompt9'], 
        'prompt10': request.form['prompt10'], 
    }
    Question.create_questions(data_for_questions)
    question_ids = [a['id'] for a in Question.get_most_recent_question_ids(data_for_questions)]
    data_for_answers = {
        'quiz_id': quiz_id,
        'question1_id': question_ids[9],
        'question2_id': question_ids[8],
        'question3_id': question_ids[7],
        'question4_id': question_ids[6],
        'question5_id': question_ids[5],
        'question6_id': question_ids[4],
        'question7_id': question_ids[3],
        'question8_id': question_ids[2],
        'question9_id': question_ids[1],
        'question10_id': question_ids[0],
        '1answer': request.form['1answer'], 
        '2answer': request.form['2answer'], 
        '3answer': request.form['3answer'], 
        '4answer': request.form['4answer'], 
        '5answer': request.form['5answer'], 
        '6answer': request.form['6answer'], 
        '7answer': request.form['7answer'], 
        '8answer': request.form['8answer'], 
        '9answer': request.form['9answer'], 
        '10answer': request.form['10answer'], 
        '1a': request.form['1a'], 
        '2a': request.form['2a'], 
        '3a': request.form['3a'], 
        '4a': request.form['4a'], 
        '5a': request.form['5a'], 
        '6a': request.form['6a'], 
        '7a': request.form['7a'], 
        '8a': request.form['8a'], 
        '9a': request.form['9a'], 
        '10a': request.form['10a'], 
        '1b': request.form['1b'], 
        '2b': request.form['2b'], 
        '3b': request.form['3b'], 
        '4b': request.form['4b'], 
        '5b': request.form['5b'], 
        '6b': request.form['6b'], 
        '7b': request.form['7b'], 
        '8b': request.form['8b'], 
        '9b': request.form['9b'], 
        '10b': request.form['10b'], 
        '1c': request.form['1c'], 
        '2c': request.form['2c'], 
        '3c': request.form['3c'], 
        '4c': request.form['4c'], 
        '5c': request.form['5c'], 
        '6c': request.form['6c'], 
        '7c': request.form['7c'], 
        '8c': request.form['8c'], 
        '9c': request.form['9c'], 
        '10c': request.form['10c'], 
        '1d': request.form['1d'], 
        '2d': request.form['2d'], 
        '3d': request.form['3d'], 
        '4d': request.form['4d'], 
        '5d': request.form['5d'], 
        '6d': request.form['6d'], 
        '7d': request.form['7d'], 
        '8d': request.form['8d'], 
        '9d': request.form['9d'], 
        '10d': request.form['10d'], 
        '1e': request.form['1e'], 
        '2e': request.form['2e'], 
        '3e': request.form['3e'], 
        '4e': request.form['4e'], 
        '5e': request.form['5e'], 
        '6e': request.form['6e'], 
        '7e': request.form['7e'], 
        '8e': request.form['8e'], 
        '9e': request.form['9e'], 
        '10e': request.form['10e']
    }
    Choice.create_choices(data_for_answers)
    return redirect('/my_quizzes')

@app.route('/search')
def search(): 
    return render_template('/search.html')

@app.route('/search', methods=['post'])
def search_post(): 
    search_type = request.form['search_type']
    search_keyword = request.form['search_keyword']
    return redirect(f'/search/{search_type}/{search_keyword}')

@app.route('/search/<search_type>/<search_keyword>', defaults={'page': 1})
@app.route('/search/<search_type>/<search_keyword>/<int:page>')
def search_result(search_type, search_keyword, page): 
    limit = 10
    offset = page * limit - limit
    data = {
        'search_type': search_type, 
        'search_keyword': search_keyword,
        'limit': limit, 
        'offset': offset
    }
    search_result = Quiz.grab_quizzes_from_search(data)
    number_of_quizzes = Quiz.get_quiz_count_for_search(data)
    total_pages = math.ceil(number_of_quizzes / limit)
    next = page + 1
    prev = page - 1
    return render_template('search_result.html', search_result = search_result, pages = total_pages, next = next, prev = prev)

@app.route('/edit_profile')
def edit_profile(): 
    return render_template('/edit_profile.html')
