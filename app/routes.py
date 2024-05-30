from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Task
from datetime import datetime

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    start_time = datetime.strptime(request.form.get('start_time'), '%Y-%m-%d %H:%M:%S')
    end_time = request.form.get('end_time', None)
    if end_time:
        end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    new_task = Task(title=title, start_time=start_time, end_time=end_time)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get(task_id)
    task.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))
