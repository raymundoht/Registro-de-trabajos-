class Stack:
    def __init__(self):
        # Inicializa la pila como una lista vacia
        self.items = []

    def is_empty(self):
        # Verifica si la pila esta vacia
        return len(self.items) == 0

    def push(self, item):
        # Agrega un elemento a la parte superior de la pila
        self.items.append(item)

    def pop(self):
        # Elimina y devuelve el elemento en la parte superior de la pila
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        # Devuelve el elemento en la parte superior de la pila sin eliminarlo
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        # Devuelve el tamaño actual de la pila
        return len(self.items)