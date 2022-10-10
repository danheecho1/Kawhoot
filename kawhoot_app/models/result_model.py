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