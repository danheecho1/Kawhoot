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
