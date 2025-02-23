from nodo import Nodo
import graphviz

class ListaCircularSimple:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    # Método para agregar un nodo a la lista circular simple
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        self.tamanio += 1

    # Método para mostrar la lista circular simple
    def mostrar(self):
        if self.cabeza is None:
            return
        actual = self.cabeza
        while True:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("(Inicio)")

    # Método para graficar la lista circular simple con Graphviz
    def graficar(self, filename="lista_circular_simple"):
        dot = graphviz.Digraph(comment='Lista Circular Simple')

        actual = self.cabeza
        index = 0

        # Crear nodos y conexiones entre ellos
        if self.cabeza is not None:
            while True:
                dot.node(f'nodo{index}', f'{actual.dato}')
                if actual.siguiente != self.cabeza:
                    dot.edge(f'nodo{index}', f'nodo{index + 1}', constraint='true')
                else:
                    # Conexión del último nodo al primero para hacer la lista circular
                    dot.edge(f'nodo{index}', 'nodo0', constraint='true')
                    break
                actual = actual.siguiente
                index += 1

        # Guardar y renderizar el gráfico
        dot.render(f'{filename}.gv', view=True)
