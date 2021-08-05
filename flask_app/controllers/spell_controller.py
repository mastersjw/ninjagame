from flask_app import app 
from flask import render_template,redirect,request,flash,session
from flask_app.models import user, character, world, spell,enemy




@app.route('/damage', methods=['POST'])
def do_dmg():
    sp = spell.Spell.get_one_by_name(request.form)
    char1 = character.Character.get_one_by_user_id({'user_id':session['uuid']})
    if char1.enemy =={}:
        flash("No Enemies")
        return redirect("/game")
    if sp.type=="magic":
        damage = sp.power * char1.intelligence
    else:
        print("THIS IS WHERE WE HIT WITH PUNCH")
        damage = sp.power* char1.strength
        print("We HIT FOR ",damage)
    
    newEhealth = char1.enemy.health - damage;
    if newEhealth <=0:
        enemy.Enemy.delEnemy({'id': char1.enemy.id})
        character.Character.update_xp({'id':char1.id, 'xp': (char1.xp+1)})
    else:
        enemy.Enemy.update_health({'id': char1.enemy.id, 'health': newEhealth})
    # update character (char can just take some standard dmg for now) also increase xp
    character.Character.update_health({'id': char1.id, 'health': (char1.health-1)})  
    return redirect("/game");