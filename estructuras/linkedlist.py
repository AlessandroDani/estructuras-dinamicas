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
        self.tail = None
        self.contador = 0

    # TODO: implementar DLL
    def append(self, task):
        """Inserta al final. O(1)"""
        nodo = DoubleNode(task["id"], task["descripcion"], task["prioridad"])
        if self.tail is None:
           self.head = nodo
           self.tail = nodo
           nodo.prev = None
           nodo.next = None
        else:
            self.tail.next = nodo
            nodo.next = None
            nodo.prev = self.tail
            self.tail = nodo
        self.contador = self.contador + 1

    def prepend(self, task):
        """Inserta al inicio. O(1)"""
        nodo = DoubleNode(task["id"], task["descripcion"], task["prioridad"])
        if self.head is None:
           self.head = nodo
           self.tail = nodo
           nodo.prev = None
           nodo.next = None
        else:
            nodo.next = self.head
            nodo.prev = None
            self.head.prev = nodo
            self.head = nodo
        self.contador = self.contador + 1

    def remove_by_id(self, task_id):
        """Elimina por id. O(n). Retorna True si elimina, False si no."""
        nodo = self.head
        while nodo is not None:
            if nodo.id != task_id:
                nodo = nodo.next
            else:
                if nodo.prev is not None and nodo.next is not None:  
                    nodo.prev.next = nodo.next
                    nodo.next.prev = nodo.prev
                else:
                    if nodo.prev is None:
                        self.head = nodo.next
                        if self.head is not None:
                            self.head.prev = None
                    if nodo.next is None:
                        self.tail = nodo.prev
                        if self.tail is not None:
                            self.tail.next = None
                self.contador = self.contador - 1
                return True
        return False

    def find_by_id(self, task_id):
        """Retorna la tarea o None. O(n)"""
        nodo = self.head
        while nodo is not None:
            if nodo.id != task_id:
                nodo = nodo.next
            else:
                return {"id": nodo.id, "descripcion": nodo.descripcion, "prioridad": nodo.prioridad}
        return None

    def find_by_prioridad(self, prioridad):
        """Retorna lista de tareas con esa prioridad. O(n)"""
        list = []
        nodo = self.head
        while self.head != None:
            if nodo == None:
               return [{"id": n.id, "descripcion": n.descripcion, "prioridad": n.prioridad}for n in list]
            if nodo.prioridad == prioridad:
                list.append(nodo)
            nodo = nodo.next
        return None
    
    def iter_forward(self):
        """Generador hacia adelante."""
        if self.head is None:
            return
        else:   
            nodo = self.head
            while True:
                yield nodo
                nodo = nodo.next
                if nodo == None:
                    break

    def iter_backward(self):
        """Generador hacia atrás."""
        if self.tail is None:
            return
        else:   
            nodo = self.tail
            while True:
                yield nodo
                nodo = nodo.prev
                if nodo == None:
                    break
    def size(self):
        """Cantidad de nodos. O(1)"""
        return self.contador
