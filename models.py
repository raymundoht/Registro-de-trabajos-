from binary_tree import BinaryTree
from stack import Stack
from queue import Queue

class TaskManager:
    def __init__(self, mysql):
        # Inicia el gestor de tareas con la conexion a la base de datos
        self.task_tree = BinaryTree() 
        self.task_stack = Stack()
        self.task_queue = Queue()

    def get_all_tasks(self):
        # Obtiene todas las tareas de la base de datos
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM tasks")
        tasks = cur.fetchall()
        cur.close()
        
        # Lista para almacenar las tareas en forma de diccionario
        task_list = []
        for task in tasks:
            # Crea un diccionario para cada tarea
            task_dict = {
                'id': task[0],               
                'title': task[1],             
                'description': task[2],       
                'category': task[3]
            }
            # Agrega el diccionario a la lista
            task_list.append(task_dict)
        return task_list

    def add_task(self, title, description, category):
        # Agrega una nueva tarea a la base de datos y ejecutar consultas
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO tasks (title, description, category) VALUES (%s, %s, %s)", (title, description, category))
        self.mysql.connection.commit()  
        cur.close()                          
        self.task_tree.insert(title)          
        self.task_stack.push(title)        
        self.task_queue.enqueue(title)         

    def delete_task(self, task_id):
        # Elimina una tarea de la base de datos segun su ID
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        # Confirma los cambios en la base de datos
        self.mysql.connection.commit()
        cur.close()

    def update_task_status(self, task_id, new_status):
        # Actualiza las tarea en la base de datos
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE tasks SET category = %s WHERE id = %s", (new_status, task_id))
        # Confirma los cambios en la base de datos
        self.mysql.connection.commit()
        cur.close()