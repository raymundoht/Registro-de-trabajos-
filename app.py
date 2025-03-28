from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from config import Config
from models import TaskManager

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)

task_manager = TaskManager(mysql)

@app.route('/')
def index():
    tasks = task_manager.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']
        task_manager.add_task(title, description, category)
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    new_status = request.form['category']
    task_manager.update_task_status(task_id, new_status)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
