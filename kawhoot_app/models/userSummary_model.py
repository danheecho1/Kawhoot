from kawhoot_app.config.mysqlconnection import connectToMySQL
from flask import flash

class UserSummary: 
    def __init__(self, data): 
        self.id = data['id']
        self.total_score_earned = data['total_score_earned']
        self.total_score_earned_updated_at = data['total_score_earned_updated_at']
        self.average_score = data['average_score']
        self.average_score_updated_at = data['average_score_updated_at']
        self.attempt_count = data['attempt_count']
        self.attempt_count_updated_at = data['attempt_count_updated_at']
        self.create_quiz_count = data['create_quiz_count']
        self.create_quiz_count_updated_at = data['create_quiz_count_updated_at']
        self.created_at = data['created_at']

    @classmethod
    def create_user_summary(cls, data): 
        query = "INSERT INTO usersummaries (total_score_earned, total_score_earned_updated_at, average_score, average_score_updated_at, attempt_count, attempt_count_updated_at, create_quiz_count, create_quiz_count_updated_at, created_at, user_id) VALUES (0, NOW(), 0, NOW(), 0, NOW(), 0, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def update_user_summary(cls, data):
        query = "UPDATE usersummaries SET total_score_earned = total_score_earned + %(score)s, total_score_earned_updated_at = NOW(), attempt_count = attempt_count + 1, attempt_count_updated_at = NOW(), average_score = (total_score_earned / attempt_count), average_score_updated_at = NOW() WHERE user_id = %(user_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)
    
    @classmethod
    def update_user_summary_create_quiz(cls, data):
        query = "UPDATE usersummaries SET create_quiz_count = create_quiz_count + 1, create_quiz_count_updated_at = NOW() WHERE user_id = %(user_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def get_my_total_score_earned(cls, data):
        query = "SELECT total_score_earned FROM usersummaries WHERE user_id = %(user_id)s;"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return result[0]['total_score_earned']
        return False

    @classmethod
    def get_scorehunters(cls):
        query = "SELECT username, total_score_earned FROM usersummaries JOIN users ON usersummaries.user_id = users.id WHERE total_score_earned > 0 ORDER BY total_score_earned DESC, total_score_earned_updated_at ASC LIMIT 5;"
        return connectToMySQL('kawhoot_schema').query_db(query)

    @classmethod
    def get_steadyhunters(cls):
        query = "SELECT username, average_score FROM usersummaries JOIN users ON usersummaries.user_id = users.id WHERE average_score > 0 ORDER BY average_score DESC, average_score_updated_at ASC LIMIT 5;"
        return connectToMySQL('kawhoot_schema').query_db(query)

    @classmethod
    def get_quizcreators(cls):
        query = "SELECT username, create_quiz_count FROM usersummaries JOIN users ON usersummaries.user_id = users.id WHERE create_quiz_count > 0 ORDER BY create_quiz_count DESC, create_quiz_count_updated_at ASC LIMIT 5;"
        return connectToMySQL('kawhoot_schema').query_db(query)
    
    @classmethod
    def get_quiztakers(cls):
        query = "SELECT attempt_count, username FROM usersummaries JOIN users ON usersummaries.user_id = users.id WHERE attempt_count > 0 ORDER BY attempt_count DESC, attempt_count_updated_at ASC LIMIT 5;"
        return connectToMySQL('kawhoot_schema').query_db(query)