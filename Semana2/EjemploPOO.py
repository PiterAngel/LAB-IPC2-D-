
from clases.Empleado import Empleado
from clases.Persona import Persona

def Menu():
    print("================= Menu principal =================")
    print("1. Registrar Peronsa")
    print("2. Registrar Empleado")
    print("3. Mostrar Informacón")
    print("4. Opción Administrador")
    print("5. Salir")
    print("================================================")

if __name__ == "__main__":
    personaCreada = None
    empleadoCreado = None

    while True:
        Menu()
        
        opcion = input("Ingrese un número para la opción:")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            edad = input("Ingrese la edad de la persona: ")

            personaCreada = Persona(nombre, edad)
            print("Persona registrada correctamente :)")
        
        elif opcion == "2":
            nombre = input("Ingrese un nombre: ")
            edad = input("Ingrese la edad del empleado: ")
            salario = input("Ingrese el salario: ")

            empleadoCreado = Empleado(nombre, edad, salario)
            print("Empleado registrado correctamente.")
        
        elif opcion == "3":
            print()
            print("Impresion de datos: :0")

            if personaCreada:
                print("Persona: ")
                print(personaCreada.saludar())
                print(personaCreada.despedir())
                print("========================")
            
            if empleadoCreado:
                print("Empleado: ")
                print(empleadoCreado)
                print(empleadoCreado.trabajar())
                print(empleadoCreado.cobrar())
                print("========================")
            
            if not personaCreada and not empleadoCreado:
                print("No hay registros que mostrar :c")
        
        elif opcion == "4":
            print()
            print("Opcion Administrador")

        elif opcion == "5":
            print("Gracias por usar el programa :)")

        else:
            print("Opcion invalidad :,v")