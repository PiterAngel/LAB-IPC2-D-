class Transaccion: 

    def __init__(self, id= None, nombre=None, tiempo=None, cantidad=None):
        self.id = id
        self.nombre= nombre
        self.tiempo = tiempo
        self.cantidad = cantidad

    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getTiempo(self):
        return self.tiempo
    
    def getCantidad(self):
        return self.cantidad
 

    def setId(self, id):
        self.id = id
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setTiempo(self, tiempo):
        self.tiempo = tiempo
    
    def setCantidad(self, cantidad):
        self.cantidad = cantidad