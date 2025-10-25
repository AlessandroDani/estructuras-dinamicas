import unittest
from retos.reto3_linkedlist import add_task, find_by_id, find_by_priority, iter_forward, remove_by_id

class TestChallenge3LinkedList(unittest.TestCase):
    def test_add_and_find_by_id(self):
        add_task(1, "Probar DLL", 2)
        tarea = find_by_id(1)
        self.assertIsNotNone(tarea)
        self.assertEqual(tarea["id"], 1)
        self.assertEqual(tarea["descripcion"], "Probar DLL")
        self.assertEqual(tarea["prioridad"], 2)

    def test_remove_by_id(self):
        add_task(10, "Tarea a eliminar", 2)
        tarea = find_by_id(10)
        self.assertIsNotNone(tarea)
        remove_by_id(10)
        tarea = find_by_id(10)
        self.assertIsNone(tarea)
        self.assertIsNone(find_by_id(-2))
        

    def test_find_by_priority(self):
        add_task(2, "Tarea baja", 5)
        add_task(3, "Tarea media", 3)
        add_task(4, "Tarea alta", 2)
        add_task(5, "Otra tarea media", 3)
        tareas = find_by_priority(3)
        self.assertIsNotNone(tareas)
        for tarea in tareas:
            self.assertEqual(tarea["prioridad"], 3)


    def test_find_by_id_exist(self):
        tarea = find_by_id(-3)
        self.assertIsNone(tarea)

    def test_iterator_forward(self):
        add_task(1, "A", 2)
        add_task(2, "B", 2)
        add_task(3, "C", 2)
        add_task(4, "D", 2)
        for tarea in iter_forward():
            print(tarea.descripcion)
        
    # TODO: agrega más casos:
    # - eliminar por id (cuando implementes remove)
    # - find_by_priority devuelve múltiples tareas
    # - find_by_id inexistente -> None

if __name__ == "__main__":
    unittest.main()
