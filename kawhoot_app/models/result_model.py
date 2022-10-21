from kawhoot_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Result: 
    def __init__(self, data): 
        self.id = data['id']
        self.score = data['score']
        self.created_at = data['created_at']

    @classmethod
    def save_grade(cls, data): 
        query = "INSERT INTO results (score, created_at, user_id, quiz_id) VALUES (%(score)s, NOW(), %(user_id)s, %(quiz_id)s);"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def grab_result(cls, data):
        query = "SELECT quizzes.id, score, results.created_at AS result_created_at, results.user_id, results.quiz_id, username, title, description, quizzes.created_at AS quiz_created_at FROM results LEFT JOIN users ON results.user_id = users.id LEFT JOIN quizzes ON results.quiz_id = quizzes.id WHERE (results.user_id = %(user_id)s AND results.quiz_id = %(quiz_id)s);"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def get_count(cls, data):
        query = "SELECT COUNT(*) FROM results WHERE quiz_id = %(quiz_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def get_leaderboard(cls, data):
        query = "SELECT results.id, score, results.created_at, user_id, quiz_id, username FROM results JOIN users ON results.user_id = users.id WHERE quiz_id = %(quiz_id)s ORDER BY score DESC, results.created_at ASC;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def check_if_taken(cls, data):
        query = "SELECT * FROM results WHERE (quiz_id = %(quiz_id)s AND user_id = %(taker)s);"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return result[0]
        return False

    @classmethod
    def grab_attempts_at_my_quiz(cls, data): 
        query = "SELECT score, CAST(results.created_at AS DATE) AS date, title, username FROM results JOIN quizzes ON quizzes.id = results.quiz_id JOIN users ON results.user_id = users.id WHERE quizzes.user_id = %(user_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def grab_attempts_at_my_quiz_from_search(cls, data): 
        search_keyword = data['search_keyword']
        search_type = data['search_type']
        query = "SELECT score, CAST(results.created_at AS DATE) AS date, title, username FROM results JOIN quizzes ON quizzes.id = results.quiz_id JOIN users ON results.user_id = users.id WHERE (quizzes.user_id = %(user_id)s AND "+search_type+" LIKE '%%" + search_keyword + "%%') ORDER BY results.created_at DESC;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def get_attempts_count(cls, data): 
        query = "SELECT COUNT(*) FROM results JOIN quizzes ON quizzes.id = results.quiz_id WHERE quizzes.user_id = %(user_id)s;"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return result[0]['COUNT(*)']
        return False

    @classmethod
    def get_my_attempts(cls, data): 
        query = "SELECT score, CAST(results.created_at AS DATE) AS date, title, username FROM results JOIN quizzes ON results.quiz_id = quizzes.id JOIN users ON quizzes.user_id = users.id WHERE results.user_id = %(user_id)s ORDER BY results.created_at DESC;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def get_my_attempts_count(cls, data):
        query = "SELECT COUNT(*) FROM results JOIN quizzes ON results.quiz_id = quizzes.id JOIN users ON quizzes.user_id = users.id WHERE results.user_id = %(user_id)s;"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return result[0]['COUNT(*)']
        return False

    @classmethod
    def get_unweighted_avg_for_my_quizzes(cls, data):
        query = "SELECT CAST(AVG(score) AS DECIMAL(10, 1)) FROM results JOIN quizzes ON results.quiz_id = quizzes.id JOIN users ON quizzes.user_id = users.id WHERE users.id = %(user_id)s;"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return result[0]['CAST(AVG(score) AS DECIMAL(10, 1))']
        return False

    @classmethod
    def get_my_average_score(cls, data): 
        query = "SELECT CAST(AVG(score) AS DECIMAL(10, 1)) FROM results WHERE user_id = %(user_id)s;"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return result[0]['CAST(AVG(score) AS DECIMAL(10, 1))']
        return False