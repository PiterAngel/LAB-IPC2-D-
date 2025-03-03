

class Estado: 
    def __init__(self, celda1=None, celda2=None):
        self.celda1 = celda1
        self.celda2 = celda2
    
    def getCelda1(self):
        return self.celda1
    
    def setCelda1(self, celda1):
        self.celda1 = celda1

    def getCelda2(self):
        return self.celda2
    
    def setCelda2(self, celda2):
        self.celda2 = celda2