import unittest
from retos.reto1_stack import validate_expression

class TestChallenge1Stack(unittest.TestCase):
    def test_simple_balanced_expression(self):
        # Arrange
        expresion = "({[]})"
        # Act
        resultado = validate_expression(expresion)
        # Assert
        self.assertTrue(resultado)

    def test_unbalanced_expression(self):
        expresion = "({[]})]"
        resultado = validate_expression(expresion)
        self.assertFalse(resultado)

    def test_order_incorrect_expression(self):
        expresion = "({[})]"
        resultado = validate_expression(expresion)
        self.assertFalse(resultado)

    def test_empty_expression(self):
        expresion = ""
        resultado = validate_expression(expresion)
        self.assertTrue(resultado)

    def test_only_opening_brackets(self):
        expresion = "((([[{{"
        resultado = validate_expression(expresion)
        self.assertFalse(resultado)
    
    def test_only_closing_brackets(self):
        expresion = "}}]]))"
        resultado = validate_expression(expresion)
        self.assertFalse(resultado)
    

    
    # TODO: agrega más casos:
    # - desbalance por cierre extra
    # - orden incorrecto "{[}]"
    # - cadena vacía -> True
    # - solo aperturas -> False

if __name__ == "__main__":
    unittest.main()
