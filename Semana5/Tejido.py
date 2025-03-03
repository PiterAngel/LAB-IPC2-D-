class Tejido:
    def __init__(self, filas=None, columnas=None, rejillaOrdenFil=None, rejillaOrdenCol=None):
        self.filas = filas
        self.columnas = columnas
        self.rejillaOrdenFil = rejillaOrdenFil
        self.rejillaOrdenCol = rejillaOrdenCol

    def getFilas(self):
        return self.filas
    
    def setFilas(self, filas):
        self.filas = filas

    def getColumnas(self):
        return self.columnas
    
    def setColumnas(self, columnas):
        self.columnas = columnas

    def getRejillaOrdenFil(self):
        return self.rejillaOrdenFil
    
    def setRejillaOrdenFil(self, rejillaOrdenFil):
        self.rejillaOrdenFil = rejillaOrdenFil

    def getRejillaOrdenCol(self):
        return self.rejillaOrdenCol
    
    def setRejillaOrdenCol(self, rejillaOrdenCol):
        self.rejillaOrdenCol = rejillaOrdenCol