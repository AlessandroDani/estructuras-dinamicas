"""
Reto 1: Validador de expresión usando Stack.
Paréntesis válidos: (), {}, []

Función a implementar:
    validate_expression(expression: str) -> bool

Reglas:
- Recorre la cadena; apila aperturas; ante un cierre, desapila y compara.
- Si al final la pila queda vacía y nunca hubo desajuste -> True.

Tips:
- Usa Stack de estructuras/stack.py
"""

from estructuras.stack import Stack

PARES = {')': '(', '}': '{', ']': '['}

def validate_expression(expression: str) -> bool:
    # TODO: Implementar con Stack siguiendo las reglas de arriba.
    # Debe ser O(n) en tiempo; O(n) espacio peor caso.
    if len(expression) == 0:
        return True
    
    pila = Stack()
    for char in expression:
        if char == PARES[')'] or char == PARES['}'] or char == PARES[']']:
            pila.push(char)
        elif char == ')' or char == '}' or char == ']':
            if pila.is_empty():
                return False
            tope = pila.pop()
            if tope != PARES[char]:
                return False
    return pila.is_empty()