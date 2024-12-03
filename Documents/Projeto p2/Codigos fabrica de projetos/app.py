from flask import Flask, request, render_template, redirect, url_for
from flask_migrate import Migrate
from config import Config
from models import db, Aluno
from routes import auth, alunos, professores
from utils import login_required  # Importa o decorador de login

# Criação da instância do Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicialização do banco de dados
db.init_app(app)

# Configuração do Flask-Migrate
migrate = Migrate(app, db)

# Registro das Blueprints
app.register_blueprint(auth)
app.register_blueprint(alunos)
app.register_blueprint(professores)

@app.route('/')
def pagina_inicial():
    return render_template('pagina_inicial.html')

@app.route('/cadastro-escola')
def cadastro_escola():
    return render_template('cadastro-escola.html')

@app.route('/salvar-escola', methods=['POST'])
def salvar_escola():
    # Pega os dados do formulário
    nome_escola = request.form['nome_escola']
    nome_diretor = request.form['nome_diretor']
    nome_coordenador = request.form['nome_coordenador']
    endereco = request.form['endereco']
    senha = request.form['senha']
    
    # Aqui você pode salvar esses dados no banco de dados ou realizar outra ação

    return redirect(url_for('login_escola'))

@app.route('/login_escola')
def login_escola():
    return render_template('login_escola.html')

@app.route('/area-cadastro')
def area_cadastro():
    return render_template('area-cadastro.html')

# Rota protegida como exemplo
@app.route('/alunos_cadastrados')
@login_required  # Aplica o decorador de autenticação
def alunos_cadastrados():
    alunos = Aluno.query.all()
    return render_template('alunos-cadastrados.html', alunos=alunos)

# Inicializa o banco de dados e executa a aplicação
if __name__ == '__main__':
    app.run(debug=True)
