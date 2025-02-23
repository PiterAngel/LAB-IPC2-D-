
from nodo import Nodo

class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else: 
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamanio += 1

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end= " - > ")
            actual = actual.siguiente
        print("None")   
