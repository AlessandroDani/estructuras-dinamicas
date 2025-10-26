"""
Stack (Pila) implementado con lista enlazada simple.

TODO:
- Implementa Node (valor, next)
- Implementa Stack con operaciones: push, pop, peek, is_empty, size
- Garantiza que push y pop sean O(1)

Sugerencia:
- Mantén referencia a la "cabeza" (top) y un contador de tamaño.
"""

class Node:
    # TODO: implementar nodo simple
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    # TODO: implementar pila enlazada
    def push(self, value):
        """Inserta en el tope. O(1)"""
        nodo = Node(value)
        if self.top is None:
            self.top = nodo
        else:
            nodo.next = self.top
            self.top = nodo
        self.count = self.count + 1

    def pop(self):
        """Extrae y retorna el tope. O(1). Debe lanzar IndexError si está vacía."""
        if self.top is None:
            raise IndexError("pop from empty stack")
        valor = self.top.value
        self.top = self.top.next
        self.count = self.count - 1
        return valor

    def peek(self):
        """Retorna el tope sin extraer. O(1). IndexError si vacía."""
        return self.top.value

    def is_empty(self):
        """True si la pila está vacía. O(1)"""
        return self.count == 0

    def size(self):
        """Cantidad de elementos. O(1)"""
        return self.count
