from nodo import Nodo

class Pila:
    def __init__(self):
        self.tope = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.tope is None

    def apilar(self, paciente):
        nuevo_nodo = Nodo(paciente)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tamanio += 1

    def desapilar(self):
        if self.esta_vacia():
            return None
        temp = self.tope
        self.tope = self.tope.siguiente
        self.tamanio -= 1
        return temp.paciente

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, paciente):
        nuevo_nodo = Nodo(paciente)
        if self.esta_vacia():
            self.frente = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
        self.final = nuevo_nodo
        self.tamanio += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        temp = self.frente
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamanio -= 1
        return temp.paciente