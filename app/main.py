from flask import Flask
from flask import render_template
from flask import url_for

# ---> comando para iniciar o ambiente ---> . venv/bin/activate 
# ---> comando para iniciar o projeto ---> export FLASK_APP=main 
# ---> comando para buildar o projeto ---> flask run  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/sistema/')
def sistema():
    return render_template('sistema.html')
