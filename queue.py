class Queue:
    def __init__(self):
        # Inicializa la cola como una lista vacia
        self.items = []

    def is_empty(self):
        # Verifica si la cola esta vacia
        return len(self.items) == 0

    def enqueue(self, item):
        # Agrega un elemento al final de la cola
        self.items.insert(0, item)

    def dequeue(self):
        # Elimina y devuelve el elemento al frente de la cola
        if not self.is_empty():
            return self.items.pop()  # Elimina el ultimo elemento de la lista
        raise IndexError("dequeue from empty queue")  # Lanza un error si la cola esta vacia

    def size(self):
        # Devuelve el tamaño actual de la cola
        return len(self.items)

    def peek(self):
        # Devuelve el elemento al frente de la cola sin eliminarlo
        if not self.is_empty():
            return self.items[-1]  # Devuelve el ultimo elemento de la lista (frente de la cola)
        raise IndexError("peek from empty queue")  # Lanza un error si la cola esta vacia