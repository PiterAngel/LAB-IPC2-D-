from lista_simple import ListaSimple

# Crear una lista y agregar algunos elementos
lista = ListaSimple()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

# Mostrar el estado actual de la lista
lista.mostrar()

# Graficar la lista usando Graphviz
lista.graficar('lista_simple_grafica')
