from flask_app import app 
from flask import render_template,redirect,request,flash,session
from flask_app.models import user, character




@app.route("/")
def login():
    if 'uuid' in session:
        return redirect('/success')
    else:
        return render_template('login.html')


@app.route("/register", methods=['POST'])
def register():
    if not user.User.validate_user(request.form):
        print("not valid")
        return redirect("/")
    
    session['uuid']=user.User.create(request.form)
    return redirect("/success")
    
    


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login', methods=['POST'])
def logUser():
    if user.User.check_cred(request.form):
        session['uuid']= user.User.logUser(request.form)
        return redirect("/success")
    else:
        flash("Login failed")
        return redirect("/")