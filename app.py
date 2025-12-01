from flask import Flask, render_template, request , url_for, redirect
from utils import db
import os 
from models import Usuario
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_usuario = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_mydb = os.getenv('DB_DATABASE')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

conexao = f"mysql+pymysql://{db_usuario}:{db_password}@{db_host}:{db_port}/{db_mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def index():
    return 'PSI COM ALBA'

@app.route('/contato')
def contato():
    x="Maria"
    y="maria@email.com"
    return  render_template('contato.html', nome=x, email=y)

@app.route('/exemplo')
def exemplo():
    return render_template('teste1.html')

@app.route('/exemplo2')
def exemplo2():
    return render_template('teste2.html')

@app.route('/perfil',defaults ={'usuario':'fulano'})
@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario= usuario)

@app.route('/semestre/<int:x>')
def semestre(x):
    y = x+1
    return render_template('semestre.html', x=x, y=y)

@app.route('/somar/<int:n1>/<int:n2>')
def somar(n1, n2):
		resultado = n1 + n2
		return str(resultado)
        
@app.route('/dados')
def dados():
    return render_template("dados.html")

@app.route('/recebedados',methods= ['POST'])
def recebedados():
    # nome = request.args['nome']
    # telefone = request.args['telefone']
    nome = request.form['nome']
    telefone = request.form['telefone']
    estado = request.form['estado']
    escolaridade = request.form['formacao']
    return f'{nome}-{telefone}-{estado}-{escolaridade}'


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():
	login = request.form["login"]
	senha = request.form["senha"]
	if login == "admin" and senha == "12345":
		return 'Seja Bem-vindo Admin!'
	else:
		return 'Você não tem permissão para acessar essa página'

@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
    return render_template('verificaridade.html', idade=idade)

@app.route('/usuario/<nome>')
def usuario(nome):
	return render_template('usuario.html', nome=nome)

@app.route('/produtos/<int:qtd>')
def produtos(qtd):
    return render_template('produtos.html',qtd=qtd)

@app.route('/compras')
def compras():
    # itens = ['Arroz', 'Feijão', 'Carne', 'Peixe', 'Frango']
    itens = request.form.getlist("item")
    return render_template ("compras.html", itens=itens)
    
@app.route('/tarefa')
def tarefas():
    tarefas = Tarefa.query.all()
    return render_template("tarefa.html", tarefas=tarefas)

@app.route('/create', methods=['POST'])
def create_tarefa():
    descricao = request.form['descricao']
    new_tarefa = Tarefa(descricao=descricao)
    db.Session.add(new_tarefa)
    db.Session.Commit()
    return redirect(url_for('tarefa.html'))

@app.route('/update/<int:tarefa_id>', methods['POST'])
def update_tarefa(tarefa_id):
    tarefa_obj = Tarefa.query.get(tarefa_id)
    if tarefa_obj:
        tarefa_obj.descricao = request.form['descricao']
        db.Session.Commit()
    return redirect(url_for('tarefa.html'))

@app.route("/delete/<int:tarefa_id>", methods=['POST'])
def delete_tarefa(tarefa_id):
    tarefa_obj = Tarefa.query.get(tarefa_id)
    if tarefa_obj:
        db.Session.delete(tarefa_obj)
        db.Session.Commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()