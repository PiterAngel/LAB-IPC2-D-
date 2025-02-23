# HOLA SOY UN COMENTARIO
# soy otro comentario

"""
OLA SOY UN COMENTARIO
MULTILINEA
OLA
AAAAAAAA

CONRTOL + S = para guardar
"""

ipc2 = "HOLA SOY UNA VARIABLE"
print("soy el que hace imprimir")
print(ipc2)
print("================================================================")


variable1 = "texto1"
variable2 = "texto2"
variabl3 = variable1 + variable2
print(variabl3)

print("================================================================")

numero1 = 12
numero2 = 3
numero3 = numero1 + numero2
print("al sumar: ", numero1, " y sumar: ", numero2, "El valor es: ", numero3)
print("El valor de la variable 1 es: ", numero1)

decimal1 = 1.1
decimal2 = 2.2
decimal3 = 3
print(decimal1 + decimal2 + decimal3)

print("================================================================")
print("El tipo de dato de la variables es un: ", type(variable1))

# ================================================================
# SENTENCIA IF

variable50 = 50
# (0,50) toma valores de 1 a 49
if variable50 > 50:
    print("El valor es mayor que 50 :)")
# (50,100) toma valores de 51 a 99
elif variable50 < 50:
    print("El valor es menor que 50 :c")
else:
    print("No cumple ninguna")


print("================================================================")

nota = 61
if nota >= 61 and nota <= 100:
    print("Felicidades ganaste IPC2")
elif nota >= 36 and nota <= 60:
    print("Congelaste laboratorio")
else:
    print("F, sale en vacas")

print("================================================================")

# ======= WHILE ======
potencia = 4
while potencia <= 817:
    potencia = potencia * 4
    print(potencia)

# 4 * 4 = 16
# 16 * 4 = 64
# 64 * 4 = 256
# 256 * 4 = 1024
# 1024 * 4 = 4096

print("================================================================")

contadorwhile = 0
while contadorwhile <= 15:
    print(contadorwhile)
    contadorwhile += 1

# ============ FOR ==========
print("================================================================")

for caracater in "palabraaa":
    print(caracater, end=" , ")

print("================================================================")

print(" ")
for palabra2 in range(5):
    if palabra2 == 4:
        print(palabra2)
    else:
        print(palabra2, end=", ")

print("================================================================")


print("================================================================")

def mostrar_menu():
    print("Bienvenidos al menu :)")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

def opcion1():
    print("Estas en la Opción 1")

def opcion2():
    print("Estas en la opción 2")

def opcion3():
    print("Estas en la ocpión 3")

def salir():
    print("ADIOS :)")


def main2():
    while True:
        mostrar_menu()
        opcion = input("Selecciona un número: ")

        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            salir()
            break 
        else: 
            print("ERROR NO EXISTE ESA OPCION")
    


if __name__ == "__main__":
    main2()