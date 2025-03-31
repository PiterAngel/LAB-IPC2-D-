class Cliente:

    def __init__(self, dpi, nombre, transacciones, tiempoEnEspera, tiempoEnAtencion):
        self.dpi = dpi
        self.nombre = nombre
        self.transacciones = transacciones
        self.tiempoEnEspera = tiempoEnEspera
        self.tiempoEnAtencion = tiempoEnAtencion

    def getId(self):
        return self.dpi
    
    def getNombre(self):
        return self.nombre
    
    def getTransacciones(self):
        return self.transacciones
    
    def getTiempoEnEspera(self):
        return self.tiempoEnEspera
    
    def getTiempoEnAtencion(self):
        return self.tiempoEnAtencion
    

    def setId(self, dpi):
       self.dpi = dpi
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setTransacciones(self, transacciones):
        self.transacciones = transacciones
    
    def setTiempoEnEspera(self, tiempoEnEspera):
        self.tiempoEnEspera = tiempoEnEspera
    
    def setTiempoEnAtencion(self, tiempoEnAtencion):
        self.tiempoEnAtencion = tiempoEnAtencion
    