class TaskManager:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_tasks(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM tasks")
        tasks = cur.fetchall()
        cur.close()
        
        # Devolver tareas como diccionarios, no como tuplas
        task_list = []
        for task in tasks:
            task_dict = {
                'id': task[0],           # Asegúrate de que el índice sea correcto según tu tabla
                'title': task[1],
                'description': task[2],
                'category': task[3]
            }
            task_list.append(task_dict)
        return task_list

    def add_task(self, title, description, category):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO tasks (title, description, category) VALUES (%s, %s, %s)", (title, description, category))
        self.mysql.connection.commit()
        cur.close()

    def delete_task(self, task_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        self.mysql.connection.commit()
        cur.close()

    def update_task_status(self, task_id, new_status):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE tasks SET category = %s WHERE id = %s", (new_status, task_id))
        self.mysql.connection.commit()
        cur.close()
