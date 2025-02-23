from nodo import Nodo
import graphviz

class Cola:
    def __init__(self):
        self.cabeza = None
        self.final = None
        self.tamanio = 0

    # Insertar datos en la cola
    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final is None:  # Cola vacía
            self.cabeza = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
        self.final = nuevo_nodo
        self.tamanio += 1

    # Eliminar el primer elemento en la cola
    def desencolar(self):
        if self.cabeza is None:
            return None
        valor = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.final = None
        self.tamanio -= 1
        return valor

    # Mostrar los elementos de la cola
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Generar el gráfico en formato DOT para Graphviz
    def graficar(self, filename="cola"):
        dot = graphviz.Digraph(comment='Cola')

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
