
from nodo_doble import NodoDoble 

class ListaDoble:
    def __init__(self):
        self.cabeza = None 
        self.tamanio = 0

    def agregar(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo 
        else: 
            actual = self.cabeza
            while actual.siguiente: 
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo 
            nuevo_nodo.anterior = actual
        self.tamanio += 1
    
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end= " <-> ")
            actual = actual.siguiente
        print("None")