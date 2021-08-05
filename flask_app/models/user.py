from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt 
from flask_app import app 
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
bcrypt = Bcrypt(app)
schema = "ninjaGame"

class User:
    def __init__(self,data):
        self.id=data['id']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO users (email,password)
        VALUES (%(email)s, %(password)s);
        """
        post_data={
            **data,
            'password': bcrypt.generate_password_hash(data['password'])
        }
        return connectToMySQL(schema).query_db(query,post_data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(schema).query_db(query)
        all_users = [];
        for result in results:
            all_users.append(cls(result))
        return all_users

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users;"
        results = connectToMySQL(schema).query_db(query,data)
        return cls(results[0]);
        
    @classmethod
    def get_user_by_email(cls,data):
        query = "SELECT * FROM users WHERE email= %(email)s;"
        results = connectToMySQL(schema).query_db(query,data)
        # print("*"*80)
        # print(results)
        if results == ():
            return False

        return cls(results[0])

    
    @classmethod
    def logUser(cls,data):
        print (data)
        user1 = cls.get_user_by_email(data)
       
        return user1.id
        
    
    
    @staticmethod
    def check_cred(post_data):
        if len(post_data['email']) >0 and len(post_data['password'])>0:
            user1 = User.get_user_by_email(post_data)
            
            if (user1):
                print (post_data['password'])
                if bcrypt.check_password_hash(user1.password, post_data['password']):
                    return True
                    
                
        return False
    
    

    @staticmethod
    def validate_user(post_data):
        is_valid = True

        if len(post_data['password'])<8:
            flash("Password must be longer then 7 characters")
            is_valid=False;
        elif post_data['password'] != post_data['cpassword']:
            flash("Password does not match Confirm Password")
            is_valid=False;

        if not EMAIL_REGEX.match(post_data['email']): 
            flash("Invalid email address!")
            is_valid = False
        elif User.get_user_by_email(post_data):
            flash("e-mail already in use")
            is_valid=False;
        
        return is_valid

        