from nodo import Nodo


class Cola:
    def __init__(self):
        self.cabeza = None
        self.final = None
        self.tamanio = 0

    #  4 -> 3 -> 2 -> NONE
    # PARA INSERTAR DATOS EN LA COLA
    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final is None: # CUANDO LA COLA ESTA VACIA 
            self.cabeza = nuevo_nodo
        else: 
            self.final.siguiente = nuevo_nodo
        self.final = nuevo_nodo
        self.tamanio += 1


    #  4 -> 3 -> 2 -> NONE
    def desencolar(self):
        if self.cabeza is None:
            return None
        valor = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.final = None
        self.tamanio -= 1
        return valor

    def mostrar(self):
        actual = self.cabeza
        while actual: 
            print(actual.dato, end = " -> ")
            actual = actual.siguiente
        print("None")
