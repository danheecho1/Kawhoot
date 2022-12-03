# This controller handles search (not including searches from dashboard-records) and quiz attempt routes

from kawhoot_app import app
from kawhoot_app.models.user_model import User
from kawhoot_app.models.quiz_model import Quiz
from kawhoot_app.models.question_model import Question
from kawhoot_app.models.summary_model import Summary
from kawhoot_app.models.userSummary_model import UserSummary
from kawhoot_app.models.result_model import Result

import math
from flask import render_template, redirect, session, request

@app.route('/search', defaults={'page': 1})
@app.route('/search/<int:page>')
def search(page): 
    if User.validate_session(session):
        limit = 10
        offset = page * limit - limit
        data = {
            'limit': limit, 
            'offset': offset
        }
        quizzes = Quiz.get_all_quizzes(data)
        number_of_quizzes = Quiz.get_total_quiz_count()
        total_pages = math.ceil(number_of_quizzes / limit)
        next = page + 1
        prev = page - 1
        return render_template('/search.html', quizzes = quizzes, pages = total_pages, next = next, prev = prev)
    return redirect('/')

@app.route('/search', methods=['post'])
def search_post(): 
    if User.validate_session(session):
        if request.form['search_keyword']:
            search_type = request.form['search_type']
            search_keyword = request.form['search_keyword']
            return redirect(f'/search/{search_type}/{search_keyword}')
        return redirect('/search')
    return redirect('/')

@app.route('/search/<search_type>/<search_keyword>', defaults={'page': 1})
@app.route('/search/<search_type>/<search_keyword>/<int:page>')
def search_result(search_type, search_keyword, page): 
    if User.validate_session(session):
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
        return render_template('search_result.html', search_type = search_type, search_keyword = search_keyword, search_result = search_result, pages = total_pages, next = next, prev = prev)
    return redirect('/')

@app.route('/search/quiz/<int:user_id>/<int:quiz_id>')
def select_quiz_from_search(user_id, quiz_id):
    if User.validate_session(session):
        data = {
            'quiz_id': quiz_id, 
            'taker': session['logged_in_user_id'], 
            'maker': user_id
        }
        quiz = Quiz.select_quiz(data)
        quiz_owner_id = user_id
        logged_in_user_id = session['logged_in_user_id']
        count = Result.get_count(data)
        summary = Summary.grab_summary(data)
        leaders = Result.get_leaderboard(data)
        taken = Result.check_if_taken(data)
        print(taken)
        return render_template('select_search.html', taken = taken, leaders = leaders, summary = summary, count = count, quiz = quiz, quiz_owner_id = quiz_owner_id, logged_in_user_id = logged_in_user_id)
    return redirect('/')

@app.route('/quiz/<int:user_id>/<int:quiz_id>')
def select_quiz(user_id, quiz_id): 
    if User.validate_session(session):
        data = {
            'quiz_id': quiz_id
        }
        quiz = Quiz.select_quiz(data)
        quiz_owner_id = user_id
        logged_in_user_id = session['logged_in_user_id']
        count = Result.get_count(data)
        summary = Summary.grab_summary(data)
        leaders = Result.get_leaderboard(data)
        return render_template('select_my_quiz.html', leaders = leaders, summary = summary, count = count, quiz = quiz, quiz_owner_id = quiz_owner_id, logged_in_user_id = logged_in_user_id)
    return redirect('/')

@app.route('/quiz/<user_id>/<quiz_id>/go')
def taking_quiz(user_id, quiz_id): 
    if User.validate_session(session):
        quiz = Quiz.get_quiz_by_id({'quiz_id': quiz_id})
        questions = Question.grab_questions_for_quiz({'quiz_id': quiz_id})
        return render_template('taking_quiz.html', quiz = quiz, questions = questions, user_id = user_id, quiz_id = quiz_id)
    return redirect('/')

@app.route('/quiz/<user_id>/<quiz_id>/done', methods=['post'])
def grade_quiz(user_id, quiz_id): 
    if User.validate_session(session):
        score = 0;
        choice1 = request.form['answer1']
        choice2 = request.form['answer2']
        choice3 = request.form['answer3']
        choice4 = request.form['answer4']
        choice5 = request.form['answer5']
        choice6 = request.form['answer6']
        choice7 = request.form['answer7']
        choice8 = request.form['answer8']
        choice9 = request.form['answer9']
        choice10 = request.form['answer10']
        answers = Question.grab_questions_for_quiz({'quiz_id': quiz_id})

        if choice1 == answers[0]['correct_answer']: 
            score += 1
        if choice2 == answers[1]['correct_answer']: 
            score += 1
        if choice3 == answers[2]['correct_answer']: 
            score += 1
        if choice4 == answers[3]['correct_answer']: 
            score += 1
        if choice5 == answers[4]['correct_answer']: 
            score += 1
        if choice6 == answers[5]['correct_answer']: 
            score += 1
        if choice7 == answers[6]['correct_answer']: 
            score += 1
        if choice8 == answers[7]['correct_answer']: 
            score += 1
        if choice9 == answers[8]['correct_answer']: 
            score += 1
        if choice10 == answers[9]['correct_answer']: 
            score += 1

        data = {
            'score': score, 
            'user_id': session['logged_in_user_id'], 
            'quiz_id': quiz_id
        }
        Result.save_grade(data)
        Summary.update_summary(data)
        UserSummary.update_user_summary(data)
        return redirect(f'/quiz/{user_id}/{quiz_id}/result')
    return redirect('/')

@app.route('/quiz/<user_id>/<quiz_id>/result')
def quiz_result(user_id, quiz_id):
    if User.validate_session(session):
        data = {
            'user_id': session['logged_in_user_id'], 
            'quiz_id': quiz_id
        }
        result = Result.grab_result(data)
        summary = Summary.grab_summary(data)
        quiz = Quiz.select_quiz(data)
        return render_template('quiz_result.html', summary = summary, result = result, quiz = quiz)
    return redirect('/')