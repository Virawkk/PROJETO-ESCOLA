from .auth import auth
from .alunos import alunos
from .professores import professores

# Função para registrar os Blueprints com o app Flask
def register_routes(app):
    app.register_blueprint(auth)
    app.register_blueprint(alunos)
    app.register_blueprint(professores)