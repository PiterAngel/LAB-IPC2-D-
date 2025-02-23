from nodo_doble import NodoDoble
import graphviz

class ListaCircularDoble:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    # Método para agregar un nodo a la lista circular doble
    def agregar(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = self.cabeza
        else:
            actual = self.cabeza.anterior
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
        self.tamanio += 1

    # Método para mostrar la lista circular doble
    def mostrar(self):
        if self.cabeza is None:
            return
        actual = self.cabeza
        while True:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("(Inicio)")

    # Método para graficar la lista circular doble con Graphviz
    def graficar(self, filename="lista_circular_doble"):
        dot = graphviz.Digraph(comment='Lista Circular Doble', format='png')

        actual = self.cabeza
        index = 0

        # Crear nodos y conexiones dobles
        if self.cabeza is not None:
            while True:
                dot.node(f'nodo{index}', f'{actual.dato}')

                # Conexión al siguiente nodo
                dot.edge(f'nodo{index}', f'nodo{(index + 1) % self.tamanio}', dir='both')

                # Conexión al nodo anterior
                dot.edge(f'nodo{index}', f'nodo{(index - 1) % self.tamanio}', dir='both')

                actual = actual.siguiente
                index += 1

                # Si hemos vuelto al inicio, cerramos el ciclo
                if actual == self.cabeza:
                    break

        # Guardar y renderizar el gráfico
        dot.render(f'{filename}.gv', view=True)
