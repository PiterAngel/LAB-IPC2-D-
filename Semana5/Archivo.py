import xml.etree.ElementTree as ET
from Experimento import Experimento
from ListaEnlazadaSimple import ListaEnlazadaSimple
from ListaEnlazadaDobleCeldas import ListaEnlazadaDobleCeldas
from Tejido import Tejido
from Celda import Celda
from ParejaProteina import ParejaProteina

class Archivo:
    def __init__(self, ruta):
        self.ruta = ruta

    def getRuta(self):
        return self.ruta
    
    def setRuta(self, ruta):
        self.ruta = ruta

    def leer(self, listaExperimentos):
        tree = ET.parse(self.ruta)
        experimentos = tree.getroot()

        for experimento in experimentos:
            nuevoExperimento = Experimento()

            # Tejido
            nombre = experimento.attrib['nombre']
            tejido = experimento.find('tejido')
            filas = int(tejido.attrib['filas'])
            columnas = int(tejido.attrib['columnas'])
            rejilla = tejido.find('rejilla')    
            rejilla = rejilla.text.replace("\n", " ").split()

            # Obtener valores en orden de filas
            rejillaOrdenFil = ListaEnlazadaSimple()
            posCol = 0
            for i in range(filas):
                filaRejilla = ListaEnlazadaDobleCeldas()
                for j in range(columnas):
                    nuevaCelda = Celda(rejilla[posCol], (posCol+1), (i+1), (j+1),  False)
                    filaRejilla.insertar(nuevaCelda)
                    posCol += 1
                rejillaOrdenFil.insertar(filaRejilla)

            # Otener valores en orden de columnas
            rejillaOrdenCol = ListaEnlazadaSimple()
            posFil = 0
            posCol = 0
            for j in range(columnas):
                posFil = posCol
                columnaRejilla = ListaEnlazadaDobleCeldas()
                for i in range(filas):
                    nuevaCelda = Celda(rejilla[posFil], (posFil+1), (posFil+1), (posCol+1),  False)
                    columnaRejilla.insertar(nuevaCelda)
                    posFil += columnas
                rejillaOrdenCol.insertar(columnaRejilla)
                posCol += 1

            # Crear nuevo tejido
            nuevoTejido = Tejido(filas, columnas, rejillaOrdenFil, rejillaOrdenCol)

            # Proteina
            listaProteinas = ListaEnlazadaSimple()
            proteinas = experimento.find('proteinas')
            for pareja in proteinas.findall('pareja'):
                parejaProteina = pareja.text.replace("\n", " ").split()
                nuevaParejaProteina = ParejaProteina()
                nuevaParejaProteina.setProteina1(parejaProteina[0])
                nuevaParejaProteina.setProteina2(parejaProteina[1])
                listaProteinas.insertar(nuevaParejaProteina)

            nuevoExperimento.setNombre(nombre)
            nuevoExperimento.setFilasEnTejido(filas)
            nuevoExperimento.setColumnasEnTejido(columnas)
            nuevoExperimento.setTejido(nuevoTejido)
            nuevoExperimento.setProteinas(listaProteinas)
            listaExperimentos.insertar(nuevoExperimento)