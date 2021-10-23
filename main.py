from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/index/')
@app.route('/index/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
