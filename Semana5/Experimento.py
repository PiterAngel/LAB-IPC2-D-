class Experimento:
    def __init__(self, nombre=None, filasEnTejido=None, columnasEnTejido=None, tejido=None, proteinas=None):
        self.nombre = nombre
        self.filasEnTejido = filasEnTejido
        self.columnasEnTejido = columnasEnTejido
        self.tejido = tejido
        self.proteinas = proteinas

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getFilasEnTejido(self):
        return self.filasEnTejido
    
    def setFilasEnTejido(self, filasEnTejido):
        self.filasEnTejido = filasEnTejido

    def getColumnasEnTejido(self):
        return self.columnasEnTejido
    
    def setColumnasEnTejido(self, columnasEnTejido):
        self.columnasEnTejido = columnasEnTejido
    
    def getTejido(self):
        return self.tejido
    
    def setTejido(self, tejido):
        self.tejido = tejido

    def getProteinas(self):
        return self.proteinas

    def setProteinas(self, proteinas):
        self.proteinas = proteinas  