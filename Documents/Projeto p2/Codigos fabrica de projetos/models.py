from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Escola(db.Model):
    __tablename__ = 'escolas'
    id = db.Column(db.Integer, primary_key=True)
    nome_escola = db.Column(db.String(150), nullable=False)
    nome_diretor = db.Column(db.String(150), nullable=False)
    nome_coordenador = db.Column(db.String(150), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Escola {self.id}: {self.nome_escola}>'

class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    foto_url = db.Column(db.String(200), nullable=True)
    disciplina = db.Column(db.String(100), nullable=True)
    id_escola = db.Column(db.Integer, db.ForeignKey('escolas.id'), nullable=False)
    escola = db.relationship('Escola', backref='professores')

    def __repr__(self):
        return f'<Professor {self.id}: {self.nome}>'

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    foto_url = db.Column(db.String(200), nullable=True)
    id_escola = db.Column(db.Integer, db.ForeignKey('escolas.id'), nullable=False)
    escola = db.relationship('Escola', backref='alunos')

    def __repr__(self):
        return f'<Aluno {self.id}: {self.nome}>'
    
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.id}: {self.nome}>'


class Matricula(db.Model):
    __tablename__ = 'matriculas'
    id = db.Column(db.Integer, primary_key=True)
    id_aluno = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    id_professor = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    id_escola = db.Column(db.Integer, db.ForeignKey('escolas.id'), nullable=False)
    data_matricula = db.Column(db.Date, nullable=False)
    nota = db.Column(db.Float, nullable=True)  # Adicionado campo para nota

    aluno = db.relationship('Aluno', backref='matriculas')
    professor = db.relationship('Professor', backref='matriculas')
    escola = db.relationship('Escola', backref='matriculas')

    def __repr__(self):
        return f'<Matricula {self.id}: Aluno {self.id_aluno} - Professor {self.id_professor}>'
