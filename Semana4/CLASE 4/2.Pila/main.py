
from pila import Pila

    # | 3 |
    # | 2 |
    # | 1 |

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print(pila.mostrar())
pila.desapilar()
print(pila.mostrar())
# EL ULTIMO EN ENTRAR ES EL PRIMERO EN SALIR

    # |   |
    # | 2 |
    # | 1 |
