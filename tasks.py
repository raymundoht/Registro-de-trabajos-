class TaskQueue:
    def __init__(self):
        # Inicializa la cola de tareas como una lista vacia
        self.queue = []

    def enqueue(self, task):
        # Agrega una tarea al final de la cola
        self.queue.append(task)

    def dequeue(self):
        # Elimina y devuelve la tarea al frente de la cola
        return self.queue.pop(0) if self.queue else None 

    def get_all(self):
        # Devuelve todas las tareas en la cola
        return self.queue

class TaskStack:
    def __init__(self):
        # Inicializa la pila de tareas como una lista vacia
        self.stack = []

    def push(self, task):
        # Agrega una tarea
        self.stack.append(task)

    def pop(self):
        # Elimina y devuelve la tarea
        return self.stack.pop() if self.stack else None 

    def get_all(self):
        # Devuelve todas las tareas
        return self.stack