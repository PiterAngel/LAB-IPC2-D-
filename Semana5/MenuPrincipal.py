from ListaEnlazadaSimple import ListaEnlazadaSimple
from ListaEnlazadaDobleCeldas import ListaEnlazadaDobleCeldas
from Celda import Celda
from Experimento import Experimento
from Tejido import Tejido
from ParejaProteina import ParejaProteina

from Archivo import Archivo


if __name__ == "__main__":


    while True:  
        print("================================================") 
        print("=               MENU PRINCIPAL :3               =")
        print("================================================") 
        print("= 1. Inicializar Sistema                      =")
        print("= 2. Crear Catalogo de Experimentos           =")
        print("= 3. Desarrollar Experimento                  =")
        print("= 4. Mostrar Datos del Estudiante             =")
        print("= 5. Salir                                    =")
        print("================================================") 
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
                listaExperimentos = ListaEnlazadaSimple()
                print("¡Sistema inicializado exitosamente!")
        
        elif opcion == 2:
            ruta = input("Ingrese la ruta del archivo XML: ")
            nuevoArchivo = Archivo(ruta)
            nuevoArchivo.leer(listaExperimentos)
            print("¡Catalogo de experimentos creado exitosamente!")

        
        elif opcion == 3:
            while True:
                print("================================================") 
                print("=           DESARROLLAR EXPERIMENTO          =")
                print("================================================") 
                print("= 1. Cargar Manualmente                       =")
                print("= 2. Cargar del Catalogo                      =")
                print("= 3. Regresar                                 =")
                print("================================================") 
                opcion = int(input("Ingrese una opcion: "))