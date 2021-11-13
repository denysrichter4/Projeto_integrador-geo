from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app import app, db, login_manager
from app.models.tables import User, Alunos
from app.models.forms import FormLogin, FormCadastro, FormCadastroAluno, FormAtualizaAluno, FormConsultaAluno
from sqlalchemy import asc, and_

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=["GET", "POST"])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.senha == form.senha.data:
            login_user(user)
            flash("logged in")
            return redirect(url_for("sistema"))
        else:
            flash("Invalid login")
    return render_template('login.html', form = form)   
    
@app.route('/sistema/<info>')
@app.route('/sistema/', defaults={'info':None}, methods=["GET", "POST"])
def sistema(info): 
    if current_user.is_anonymous == True:
        return render_template('index.html')
    else:
        alunos = Alunos.query.filter_by(professor_id=current_user.id).order_by(asc(Alunos.numero))
        return render_template('sistema.html', alunos = alunos)
    return render_template('sistema.html')

@app.route('/consulta/<info>')
@app.route('/consulta/', defaults={'info':None}, methods=["GET", "POST"])
def consulta(info):
    if current_user.is_anonymous == True:
        return render_template('index.html')
    else: 
        form = FormAtualizaAluno()
        if form.validate_on_submit():
            alunos = Alunos.query.filter_by(professor_id=current_user.id).order_by(asc(Alunos.numero))
            form2 = FormConsultaAluno()
            for aluno in alunos:
                if(form2.numero.data != ""):
                    alunosNumero = Alunos.query.filter(and_(Alunos.professor_id == current_user.id, Alunos.numero == form2.numero.data)).all()
                    return render_template('consulta.html', alunos = alunosNumero, form = form2)
                elif(aluno.nome != ""):
                    alunosNome = Alunos.query.filter(and_(Alunos.professor_id == current_user.id, Alunos.nome == form2.nome.data)).all()
                    return render_template('consulta.html', alunos = alunosNome, form = form2)
    return render_template('consulta.html', form = form)

@app.route('/delete/<int:aluno_id>', methods=["GET", "POST"])
def delete(aluno_id):
    if current_user.is_anonymous == True:
        return render_template('index.html')
    else:
        aluno_d = Alunos.query.filter_by(id=aluno_id).first()
        db.session.delete(aluno_d)
        db.session.commit()
        return redirect(url_for("sistema", aluno_id = aluno_id))

@app.route('/update/<info>')
@app.route('/update/<int:aluno_id>', defaults={'info':None}, methods=["GET", "POST"])
def update(aluno_id, info):
    if current_user.is_anonymous == True:
        return render_template('index.html')
    else:
        form = FormCadastroAluno()
        aluno_e = Alunos.query.filter_by(id=aluno_id).first()

        form.numero.data = aluno_e.numero 
        form.nome.data = aluno_e.nome 
        form.classe.data = aluno_e.classe 
        form.materia.data = aluno_e.materia 
        form.nota.data = aluno_e.nota 
        form.aulas.data = aluno_e.qtd_aulas 
        form.faltas.data = aluno_e.qtd_faltas 
        
        if form.validate_on_submit():
            form2 = FormAtualizaAluno()
            aluno_e.numero = str(form2.numero.data)
            aluno_e.nome = str(form2.nome.data)
            aluno_e.classe = str(form2.classe.data)
            aluno_e.materia = str(form2.materia.data)
            aluno_e.nota = str(form2.nota.data ) 
            aluno_e.qtd_aulas = str(form2.aulas.data)
            aluno_e.qtd_faltas = str(form2.faltas.data)
            db.session.add(aluno_e)
            db.session.commit()
            return redirect(url_for("sistema", form = form2))
        return render_template('cadastro_aluno.html', form = form)  

@app.route('/cadastro/<info>')
@app.route('/cadastro/', defaults={'info':None}, methods=["GET", "POST"])
def cadastro(info):
    form = FormCadastro()
    if form.validate_on_submit():
        if form.senha.data == form.confirmar_senha.data:
            i = User(form.nome.data, form.email.data, form.senha.data)
            db.session.add(i)
            db.session.commit()
            return redirect(url_for("login", form = form))
        else:
            flash("Insira a mesma senha nos dois campos")
    return render_template('cadastro.html', form = form)


@app.route('/cadastro_aluno/<info>')
@app.route('/cadastro_aluno/', defaults={'info':None}, methods=["GET", "POST"])
def cadastro_aluno(info):
    if current_user.is_anonymous == True:
        return render_template('index.html')
    else:
        form = FormCadastroAluno()
        if form.validate_on_submit():
            i = Alunos(form.numero.data, form.nome.data, form.classe.data, current_user.id , form.materia.data, form.nota.data, form.aulas.data, form.faltas.data)
            db.session.add(i)
            db.session.commit()
            form.numero.data = "" 
            form.nome.data = "" 
            form.classe.data = "" 
            form.materia.data = ""  
            form.nota.data = ""  
            form.aulas.data = ""  
            form.faltas.data = ""  
        return render_template('cadastro_aluno.html', form = form)


@app.route('/logout/')
def logout():
    logout_user()
    flash("logout")
    return render_template('index.html')