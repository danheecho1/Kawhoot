from kawhoot_app.config.mysqlconnection import connectToMySQL
from flask import flash

class UserSummary: 
    def __init__(self, data): 
        self.id = data['id']
        self.total_score_earned = data['total_score_earned']
        self.average_score = data['average_score']
        self.attempt_count = data['attempt_count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user_summary(cls, data): 
        query = "INSERT INTO usersummaries (total_score_earned, average_score, attempt_count, created_at, updated_at, user_id) VALUES (0, 0, 0, NOW(), NOW(), %(user_id)s;);"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def update_user_summary(cls, data):
        query = "UPDATE usersummaries SET total_score_earned = total_score_earned + %(score)s, attempt_count = attempt_count + 1, average_score = (total_score_earned / attempt_count), updated_at = NOW() WHERE user_id = %(user_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)
