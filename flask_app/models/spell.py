

from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt 
from flask_app import app 
from flask import flash
from flask_app.models import user,character

schema = "ninjaGame"
class Spell:

    def __init__(self, data):
        self.id= data['id']
        self.power=data['power']
        self.type=data['type']
        self.name= data['name']
        



    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM spells WHERE id = %(id)s;"
        result = connectToMySQL(schema).query_db(query,data)
        if result != False and result!=():
            return cls(result[0])
        else: return None;

    @classmethod
    def get_one_by_name(cls,data):
        query = "SELECT * FROM spells WHERE name=%(name)s;"
        result = connectToMySQL(schema).query_db(query,data)
        if result != False and result!=():
            return cls(result[0])
        else: return None;
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM spells;"
        results = connectToMySQL(schema).query_db(query)
        spells = []
        for result in results:
            spells.append(cls(result))
        
        return spells

    @classmethod
    def add_starters(cls):
        query = "INSERT INTO spells (power,type,name) VALUES (10,'phys','Punch');"
        query2= "INSERT INTO spells (power,type,name) VALUES(10,'magic','Poison');"
        connectToMySQL(schema).query_db(query)
        connectToMySQL(schema).query_db(query2)
        
    