"""
Reto 2: Simulador de atención usando Queue (FIFO).

Clase a implementar:
    class QueueManager:
        - add_person(nombre: str, tiempo: int) -> None
        - serve_person() -> tuple[str, int]   # (nombre, tiempo)
        - state() -> list[str]                # nombres en orden FIFO

Reglas:
- 'agregar_persona' encola al final.
- 'atender_persona' desencola y retorna la tupla; si está vacía, lanza IndexError.
- 'estado' retorna los nombres en el orden actual sin mutar la cola.

Tips:
- Usa Queue de estructuras/queue.py
"""

from estructuras.queue import Queue

class QueueManager:
    # TODO: implementar usando Queue internamente.
    def __init__(self):
        self.cola = Queue()

    def add_person(self, nombre: str, tiempo: int) -> None:
        self.cola.enqueue( (nombre, tiempo) )

    def serve_person(self) -> tuple[str, int]:
        return self.cola.dequeue()

    def state(self) -> list[str]:
        resultado = []
        nodo_actual = self.cola.head
        while nodo_actual is not None:
            nombre, _ = nodo_actual.value
            resultado.append(nombre)
            nodo_actual = nodo_actual.next
        return resultado
