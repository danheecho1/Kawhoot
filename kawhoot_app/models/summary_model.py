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