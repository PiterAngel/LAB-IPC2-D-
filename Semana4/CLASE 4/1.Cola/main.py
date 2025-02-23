
from cola import Cola

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.encolar(5)


print(cola.mostrar())

# Primero en entrar es el primero en salir 
print(cola.desencolar()) 

print(cola.mostrar())
