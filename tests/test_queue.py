import unittest
from retos.reto2_queue import QueueManager

class TestChallenge2Queue(unittest.TestCase):
    def test_serve_in_fifo_order(self):
        gestor = QueueManager()
        gestor.add_person("Ana", 5)
        gestor.add_person("Luis", 3)

        nombre, tiempo = gestor.serve_person()
        self.assertEqual(nombre, "Ana")
        self.assertEqual(tiempo, 5)

    def test_serve_empty_queue_raises(self):
        gestor = QueueManager()
        with self.assertRaises(IndexError):
            gestor.serve_person()

    def test_queue_state(self):
        gestor = QueueManager()
        gestor.add_person("Carlos", 4)
        gestor.add_person("Marta", 2)
        estado = gestor.state()
        self.assertEqual(estado, ["Carlos", "Marta"])

    def test_multiple_adds_and_serves(self):
        gestor = QueueManager()
        gestor.add_person("Pedro", 6)
        gestor.add_person("Sofia", 1)
        gestor.add_person("Jorge", 3)

        nombre, tiempo = gestor.serve_person()
        self.assertEqual(nombre, "Pedro")
        self.assertEqual(tiempo, 6)

        gestor.add_person("Lucia", 2)
        estado = gestor.state()
        self.assertEqual(estado, ["Sofia", "Jorge", "Lucia"])


    # TODO: agrega más casos:
    # - atender_persona en cola vacía -> IndexError
    # - estado() refleja el orden actual
    # - mezcla de agregar/atender repetidas veces

if __name__ == "__main__":
    unittest.main()
