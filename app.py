#!/usr/bin/env python3
import logging
import flask as f 

from db import AttendanceWizard

#Create the flask app
app = f.Flask(__name__)
app.secret_key = "asdf1234"

@app.route('/dashboard/success')
def dashboard():
    login_info = f.session['login_info']
    secret = login_info['secret']
    id_number = login_info['id_number']
    a = AttendanceWizard()
    a.prepAndAddStatement(id_number,secret)

    return f'Welcome, {id_number}, the secret word you submitted was {secret}!' 

@app.route('/',methods = ['POST', 'GET'])
def home():
    return f.render_template('home.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if f.request.method == 'POST':
        app.logger.info("POST request hit")
        app.logger.info(f.request.form)
        #Save me some typing
        d = f.request.form
        f.session['login_info'] = d
        return f.redirect(f.url_for('dashboard' ))
    elif f.request.method == 'GET':
        app.logger.info("GET request hit")
        user = f.request.args.get('last')
        return f.render_template('login.html')
    else:
        return "Illegal action"

      

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)
