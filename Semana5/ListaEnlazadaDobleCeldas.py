class Nodo:
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

class ListaEnlazadaDobleCeldas:
    def __init__(self):
        self.primero = None
        self.largo = 0
    
    def insertar(self, numero):
        nodo = Nodo(dato=numero)
        if self.primero is None:
            self.primero = nodo
            self.largo += 1
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo
            nodo.anterior = actual
            self.largo += 1

    def cambiarEstadoInerte(self, posicion):
        actual = self.primero
        while actual:
            if actual.dato.getPosicion() == posicion:
                actual.dato.setInerte(True)
                return True
            actual = actual.siguiente
        return False

    def recorrer(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            if actual.dato == 3:
                break
            actual = actual.siguiente
        while actual:
            print(actual.dato)
            actual = actual.anterior
    
    def datos(self):
        datos = self.primero
        return datos

    def longitud(self):
        return self.largo