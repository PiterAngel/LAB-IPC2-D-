from nodo_matriz import NodoMatriz

class MatrizDispersa:
    def __init__(self):
        self.cabecera = None

    def insertar(self, fila, columna, valor):
        nuevo_nodo = NodoMatriz(fila, columna, valor)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
        else:
            actual = self.cabecera
            while actual.siguiente and actual.fila < fila:
                actual = actual.siguiente
            while actual.abajo and actual.columna < columna:
                actual = actual.abajo
            actual.siguiente = nuevo_nodo
            actual.abajo = nuevo_nodo

    def mostrar(self):
        actual = self.cabecera
        while actual:
            print(f"({actual.fila}, {actual.columna}) -> {actual.valor}")
            actual = actual.siguiente
