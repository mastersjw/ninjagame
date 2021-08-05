from flask_app import app 
from flask import render_template,redirect,request,flash,session
from flask_app.models import user, character, world









@app.route('/success')
def display():
    char_exist = character.Character.get_one_by_user_id({'user_id': session['uuid']})
    
    
    if 'uuid' in session and  char_exist == False:
    
        return render_template('createChar.html')
    elif 'uuid' in session and char_exist: 
        return redirect("/game")
    
@app.route('/game')
def playGame():
    char1 = character.Character.get_one_by_user_id({'user_id': session['uuid']})
    world1 = world.World()
    
    location = world1.w[char1.loc_x][char1.loc_y]
    print(location)
    if location == 0:
        loc ="meadow"
    elif location ==1:
        loc="mountain"
    else: loc="forest"
    return render_template("game.html", character = char1 ,loc= loc)

@app.route('/create', methods =['POST'])
def create():
    character.Character.create(request.form);
    return redirect('/game')

@app.route('/move',methods=['POST'])
def move():
    character.Character.move_char(request.form)
    return redirect ('/game')

@app.route('/sleep')
def sleep():
    char1 = character.Character.get_one_by_user_id({'user_id': session['uuid']})
    recovered_health = char1.health+5;
    if recovered_health > (char1.strength*10):
        recovered_health= char1.strength*10
    character.Character.update_health({'id':char1.id, 'health': recovered_health})
    return redirect("/")
