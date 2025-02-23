from pila import Pila

# Crear una pila y apilar algunos elementos
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(5)
pila.apilar(6)

# Mostrar el estado actual de la pila
pila.mostrar()

# Desapilar el elemento de la cima
pila.desapilar()

# Mostrar el estado de la pila después de desapilar
pila.mostrar()

# Graficar la pila usando Graphviz
pila.graficar('pila_grafica')
