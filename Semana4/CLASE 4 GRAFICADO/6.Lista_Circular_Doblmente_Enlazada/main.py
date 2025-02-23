from lista_circular_doble import ListaCircularDoble

# Crear una lista circular doble y agregar algunos elementos
lista_circular_doble = ListaCircularDoble()
lista_circular_doble.agregar(10)
lista_circular_doble.agregar(20)
lista_circular_doble.agregar(30)
lista_circular_doble.agregar(40)
lista_circular_doble.agregar(50)

# Mostrar la lista circular doble
lista_circular_doble.mostrar()  # Output: 10 <-> 20 <-> 30 <-> (Inicio)

# Graficar la lista circular doble con Graphviz
lista_circular_doble.graficar('lista_circular_doble_grafica')
