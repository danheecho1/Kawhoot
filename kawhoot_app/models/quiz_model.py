from kawhoot_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Quiz: 
    def __init__(self, data): 
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_blank_quiz(cls, data): 
        query = "INSERT INTO quizzes (title, description, user_id, created_at, updated_at) VALUES (%(title)s, %(description)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def get_most_recent_quiz_id(cls, data): 
        query = "SELECT * FROM quizzes WHERE user_id = %(user_id)s ORDER BY created_at DESC;"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return cls(result[0])
        return False

    @classmethod
    def get_quiz_count(cls, data):
        query = "SELECT COUNT(*) FROM quizzes LEFT JOIN users on users.id = quizzes.user_id WHERE users.id = %(user_id)s;"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return result[0]['COUNT(*)']
        return False

    @classmethod
    def get_all_quizzes(cls, data): 
        query = "SELECT *, CAST(quizzes.created_at as DATE) as created_date FROM quizzes JOIN users ON quizzes.user_id = users.id ORDER BY quizzes.created_at DESC LIMIT 1000000 OFFSET %(offset)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def get_total_quiz_count(cls):
        query = "SELECT COUNT(*) FROM quizzes;"
        result = connectToMySQL('kawhoot_schema').query_db(query)
        if result: 
            return result[0]['COUNT(*)']
        return False

    @classmethod
    def get_paginated_quizzes(cls, data): 
        query = "SELECT *, CAST(created_at as DATE) AS created_date FROM quizzes WHERE user_id = %(user_id)s ORDER BY created_at DESC LIMIT 1000000 OFFSET %(offset)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def select_quiz(cls, data): 
        query = "SELECT * FROM quizzes JOIN users ON quizzes.user_id = users.id WHERE quizzes.id = %(quiz_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def grab_quiz_to_edit(cls, data): 
        query = "SELECT * FROM quizzes LEFT JOIN questions on questions.quiz_id = quizzes.id JOIN choices ON questions.id = choices.question_id where quizzes.id = %(quiz_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def delete_quiz(cls, data): 
        query = "DELETE FROM quizzes WHERE id = %(quiz_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def update_quiz(cls, data): 
        query = "UPDATE quizzes SET title = %(title)s, description = %(description)s, updated_at = NOW() WHERE quizzes.id = %(quiz_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def grab_quizzes_from_search(cls, data):
        search_keyword = data['search_keyword']
        search_type = data['search_type']
        query = "SELECT quizzes.created_at, title, description, username, quizzes.id as quiz_id, users.id as user_id, CAST(quizzes.created_at as DATE) AS created_date FROM quizzes LEFT JOIN users ON users.id = quizzes.user_id WHERE "+search_type+ " LIKE '%%"+search_keyword+"%%' ORDER BY created_at DESC LIMIT 1000000 OFFSET %(offset)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def get_quiz_count_for_search(cls, data):
        search_keyword = data['search_keyword']
        search_type = data['search_type']
        query = "SELECT COUNT(*) FROM quizzes WHERE "+search_type+" LIKE '%%"+search_keyword+"%%';"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return result[0]['COUNT(*)']
        return False

    @classmethod
    def get_quiz_by_id(cls, data): 
        query = "SELECT * FROM quizzes WHERE quizzes.id = %(quiz_id)s;"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return result[0]
        return False

    @classmethod
    def grab_quizzes_from_my_quizzes_search(cls, data):
        search_keyword = data['search_keyword']
        search_type = data['search_type']
        query = "SELECT quizzes.created_at, title, description, username, quizzes.id as quiz_id, users.id as user_id, CAST(quizzes.created_at as DATE) AS created_date FROM quizzes LEFT JOIN users ON users.id = quizzes.user_id WHERE ("+search_type+ " LIKE '%%"+search_keyword+"%%') AND (user_id = %(user_id)s) ORDER BY created_at DESC LIMIT 1000000 OFFSET %(offset)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def get_my_quiz_count_for_search(cls, data):
        search_keyword = data['search_keyword']
        search_type = data['search_type']
        query = "SELECT COUNT(*) FROM quizzes WHERE ("+search_type+" LIKE '%%"+search_keyword+"%%') AND (user_id = %(user_id)s) ORDER BY created_at DESC LIMIT 1000000 OFFSET %(offset)s;"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return result[0]['COUNT(*)']
        return False
