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

    @classmethod
    def update_choices(cls, data): 
        query = "UPDATE choices SET updated_at = NOW(), a = (CASE WHEN id = %(question1_id)s THEN %(1a)s WHEN id = %(question2_id)s THEN %(2a)s WHEN id = %(question3_id)s THEN %(3a)s WHEN id = %(question4_id)s THEN %(4a)s WHEN id = %(question5_id)s THEN %(5a)s WHEN id = %(question6_id)s THEN %(6a)s WHEN id = %(question7_id)s THEN %(7a)s WHEN id = %(question8_id)s THEN %(8a)s WHEN id = %(question9_id)s THEN %(9a)s WHEN id = %(question10_id)s THEN %(10a)s WHEN id THEN a END), b = (CASE WHEN id = %(question1_id)s THEN %(1b)s WHEN id = %(question2_id)s THEN %(2b)s WHEN id = %(question3_id)s THEN %(3b)s WHEN id = %(question4_id)s THEN %(4b)s WHEN id = %(question5_id)s THEN %(5b)s WHEN id = %(question6_id)s THEN %(6b)s WHEN id = %(question7_id)s THEN %(7b)s WHEN id = %(question8_id)s THEN %(8b)s WHEN id = %(question9_id)s THEN %(9b)s WHEN id = %(question10_id)s THEN %(10b)s WHEN id THEN b END), c = (CASE WHEN id = %(question1_id)s THEN %(1c)s WHEN id = %(question2_id)s THEN %(2c)s WHEN id = %(question3_id)s THEN %(3c)s WHEN id = %(question4_id)s THEN %(4c)s WHEN id = %(question5_id)s THEN %(5c)s WHEN id = %(question6_id)s THEN %(6c)s WHEN id = %(question7_id)s THEN %(7c)s WHEN id = %(question8_id)s THEN %(8c)s WHEN id = %(question9_id)s THEN %(9c)s WHEN id = %(question10_id)s THEN %(10c)s  WHEN id THEN c END), d = (CASE WHEN id = %(question1_id)s THEN %(1d)s WHEN id = %(question2_id)s THEN %(2d)s WHEN id = %(question3_id)s THEN %(3d)s WHEN id = %(question4_id)s THEN %(4d)s WHEN id = %(question5_id)s THEN %(5d)s WHEN id = %(question6_id)s THEN %(6d)s WHEN id = %(question7_id)s THEN %(7d)s WHEN id = %(question8_id)s THEN %(8d)s WHEN id = %(question9_id)s THEN %(9d)s WHEN id = %(question10_id)s THEN %(10d)s WHEN id THEN d END), e = (CASE WHEN id = %(question1_id)s THEN %(1e)s WHEN id = %(question2_id)s THEN %(2e)s WHEN id = %(question3_id)s THEN %(3e)s WHEN id = %(question4_id)s THEN %(4e)s WHEN id = %(question5_id)s THEN %(5e)s WHEN id = %(question6_id)s THEN %(6e)s WHEN id = %(question7_id)s THEN %(7e)s WHEN id = %(question8_id)s THEN %(8e)s WHEN id = %(question9_id)s THEN %(9e)s WHEN id = %(question10_id)s THEN %(10e)s WHEN id THEN e END), correct_answer = (CASE WHEN id = %(question1_id)s THEN %(1answer)s WHEN id = %(question2_id)s THEN %(2answer)s WHEN id = %(question3_id)s THEN %(3answer)s WHEN id = %(question4_id)s THEN %(4answer)s WHEN id = %(question5_id)s THEN %(5answer)s WHEN id = %(question6_id)s THEN %(6answer)s WHEN id = %(question7_id)s THEN %(7answer)s WHEN id = %(question8_id)s THEN %(8answer)s WHEN id = %(question9_id)s THEN %(9answer)s WHEN id = %(question10_id)s THEN %(10answer)s WHEN id THEN correct_answer END);"
        return connectToMySQL('kawhoot_schema').query_db(query, data)