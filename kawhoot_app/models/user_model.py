from kawhoot_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User: 
    def __init__(self, data): 
        self.id = data['id']
        self.username = data['username']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register_user(cls, data): 
        query = "INSERT INTO users (username, password, created_at, updated_at) VALUES (%(username)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def get_user_by_username(cls, data): 
        query = "SELECT * FROM users WHERE username = %(username)s;"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return cls(result[0])
        return False

    @classmethod
    def get_user_by_id(cls, data): 
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        result = connectToMySQL('kawhoot_schema').query_db(query, data)
        if result: 
            return cls(result[0])
        return False

    @classmethod
    def update_username(cls, data): 
        query = "UPDATE users SET username = %(username)s, updated_at = NOW() WHERE id = %(user_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @classmethod
    def update_password(cls, data): 
        query = "UPDATE users SET password = %(new_password)s, updated_at = NOW() WHERE id = %(user_id)s;"
        return connectToMySQL('kawhoot_schema').query_db(query, data)

    @staticmethod
    def validate_new_username(data): 
        is_valid = True
        if len(data['username']) < 1: 
            flash("Username is required", 'username')
            is_valid = False
        elif len(data['username']) < 6: 
            flash("Username must be at least 5 characters", 'username')
            is_valid = False
        elif len(data['username']) > 16: 
            flash("Username must be 15 characters or shorter", 'username')
            is_valid = False
        else: 
            existing_user = User.get_user_by_username(data)
            if existing_user: 
                flash("Username already exists", 'username')
                is_valid = False
        return is_valid

    @staticmethod
    def validate_new_password(data):
        is_valid = True
        # checking that the password is at least 8 characters
        if len(data['new_password']) < 8: 
            flash("Password must be at least 8 characters", 'new_password')
            is_valid = False
        elif len(data['confirm']) < 1: 
            flash("Confirm password is required", 'confirm')
            is_valid = False
        # checking that confirm password matches
        elif data['new_password'] != data['confirm']: 
            flash("Passwords do not match", 'confirm')
            is_valid = False
        # this static method returns a boolean value of is_valid 
        return is_valid

    @staticmethod
    def validate_registration(data):
        # default is_valid value is true
        is_valid = True
        # for validating a username, we will have three steps: 1) an appropriate username is provided, and 2) it is not a duplicate. 
        # 1) checking that a username is provided
        if len(data['username']) < 1: 
            flash("Username is required", 'username')
            is_valid = False
        elif len(data['username']) < 6: 
            flash("Username must be at least 5 characters", 'username')
            is_valid = False
        elif len(data['username']) > 16: 
            flash("Username must be 15 characters or shorter", 'username')
            is_valid = False
        # 2) provided username is not a duplicate
        else: 
            existing_user = User.get_user_by_username({'username': data['username']})
            if existing_user: 
                flash("Username already exists", 'username')
                is_valid = False
        # checking that the password is at least 8 characters
        if len(data['password']) < 8: 
            flash("Password must be at least 8 characters", 'password')
            is_valid = False
        # checking that confirm password matches
        if data['password'] != data['confirm']: 
            flash("passwords do not match", 'confirm')
            is_valid = False
        # this static method returns a boolean value of is_valid 
        return is_valid