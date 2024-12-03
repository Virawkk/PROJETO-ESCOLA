from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Professor
from utils import login_required

# Definição do Blueprint para professores
professores_bp = Blueprint('professores', __name__, url_prefix='/professores')

# Rota para listar professores cadastrados
@professores_bp.route('/cadastrados', methods=['GET'])
@login_required
def listar_professores():
    professores = Professor.query.all()
    return render_template('professores_cadastrados.html', professores=professores)

# Rota para cadastrar um novo professor
@professores_bp.route('/cadastro', methods=['GET', 'POST'])
@login_required
def cadastrar_professor():
    if request.method == 'POST':
        nome = request.form.get('nome')
        foto_url = request.form.get('foto_url')
        materia = request.form.get('materia')

        # Validação de dados obrigatórios
        if not nome:
            flash('O nome do professor é obrigatório.', 'error')
            return redirect(url_for('professores.cadastrar_professor'))

        novo_professor = Professor(nome=nome, foto_url=foto_url, materia=materia)
        db.session.add(novo_professor)
        db.session.commit()
        flash('Professor cadastrado com sucesso!', 'success')
        return redirect(url_for('professores.listar_professores'))
    
    return render_template('cadastro_professor.html')

# Rota para editar um professor existente
@professores_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_professor(id):
    professor = Professor.query.get_or_404(id)

    if request.method == 'POST':
        professor.nome = request.form.get('nome')
        professor.foto_url = request.form.get('foto_url')
        professor.materia = request.form.get('materia')

        # Validação de dados obrigatórios
        if not professor.nome:
            flash('O nome do professor é obrigatório.', 'error')
            return redirect(url_for('professores.editar_professor', id=id))

        db.session.commit()
        flash('Professor atualizado com sucesso!', 'success')
        return redirect(url_for('professores.listar_professores'))
    
    return render_template('editar_professor.html', professor=professor)

# Rota para excluir um professor
@professores_bp.route('/excluir/<int:id>', methods=['POST'])
@login_required
def excluir_professor(id):
    professor = Professor.query.get_or_404(id)
    db.session.delete(professor)
    db.session.commit()
    flash('Professor excluído com sucesso!', 'success')
    return redirect(url_for('professores.listar_professores'))

# Rota para visualizar os detalhes de um professor
@professores_bp.route('/detalhes/<int:id>', methods=['GET'])
@login_required
def detalhes_professor(id):
    professor = Professor.query.get_or_404(id)
    return render_template('detalhes_professor.html', professor=professor)
