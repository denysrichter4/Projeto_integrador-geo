from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/sistema/')
def sistema():
    return render_template('sistema.html')
