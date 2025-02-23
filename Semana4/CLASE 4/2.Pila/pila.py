
from nodo import Nodo

class Pila:

    # |   |
    # | - |
    # | - |

    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar (self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo 
        self.tamanio += 1

    def desapilar(self):
        if self.cima is None:
            return None
        valor = self.cima.dato 
        self.cima = self.cima.siguiente
        self.tamanio -= 1
        return valor

    def mostrar(self):
        actual = self.cima 
        while actual:
            print(actual.dato, end= " - > " )
            actual = actual.siguiente
        print(" None ")