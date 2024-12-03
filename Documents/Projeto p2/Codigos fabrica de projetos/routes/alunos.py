from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Aluno
from utils import login_required

# Definição do Blueprint para alunos
alunos_bp = Blueprint('alunos', __name__, url_prefix='/alunos')

# Rota para listar alunos cadastrados
@alunos_bp.route('/cadastrados', methods=['GET'])
@login_required
def listar_alunos():
    alunos = Aluno.query.all()
    return render_template('alunos_cadastrados.html', alunos=alunos)

# Rota para cadastrar um novo aluno
@alunos_bp.route('/cadastro', methods=['GET', 'POST'])
@login_required
def cadastrar_aluno():
    if request.method == 'POST':
        nome = request.form.get('nome')
        foto_url = request.form.get('foto_url')

        # Validação de dados obrigatórios
        if not nome:
            flash('O nome do aluno é obrigatório.', 'error')
            return redirect(url_for('alunos.cadastrar_aluno'))

        novo_aluno = Aluno(nome=nome, foto_url=foto_url)
        db.session.add(novo_aluno)
        db.session.commit()
        flash('Aluno cadastrado com sucesso!', 'success')
        return redirect(url_for('alunos.listar_alunos'))
    
    return render_template('cadastro_aluno.html')

# Rota para editar um aluno existente
@alunos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_aluno(id):
    aluno = Aluno.query.get_or_404(id)

    if request.method == 'POST':
        aluno.nome = request.form.get('nome')
        aluno.foto_url = request.form.get('foto_url')

        # Validação de dados obrigatórios
        if not aluno.nome:
            flash('O nome do aluno é obrigatório.', 'error')
            return redirect(url_for('alunos.editar_aluno', id=id))

        db.session.commit()
        flash('Aluno atualizado com sucesso!', 'success')
        return redirect(url_for('alunos.listar_alunos'))
    
    return render_template('editar_aluno.html', aluno=aluno)

# Rota para excluir um aluno
@alunos_bp.route('/excluir/<int:id>', methods=['POST'])
@login_required
def excluir_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    flash('Aluno excluído com sucesso!', 'success')
    return redirect(url_for('alunos.listar_alunos'))

# Rota para visualizar os detalhes de um aluno
@alunos_bp.route('/detalhes/<int:id>', methods=['GET'])
@login_required
def detalhes_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    return render_template('detalhes_aluno.html', aluno=aluno)
