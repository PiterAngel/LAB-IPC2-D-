from cola import Cola

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.encolar(5)

# Mostrar la cola
cola.mostrar()

# Desencolar el primer elemento
print(cola.desencolar())

# Mostrar la cola actualizada
cola.mostrar()

# Graficar la cola usando Graphviz
cola.graficar("cola_grafica")
