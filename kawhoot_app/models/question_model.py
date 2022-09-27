from kawhoot_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Question: 
    def __init__(self, data): 
        self.id = data['id']
        self.prompt = data['prompt']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_questions(cls, data): 
        query = "INSERT INTO questions (prompt, created_at, updated_at, quiz_id) VALUES (%(prompt1)s, NOW(), NOW(), %(quiz_id)s), (%(prompt2)s, NOW(), NOW(), %(quiz_id)s), (%(prompt3)s, NOW(), NOW(), %(quiz_id)s), (%(prompt4)s, NOW(), NOW(), %(quiz_id)s), (%(prompt5)s, NOW(), NOW(), %(quiz_id)s), (%(prompt6)s, NOW(), NOW(), %(quiz_id)s), (%(prompt7)s, NOW(), NOW(), %(quiz_id)s), (%(prompt8)s, NOW(), NOW(), %(quiz_id)s), (%(prompt9)s, NOW(), NOW(), %(quiz_id)s), (%(prompt10)s, NOW(), NOW(), %(quiz_id)s);"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def get_most_recent_question_ids(cls, data):
        query = "SELECT id FROM questions WHERE quiz_id = %(quiz_id)s ORDER BY id DESC;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def update_questions(cls, data): 
        query = "UPDATE questions SET updated_at = NOW(), prompt = (CASE WHEN id = %(question1_id)s THEN %(prompt1)s WHEN id = %(question2_id)s THEN %(prompt2)s WHEN id = %(question3_id)s THEN %(prompt3)s WHEN id = %(question4_id)s THEN %(prompt4)s WHEN id = %(question5_id)s THEN %(prompt5)s WHEN id = %(question6_id)s THEN %(prompt6)s WHEN id = %(question7_id)s THEN %(prompt7)s WHEN id = %(question8_id)s THEN %(prompt8)s WHEN id = %(question9_id)s THEN %(prompt9)s WHEN id = %(question10_id)s THEN %(prompt10)s WHEN id THEN prompt END);"
        return connectToMySQL('kawhoot_schema').query_db(query, data)
