from flask import render_template, flash
from flask_login import login_user
from app import app, db
from app.models.tables import Professores, Alunos
from app.models.forms import FormLogin

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login/', methods=["GET", "POST"])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        professor = Professores.query.filter_by(email=form.email.data).first()
        if professor and Professores.senha == form.data.senha:
            login_user(professor)
            flash("logged in")
            return render_template('sistema.html')
        else:
            flash("Invalid login")
        
    return render_template('login.html',form = form)

@app.route('/sistema/')
def sistema():
    return render_template('sistema.html')


@app.route('/cadastro/')
def cadastro():
    return render_template('cadastro.html')


#@app.route('/teste/<info>')
#@app.route('/teste/', defaults={'info':None})
#def teste(info):
    #create
    #i = Professores("João8", "joao8@gmail.com", "123456")
    #db.session.add(i)
    #db.session.commit()

    #read
    #r = Professores.query.filter_by(nome="João").first()
    #print(r.nome)
    #return f'{r.nome}'

    #update
    #r = Professores.query.filter_by(nome="João").first()
    #r.nome = "Joao01"
    #db.session.add(r)
    #db.session.commit()

    #delete
    #r = Professores.query.filter_by(nome="João").first()
    #db.session.delete(r)
    #db.session.commit()
    
    #print(r.id)
    #return f'{r.nome}'