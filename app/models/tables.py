from app import db

class Professores(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    senha = db.Column(db.String)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return "<Professor %r>" % self.nome

class Alunos(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer)
    nome = db.Column(db.String, unique=True)
    classe = db.Column(db.String)
    materia = db.Column(db.String)
    nota = db.Column(db.String)
    qtd_aulas = db.Column(db.String)
    qtd_faltas = db.Column(db.String)

    def __init__(self, numero, nome, classe, materia, nota, qtd_aulas, qtd_faltas):
        self.numero = numero
        self.nome = nome
        self.classe = classe
        self.materia = materia
        self.nota = nota
        self.qtd_aulas = qtd_aulas
        self.qtd_faltas = qtd_faltas

    def __repr__(self):
        return "<Aluno %r>" % self.nome
