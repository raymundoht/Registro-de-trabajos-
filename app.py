from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from config import Config
from models import TaskManager

# Inicializa la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)

# Crea una instancia
task_manager = TaskManager(mysql)

# Ruta principal que muestra todas las tareas
@app.route('/')
def index():
    tasks = task_manager.get_all_tasks()
    return render_template('index.html', tasks=tasks, task_manager=task_manager)

# Ruta para agregar una nueva tarea
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        # Obtiene los datos del formulario
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']
        # Agrega la nueva tarea
        task_manager.add_task(title, description, category)
        return redirect(url_for('index'))
    return render_template('add_task.html')

# Ruta para eliminar una tarea
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return redirect(url_for('index'))

# Ruta para actualizar el estado de una tarea
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    new_status = request.form['category']
    task_manager.update_task_status(task_id, new_status)
    return redirect(url_for('index'))

# Ejecuta la aplicación en modo de depuración
if __name__ == '__main__':
    app.run(debug=True)