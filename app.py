#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/dashboard/<name>')
def dashboard(name):
    return f'Welcome, {name}!' 

@app.route('/',methods = ['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        last = request.form['name_last']
        return redirect(url_for('dashboard',name = last))
    elif request.method == 'GET':
        user = request.args.get('last')
        return render_template('login.html')
    else:
        return "Illegal action"

      

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)
