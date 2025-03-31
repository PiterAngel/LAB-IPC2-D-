class Escritorio: 
    
    def __init__(self, id, identificacionEscritorio, nombreEncargado, estado, clientesAtendidos):
        self.id = id 
        self.identificacionEscritorio = identificacionEscritorio
        self.nombreEncargado = nombreEncargado
        self.estado = estado
        self.clientesAtendidos = clientesAtendidos

    def getId(self):
        return self.id
    
    def getIdentificacionEscritorio(self):
        return self.identificacionEscritorio

    def getNombreEncargado(self):
        return self.nombreEncargado
    
    def getEstado(self):
        return self.estado
    
    def getClientesAtendidos(self):
        return self.clientesAtendidos
    
    def setIdentificacionEscritorio(self, identificacionEscritorio):
        self.identificacionEscritorio = identificacionEscritorio

    def setNombreEncargado(self, nombreEncargado):
        self.nombreEncargado = nombreEncargado

    def setEstado(self, estado):
        self.estado = estado
    
    def setClientesAtendidos(self, clientesAtendidos):
        self.clientesAtendidos = clientesAtendidos