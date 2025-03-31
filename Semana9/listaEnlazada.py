class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato 
        self.siguiente = siguiente
    
class listaEnlazada: 
    def __init__(self):
        self.primero = None
        self.tamanio = 0
    
    def insertar(self, dato):
        if self.primero is None:
            self.primero = Nodo(dato=dato)
            self.tamanio += 1
            return 
        actual = self.primero 
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato=dato)
        self.tamanio += 1

    def valores(self):
        valores = self.primero 
        return valores
    
    def longitud(self):
        return self.tamanio

    def eliminarPrimero(self):
        primero = self.primero 
        if self.primero != None:
            self.primero = self.primero.siguiente
        if primero != None: 
            primero.siguiente = None
            self.tamanio -=1 
        return primero 
    
    def eliminarUltimo(self):
        actual = self.primero 
        anterior = None
        ultimo = None

        if actual != None:
            while actual and actual.siguiente != None:
                anterior = actual 
                actual = actual.siguiente

            if anterior is None:
                ultimo = self.primero
                self.primero = actual.siguiente
                actual.siguiente = None
                self.tamanio -= 1
            elif actual:
                ultimo = anterior.siguiente
                anterior.siguiente = actual.siguiente
                actual.siguiente = None
                self.tamanio -= 1
        return ultimo
    
    def buscarId(self, id):
        actual = self.primero
        anterior = None

        while actual and actual.dato.getId() != id:
            anterior = actual 
            actual = actual.siguiente
        
        if actual != None: 
            return actual 
        else: 
            return 
        
    def buscarNombre(self, nombre):
        actual = self.primero
        anterior = None

        while actual and actual.dato.getNombre().lower() != nombre.lower():
            anterior = actual 
            actual = actual.siguiente
        
        if actual != None:
            return actual 
        else:
            return
    
    def buscarPosicion(self, posicion):
        pos = 1
        if posicion > 0:
            actual = self.primero
            anterior = None

            while actual and pos != posicion:
                pos += 1
                anterior = actual
                actual = actual.siguiente 
            
            if actual != None:
                return actual 
            else: 
                return 
        else:
            return
        
    def recorrer(self):
        actual = self.primero 
        while actual != None:
            print(actual.dato)
            actual = actual.siguiente
