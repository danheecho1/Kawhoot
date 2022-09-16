from kawhoot_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Question: 
    def __init__(self, data): 
        self.id = data['id']
        self.prompt = data['prompt']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_question(cls, data): 
        query = "INSERT INTO questions (prompt, quiz_id, created_at, updated_at) VALUES (%(prompt)s, %(quiz_id)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

