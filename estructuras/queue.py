"""
Queue (Cola) implementada con lista doblemente enlazada.

TODO:
- Implementa DoubleNode (value, prev, next)
- Implementa Queue con operaciones: enqueue, dequeue, peek, is_empty, size
- Enqueue al final (tail) y dequeue al inicio (head) para O(1)

Sugerencia:
- Mantén punteros a head y tail, más un contador.
"""

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    # TODO: implementar nodo doble

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    # TODO: implementar cola enlazada doble
    def enqueue(self, value):
        """Inserta al final. O(1)"""
        nodo = DoubleNode(value)

        if self.tail == None:
            self.head = nodo
            self.tail = nodo
            nodo.prev = None
            nodo.next = None
        else:
            self.tail.next = nodo
            nodo.next = None
            nodo.prev = self.tail
            self.tail = nodo
        self.count = self.count + 1

    def dequeue(self):
        """Extrae el primero. O(1). Debe lanzar IndexError si está vacía."""
        if self.head == None:
            raise IndexError("dequeue from empty queue")
        else:
            valor = self.head.value
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            self.count = self.count - 1
            return valor

    def peek(self):
        """Retorna el primero sin extraer. O(1). IndexError si vacía."""
        return self.head.value

    def is_empty(self):
        """True si la cola está vacía. O(1)"""
        return self.count == 0

    def size(self):
        """Cantidad de elementos. O(1)"""
        return self.count
