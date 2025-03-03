
class Celda: 
    def __init__(self, celula=None, posicion=None, posicionX=None, posicionY=None, inerte=False ):
        self.celula = celula
        self.posicion = posicion
        self.posicionY = posicionY
        self.posicionX = posicionX
        self.inerte = inerte
        
    
    def getCelula(self):
        return self.celula

    def setCelula(self, celula):
        self.celula = celula 
    
    def getPosicion(self):
        return self.posicion

    def setPosicion(self, posicion):
        self.posicion = posicion
    
    def getPosicionX(self):
        return self.posicionX
    
    def setPosicionX(self, posicionX):
        self.posicionX = posicionX

    def getPosicionY(self):
        return self.posicionY
    
    def setPosicionY(self, posicionY):
        self.posicionY = posicionY

    def getInerte(self):
        return self.inerte
    
    def setInerte(self, inerte):
        self.inerte = inerte