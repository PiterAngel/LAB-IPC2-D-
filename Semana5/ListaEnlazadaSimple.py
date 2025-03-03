
class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
    
class ListaEnlazadaSimple:
    def __init__(self):
        self.primero = None
        self.largo = 0

    def insertar(self, dato):
        nodo = Nodo(dato=dato)
        if self.primero is None:
            self.primero = nodo
            self.largo  += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo
        self.largo += 1 

    def eliminar (self, posicion):
        actual = self.primero
        anterior = None
        while actual and actual.dato.posicion != posicion:
            anterior = actual 
            actual = actual.siguiente
        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual: 
            anterior.siguiente = actual.siguiente
            actual.siguiente = None
        self.largo -= 1 
    
    def buscar(self,posicion):
        actual = self.primero 
        anterior = None
        while actual and actual.dato.posicion != posicion:
            anterior = actual
            actual = actual.siguiente
        if actual != None:
            return actual.dato
        else: 
            print("Error, no encontrado :c")

    def datos(self):
        datos = self.primero
        return datos
    
    def recorrer(self):
        actual = self.primero 
        while actual != None:
            print(actual.dato)
            actual = actual.siguiente
        
    def longitud(self):
        return self.largo