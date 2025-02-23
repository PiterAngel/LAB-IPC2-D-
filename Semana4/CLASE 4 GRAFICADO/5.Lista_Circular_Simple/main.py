from lista_circular_simple import ListaCircularSimple

# Crear una lista circular simple y agregar algunos elementos
lista_circular_simple = ListaCircularSimple()
lista_circular_simple.agregar(10)
lista_circular_simple.agregar(20)
lista_circular_simple.agregar(30)
lista_circular_simple.agregar(40)
lista_circular_simple.agregar(50)

# Mostrar la lista circular simple
lista_circular_simple.mostrar()  # Output: 10 -> 20 -> 30 -> (Inicio)

# Graficar la lista circular simple con Graphviz
lista_circular_simple.graficar('lista_circular_simple_grafica')
