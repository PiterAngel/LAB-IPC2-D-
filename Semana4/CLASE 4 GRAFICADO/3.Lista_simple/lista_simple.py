from nodo import Nodo
import graphviz

class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    # Método para agregar un elemento a la lista
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamanio += 1

    # Método para mostrar los elementos de la lista
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Método para graficar la lista en Graphviz
    def graficar(self, filename="lista_simple"):
        dot = graphviz.Digraph(comment='Lista Simple')

        actual = self.cabeza
        index = 0
        # Crear nodos y relaciones
        while actual is not None:
            dot.node(f'nodo{index}', f'{actual.dato}')
            if actual.siguiente is not None:
                dot.edge(f'nodo{index}', f'nodo{index + 1}')
            actual = actual.siguiente
            index += 1

        # Guardar y renderizar el gráfico
        dot.render(f'{filename}.gv', view=True)
