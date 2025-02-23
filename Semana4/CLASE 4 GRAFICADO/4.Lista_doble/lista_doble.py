from nodo_doble import NodoDoble
import graphviz


class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    # Método para agregar un elemento a la lista
    def agregar(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
        self.tamanio += 1

    # Método para mostrar la lista doblemente enlazada
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

    # Método para graficar la lista doblemente enlazada en Graphviz
    def graficar(self, filename="lista_doble"):
        dot = graphviz.Digraph(comment="Lista Doble")

        actual = self.cabeza
        index = 0

        # Crear nodos y relaciones
        while actual is not None:
            dot.node(f"nodo{index}", f"{actual.dato}")
            if actual.siguiente is not None:
                # Conexión hacia el siguiente nodo
                dot.edge(f"nodo{index}", f"nodo{index + 1}", constraint="true")
                # Conexión hacia el nodo anterior
                dot.edge(f"nodo{index + 1}", f"nodo{index}", constraint="true")
            actual = actual.siguiente
            index += 1

        # Guardar y renderizar el gráfico
        dot.render(f"{filename}.gv", view=True)
