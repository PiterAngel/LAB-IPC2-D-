from lista_doble import ListaDoble

# Crear una lista doblemente enlazada y agregar algunos elementos
lista_doble = ListaDoble()
lista_doble.agregar(10)
lista_doble.agregar(20)
lista_doble.agregar(30)

# Mostrar el estado actual de la lista
lista_doble.mostrar()

# Graficar la lista usando Graphviz
lista_doble.graficar('lista_doble_grafica')
