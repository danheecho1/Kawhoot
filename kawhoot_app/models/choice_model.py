from kawhoot_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Choice: 
    def __init__(self, data): 
        self.id = data['id']
        self.a = data['a']
        self.b = data['b']
        self.c = data['c']
        self.d = data['d']
        self.e = data['e']
        self.correct_answer = data['correct_answer']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_choices(cls, data): 
        query = "INSERT INTO choices (a, b, c, d, e, correct_answer, created_at, updated_at, question_id) VALUES (%(1a)s, %(1b)s, %(1c)s, %(1d)s, %(1e)s, %(1answer)s, NOW(), NOW(), %(question1_id)s), (%(2a)s, %(2b)s, %(2c)s, %(2d)s, %(2e)s, %(2answer)s, NOW(), NOW(), %(question2_id)s), (%(3a)s, %(3b)s, %(3c)s, %(3d)s, %(3e)s, %(3answer)s, NOW(), NOW(), %(question3_id)s), (%(4a)s, %(4b)s, %(4c)s, %(4d)s, %(4e)s, %(4answer)s, NOW(), NOW(), %(question4_id)s), (%(5a)s, %(5b)s, %(5c)s, %(5d)s, %(5e)s, %(5answer)s, NOW(), NOW(), %(question5_id)s), (%(6a)s, %(6b)s, %(6c)s, %(6d)s, %(6e)s, %(6answer)s, NOW(), NOW(), %(question6_id)s), (%(7a)s, %(7b)s, %(7c)s, %(7d)s, %(7e)s, %(7answer)s, NOW(), NOW(), %(question7_id)s), (%(8a)s, %(8b)s, %(8c)s, %(8d)s, %(8e)s, %(8answer)s, NOW(), NOW(), %(question8_id)s), (%(9a)s, %(9b)s, %(9c)s, %(9d)s, %(9e)s, %(9answer)s, NOW(), NOW(), %(question9_id)s), (%(10a)s, %(10b)s, %(10c)s, %(10d)s, %(10e)s, %(10answer)s, NOW(), NOW(), %(question10_id)s);"
        return connectToMySQL('kawhoot_schema').query_db(query, data)