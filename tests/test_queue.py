# import unittest
# from retos.reto2_queue import QueueManager

# class TestChallenge2Queue(unittest.TestCase):
#     def test_serve_in_fifo_order(self):
#         gestor = QueueManager()
#         gestor.add_person("Ana", 5)
#         gestor.add_person("Luis", 3)

#         nombre, tiempo = gestor.serve_person()
#         self.assertEqual(nombre, "Ana")
#         self.assertEqual(tiempo, 5)

#     # TODO: agrega más casos:
#     # - atender_persona en cola vacía -> IndexError
#     # - estado() refleja el orden actual
#     # - mezcla de agregar/atender repetidas veces

# if __name__ == "__main__":
#     unittest.main()
