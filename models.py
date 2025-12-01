from utils import db
class Usuario(db.Model):
	__tablename__= "usuario"
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(100))
	email = db.Column(db.String(100))
	senha = db.Column(db.String(100))
	
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __repr__(self):
        return "<Usuario {}>".format(self.nome)

class Tarefa(db.Model):
        id = db.Column(db.Integer, primary_key= True)
        descricao = db.Column(db.string(200), unique=True, nullable=False)