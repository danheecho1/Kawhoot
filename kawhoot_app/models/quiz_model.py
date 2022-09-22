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
    def get_paginated_posts(cls, data): 
        query = "SELECT *, CAST(created_at as DATE) AS created_date FROM quizzes WHERE user_id = %(user_id)s ORDER BY created_at DESC LIMIT 1000000 OFFSET %(offset)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)