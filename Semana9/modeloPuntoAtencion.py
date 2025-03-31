class PuntoAtencion:
    
    def __init__(self, id, nombre, direccion, escritorios, escritoriosActivos, clientes):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.escritorios = escritorios
        self.escritoriosActivos = escritoriosActivos
        self.clientes = clientes
        self.turnoEnPunto = 0
        self.turnoAPasar = 0

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def getEscritorios(self):
        return self.escritorios

    def getEscritoriosActivos(self):
        return self.escritoriosActivos

    def getClientes(self):
        return self.clientes

    def getTurnoEnPunto(self):
        return self.turnoEnPunto

    def getTurnoAPasar(self):
        return self.turnoAPasar

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion
    
    def setEscritorios(self, escritorios):
        self.escritorios = escritorios
    
    def setEscritoriosActivos(self, escritoriosActivos):
        self.escritoriosActivos = escritoriosActivos

    def setClientes(self, clientes):
        self.clientes = clientes

    def setTurnoEnPunto(self):
        self.turnoEnPunto += 1

    def setTurnoAPasar(self):
        self.turnoAPasar += 1