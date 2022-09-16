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

