from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Task

@app.route('/')
def index():
    with app.app_context():
        tasks = Task.query.all()  # Ejemplo de consulta a la base de datos dentro de una ruta
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    task = Task.query.get(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))
