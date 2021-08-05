from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt 
from flask_app import app 
from flask import flash
from flask_app.models import user,character,enemy,spell
import random

schema = "ninjaGame"
class Character:

    def __init__(self, data):
        self.id=data['id']
        self.name = data['name']
        self.dexterity = data['dexterity']
        self.health = data['health']
        self.stamina = data['stamina']
        self.mana = data['mana']
        self.strength = data['strength']
        self.loc_x =  data['loc_x']
        self.loc_y =  data['loc_y']
        self.level = data['level']
        self.xp = data['xp']
        self.intelligence = data['intelligence']
        self.user_id = data['user_id']
        if data['user_id']:
            self.user = user.User.get_one({'id': data['user_id']})
        
        self.enemy={};
        self.spells =[];
        

    @classmethod
    def move_char(cls,data):
        char1 = Character.get_one_by_user_id(data)
        if data['direction'] == 'N':
            char1.loc_x = char1.loc_x-1
        elif data['direction']=='S':
            char1.loc_x= char1.loc_x+1
        elif data['direction']=='E':
            char1.loc_y= char1.loc_y+1
        else: char1.loc_y-=1
        if(char1.loc_x<0 or char1.loc_x>20 or char1.loc_y<0 or char1.loc_y>20):
            flash("Cannot go that way")
            return False
        post_data ={
            'user_id': data['user_id'],
            'loc_x': char1.loc_x,
            'loc_y': char1.loc_y
        } 
        query = "UPDATE characters SET loc_x = %(loc_x)s, loc_y = %(loc_y)s WHERE user_id = %(user_id)s;"
        if random.randint(0,3) == 2 and char1.enemy =={}: enemy.Enemy.create({'character_id':char1.id})
        
     
        
        return connectToMySQL(schema).query_db(query, post_data)

    @classmethod
    def get_one_by_user_id(cls,data):
        char1 = False
        query = "SELECT * FROM characters LEFT JOIN enemies on characters.id = enemies.character_id WHERE characters.user_id = %(user_id)s;"
        results = connectToMySQL(schema).query_db(query,data)
        if results != False and results!=():
            char1 =  cls(results[0])
            if results[0]['enemies.id'] != None:
                for result in results:
                    post_data = {
                        "id": result['enemies.id'],
                        "character_id": result['id'],
                        "power": result["power"],
                        "health": result['enemies.health'],
                        "max_health": result['max_health']
                        }
                char1.enemy= enemy.Enemy(post_data);
        
        query = "SELECT * FROM casts JOIN spells on casts.spell_id = spells.id WHERE casts.character_id= %(id)s"
        if (char1):
            results = connectToMySQL(schema).query_db(query,{"id":char1.id})
            if results !=():
                for result in results:
                    data2={
                        **result,
                        "id": result['spells.id']
                    }
                    char1.spells.append(spell.Spell(data2))
        return char1
        
    
    @classmethod
    def get_one_by_id(cls,data):
        query = "SELECT * FROM characters LEFT JOIN enemies on characters.id = enemies.character_id WHERE characters.id = %(id)s;"
        results = connectToMySQL(schema).query_db(query,data)
        char1 =  cls(results[0])
        if results[0]['enemies.id'] != None:
            for result in results:
                post_data = {
                    "id": result['enemies.id'],
                    "character_id": result['id'],
                    "power": result["power"],
                    "health": result['enemies.health'],
                    "max_health": result['max_health']
                    }
                char1.enemy= enemy.Enemy(post_data);
        return char1;


    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO characters (name,loc_y,loc_x,stamina,level,xp,dexterity,intelligence,mana,health, strength, user_id)
        VALUES (%(name)s,0,0,%(stamina)s,1,0,%(dexterity)s,%(intelligence)s,%(mana)s,%(health)s,%(strength)s,%(user_id)s); 
        """

        post_data={
            **data,
            'health': int(data['strength'])*10,
            'mana': int(data['intelligence'])*10,
            'stamina': int(data['dexterity'])*10
        }
        connectToMySQL(schema).query_db(query,post_data)
        char1 = Character.get_one_by_user_id(data)

        if spell.Spell.get_all() ==[]:
            spell.Spell.add_starters()

        query="""
        INSERT INTO casts (character_id,spell_id) VALUES (%(id)s, 1),(%(id)s,2);
        """
        
        return connectToMySQL(schema).query_db(query,{'id':char1.id})


    @classmethod
    def update_xp(cls,data):
        query ="UPDATE characters SET xp = %(xp)s WHERE id = %(id)s;"
        return connectToMySQL(schema).query_db(query,data)
    
    @classmethod
    def update_health(cls,data):
        query = "UPDATE characters SET health = %(health)s WHERE id = %(id)s;"
        return connectToMySQL(schema).query_db(query,data)