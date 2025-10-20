"""
Lista doblemente enlazada (DLL) para gestionar tareas.

TODO:
- Implementa DoubleNode (id, descripcion, prioridad, prev, next)
- Implementa DoublyLinkedList con: append, prepend, remove_by_id, find_by_id, find_by_prioridad, iter_forward, iter_backward, size
- Mantén head, tail y contador para O(1) en inserciones a extremos.

Nota:
- 'find' será O(n) lineal.
"""
class DoubleNode:
    # TODO: implementar nodo doble para tareas
    def __init__(self,id,descripcion,prioridad):
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.contador = 0

    # TODO: implementar DLL
    def append(self, task):
        """Inserta al final. O(1)"""
        nodo = DoubleNode(task.id, task.descripcion, task.prioridad)
        if contador == 0:
            head = nodo
        else:
            head.prev = nodo
            nodo.next = head
        
        contador = contador + 1

    def prepend(self, task):
        """Inserta al inicio. O(1)"""
        nodo = DoubleNode(task.id, task.descripcion, task.prioridad)
        if contador == 0:
            head = nodo
        else:
            temp = head
            head = nodo
            head.prev = temp.prev
            head.next = temp

        contador = contador + 1

    def remove_by_id(self, task_id):
        """Elimina por id. O(n). Retorna True si elimina, False si no."""
        nodo = self.head.next
        while(self.head.id != nodo.id):
            if nodo.id == task_id:
                nodo.prev.next = nodo.next
                nodo.next.prev = nodo.prev
                contador = contador - 1
                return True
            nodo = nodo.next
        return False
    

    def find_by_id(self, task_id):
        """Retorna la tarea o None. O(n)"""
        nodo = self.head
        
        raise NotImplementedError

    def find_by_prioridad(self, prioridad):
        """Retorna lista de tareas con esa prioridad. O(n)"""
        raise NotImplementedError

    def iter_forward(self):
        """Generador hacia adelante."""
        raise NotImplementedError

    def iter_backward(self):
        """Generador hacia atrás."""
        raise NotImplementedError

    def size(self):
        """Cantidad de nodos. O(1)"""
        raise NotImplementedError
