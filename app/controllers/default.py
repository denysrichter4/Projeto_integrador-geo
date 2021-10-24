from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/sistema/')
def sistema():
    return render_template('sistema.html')