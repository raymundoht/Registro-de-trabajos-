class Node:
    def __init__(self, key):
        # Inicializa un nodo con un valor key
        self.left = None  # izquierdo
        self.right = None  #derecho
        self.value = key  # nodo

class BinaryTree:
    def __init__(self):
        # Inicializa un arbol binario sin raíz
        self.root = None  # Raiz del árbol

    def insert(self, key):
        # Inserta un nuevo nodo
        if self.root is None:
            self.root = Node(key)
        else:
            # Si el arbol no está vacío, llama a la funcion recursiva para insertar
            self._insert_rec(self.root, key)

    def _insert_rec(self, current_node, key):
        # Funcion recursiva para insertar un nuevo nodo en el arbol
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_rec(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_rec(current_node.right, key)

    def inorder_traversal(self, node):
        # recorrido en orden del arbol y devuelve una lista de valores
        return self.inorder_traversal(node.left) + [node.value] + self.inorder_traversal(node.right) if node else []