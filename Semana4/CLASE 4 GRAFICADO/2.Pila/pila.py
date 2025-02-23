from nodo import Nodo
import graphviz

class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    # Método para apilar un dato en la pila
    def apilar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo
        self.tamanio += 1

    # Método para desapilar el dato de la cima
    def desapilar(self):
        if self.cima is None:
            return None
        valor = self.cima.dato
        self.cima = self.cima.siguiente
        self.tamanio -= 1
        return valor

    # Método para mostrar los elementos en la pila
    def mostrar(self):
        actual = self.cima
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Método para graficar la pila en Graphviz
    def graficar(self, filename="pila"):
        dot = graphviz.Digraph(comment='Pila')

        actual = self.cima
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
