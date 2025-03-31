from listaEnlazada import listaEnlazada

class Empresa:

    def __init__(self, id, nombre, abreviatura, puntosAtencion, transacciones):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.puntosAtencion = puntosAtencion
        self.transacciones = transacciones
    
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getAbreviatura(self):
        return self.abreviatura

    def getPuntosDeAtencion(self):
        return self.puntosAtencion
    
    def getTransacciones(self):
        return self.transacciones

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setAbreviatura(self, abreviatura):
        self.abreviatura = abreviatura

    def setPuntosDeAtencion(self, puntosAtencion):
        self.puntosAtencion = puntosAtencion

    def setTransacciones(self, transacciones):
        self.transacciones = transacciones