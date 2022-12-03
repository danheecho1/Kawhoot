# This controller handles dashboard and all records routes

from kawhoot_app import app
from kawhoot_app.models.user_model import User
from kawhoot_app.models.quiz_model import Quiz
from kawhoot_app.models.result_model import Result
from kawhoot_app.models.userSummary_model import UserSummary

import math
from flask import render_template, redirect, session, request

@app.route('/dashboard')
def test(): 
    if User.validate_session(session): 
        data = {
            'user_id': session['logged_in_user_id']
        }
        user = User.get_user_by_id(data)
        my_quizzes_count = Quiz.get_quiz_count(data)
        my_attempts_count = Result.get_my_attempts_count(data)
        attempts_at_my_quizzes_count = Result.get_attempts_count(data)
        average_for_my_quizzes = Result.get_unweighted_avg_for_my_quizzes(data)
        my_average_score = Result.get_my_average_score(data)
        my_total_score = UserSummary.get_my_total_score_earned(data)
        scorehunters = UserSummary.get_scorehunters()
        steadyhunters = UserSummary.get_steadyhunters()
        quizcreators = UserSummary.get_quizcreators()
        quiztakers = UserSummary.get_quiztakers()
        return render_template('dashboard.html', user = user, my_quizzes_count = my_quizzes_count, my_attempts_count = my_attempts_count, attempts_at_my_quizzes_count = attempts_at_my_quizzes_count, average_for_my_quizzes = average_for_my_quizzes, my_average_score = my_average_score, my_total_score = my_total_score, scorehunters = scorehunters, steadyhunters = steadyhunters, quizcreators = quizcreators, quiztakers = quiztakers)
    return redirect('/')

@app.route('/dashboard/attempts', defaults={'page': 1})
@app.route('/dashboard/attempts/<int:page>')
def attempts_at_me(page): 
    if User.validate_session(session): 
        limit = 10
        offset = page * limit - limit
        data = {
            'user_id': session['logged_in_user_id'],
            'limit': limit, 
            'offset': offset
        }
        attempts_at_my_quizzes = Result.grab_attempts_at_my_quiz(data)
        number_of_attempts = Result.get_attempts_count(data)
        total_pages = math.ceil(number_of_attempts / limit)
        next = page + 1
        prev = page - 1
        return render_template('attempts.html', attempts = attempts_at_my_quizzes, pages = total_pages, next = next, prev = prev)
    return redirect('/')

@app.route('/dashboard/attempts/search_post', methods=['POST'])
def attempts_at_me_search_post():
    if User.validate_session(session): 
        if request.form['search_keyword']:
            search_keyword = request.form['search_keyword']
            search_type = request.form['search_type']
            return redirect(f'/dashboard/attempts/search/{search_type}/{search_keyword}')
        return redirect('/dashboard/attempts')
    return redirect('/')

@app.route('/dashboard/attempts/search/<search_type>/<search_keyword>', defaults={'page': 1})
@app.route('/dashboard/attempts/search/<search_type>/<search_keyword>/<int:page>')
def attempts_at_me_search(page, search_type, search_keyword): 
    if User.validate_session(session):
        limit = 10
        offset = page * limit - limit
        data = {
            'user_id': session['logged_in_user_id'],
            'limit': limit, 
            'offset': offset, 
            'search_type': search_type, 
            'search_keyword': search_keyword
        }
        attempts_at_my_quizzes = Result.grab_attempts_at_my_quiz_from_search(data)
        number_of_attempts = Result.get_attempts_count_from_search(data)
        total_pages = math.ceil(number_of_attempts / limit)
        next = page + 1
        prev = page - 1
        return render_template('attempts_search.html', attempts = attempts_at_my_quizzes, pages = total_pages, next = next, prev = prev, search_type = search_type, search_keyword = search_keyword)
    return redirect('/')

@app.route('/dashboard/myattempts', defaults={'page': 1})
@app.route('/dashboard/myattempts/<int:page>')
def my_attempts(page): 
    if User.validate_session(session):
        limit = 10
        offset = page * limit - limit
        data = {
            'user_id': session['logged_in_user_id'],
            'limit': limit, 
            'offset': offset
        }
        my_attempts = Result.get_my_attempts(data)
        number_of_attempts = Result.get_my_attempts_count(data)
        total_pages = math.ceil(number_of_attempts / limit)
        next = page + 1
        prev = page - 1
        return render_template('my_attempts.html', attempts = my_attempts, pages = total_pages, next = next, prev = prev)
    return redirect('/')

@app.route('/dashboard/myattempts/search_post', methods=['POST'])
def my_attempts_search_post():
    if User.validate_session(session):
        if request.form['search_keyword']:
            search_keyword = request.form['search_keyword']
            search_type = request.form['search_type']
            return redirect(f'/dashboard/myattempts/search/{search_type}/{search_keyword}')
        return redirect('/dashboard/myattempts')
    return redirect('/')

@app.route('/dashboard/myattempts/search/<search_type>/<search_keyword>', defaults={'page': 1})
@app.route('/dashboard/myattempts/search/<search_type>/<search_keyword>/<int:page>')
def my_attempts_search(page, search_type, search_keyword): 
    if User.validate_session(session):
        limit = 10
        offset = page * limit - limit
        data = {
            'user_id': session['logged_in_user_id'],
            'limit': limit, 
            'offset': offset, 
            'search_type': search_type, 
            'search_keyword': search_keyword
        }
        my_attempts = Result.get_my_attempts_from_search(data)
        number_of_attempts = Result.get_my_attempts_count_from_search(data)
        total_pages = math.ceil(number_of_attempts / limit)
        next = page + 1
        prev = page - 1
        return render_template('my_attempts_search.html', attempts = my_attempts, pages = total_pages, next = next, prev = prev, search_type = search_type, search_keyword = search_keyword)
    return redirect('/')