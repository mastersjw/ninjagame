from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt 
from flask_app import app 
from flask import flash
from flask_app.models import user,character

schema = "ninjaGame"
class Enemy:

    def __init__(self, data):
        self.health = data['health']
        self.id= data['id']
        self.power=data['power']
        self.character_id=data['character_id']
        self.max_health= data['max_health']
        



    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM enemies WHERE id = %(id)s;"
        result = connectToMySQL(schema).query_db(query,data)
        if result != False and result!=():
            return cls(result[0])
        else: return None;
    
    @classmethod
    def create(cls,data):
        query= "INSERT INTO enemies (character_id, health, max_health,power) VALUES (%(character_id)s,100,100,20);"
        result = connectToMySQL(schema).query_db(query,data);
        return result

    @classmethod
    def delEnemy(cls,data):
        query="DELETE FROM enemies WHERE id =%(id)s;"
        return connectToMySQL(schema).query_db(query,data)

    @classmethod
    def update_health(cls,data):
        query = "UPDATE enemies SET health = %(health)s WHERE id = %(id)s;"
        return connectToMySQL(schema).query_db(query,data)
