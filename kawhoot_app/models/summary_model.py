from kawhoot_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Summary: 
    def __init__(self, data): 
        self.id = data['id']
        self.number_of_takers = data['number_of_takers']
        self.total_scores = data['total_scores']
        self.average_score = data['average_score']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_summary(cls, data): 
        query = "INSERT INTO summaries (number_of_takers, total_scores, average_score, created_at, updated_at, quiz_id) VALUES (0, 0, 0, NOW(), NOW(), %(quiz_id)s);"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def update_summary(cls, data):
        query = "UPDATE summaries SET number_of_takers = number_of_takers + 1, total_scores = total_scores + %(score)s, average_score = total_scores / number_of_takers, updated_at = NOW() WHERE quiz_id = %(quiz_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def grab_summary(cls, data): 
        query = "SELECT * FROM summaries WHERE quiz_id = %(quiz_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)
