
from nodo_doble import NodoDoble

class ListaCircularDoble:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def agregar(self,dato):
        nuevo_nodo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = self.cabeza 
        else: 
            actual = self.cabeza.anterior 
            actual.siguiente = nuevo_nodo 
            nuevo_nodo.anterior = actual
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
        self.tamanio += 1

    def mostrar(self):
        if self.cabeza is None:
            return 
        actual = self.cabeza
        while True: 
            print(actual.dato, end = " <-> ")
            actual = actual.siguiente
            if actual == self.cabeza: 
                break 
        print(" (INICIO) ")