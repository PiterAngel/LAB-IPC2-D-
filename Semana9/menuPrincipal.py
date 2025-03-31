from cargarArchivo import CargarArchivo
from listaEnlazada import listaEnlazada
from modeloEmpresa import Empresa
from modeloPuntoAtencion import PuntoAtencion
from modeloCliente import Cliente
from modeloEscritorio import Escritorio
from modeloTransaccion import Transaccion
from grafico import Grafico
import os

class MenuPrincipal:
    
    def __init__(self):
        self.listaEmpresas = listaEnlazada()
        self.menu()

    def menu(self):
        idEmpresa = 0
        while True:
            print(" -----------------Menu Principal----------------- ")
            print("| 1. Configuracion de Empresas                   |")
            print("| 2. Seleccion de Empresa y Punto de Atencion    |")
            print("| 3. Limpiar Sistema                             |")
            print("| 4. Salir                                       |")
            print(" ------------------------------------------------ ")
            try:
                opcion = int(input("Ingrese una opcion: "))
                if opcion == 1:
                    menu = True
                    while menu:
                        print(" -----------Configuracion de Empresas------------ ")
                        print("| 1. Cargar Archivo de Configuracion del Sistema |")
                        print("| 2. Cargar Archivo con Configuracion Inicial    |")
                        print("| 4. Regresar al Menu Principal                  |")
                        print(" ------------------------------------------------ ")
                        try:
                            archivo = CargarArchivo(self.listaEmpresas)
                            opcion = int(input("Ingrese una opcion: "))
                            if opcion == 1:
                                #ConfiguracionSistema.xml
                                ruta = input("Ingrese la ruta del archivo -> ")
                                archivo.leerArchivoConfiguracionSistema(ruta)
                                print("¡Archivo leido exitosamente!")
                            elif opcion == 2:
                                if self.listaEmpresas.valores() != None:
                                    #ConfiguracionInicial.xml
                                    ruta = input("Ingrese la ruta del archivo -> ")
                                    archivo.leerArchivoConfiguracionInicial(ruta) 
                                    print("¡Archivo leido exitosamente!") 
                                else: print("¡Sistema vacio! No se pudo aplicar la configuracion")                                                                  
                            elif opcion == 4: break
                            else: 
                                print("¡Ingrese una opcion valida!")
                        except ValueError:
                            print("¡Ingrese solo numeros!")
                        except FileNotFoundError:
                            print("¡El archivo no existe!")                     
                elif opcion == 2:
                    resultado = self.mostrarEmpresas()
                    if resultado == False: continue
                    posicion = int(input("Ingrese un numero: "))                                 
                    empresa = self.listaEmpresas.buscarPosicion(posicion)
                    if empresa == None: continue
                    listaTransacciones = empresa.dato.getTransacciones()
                    listaPuntosAtencion = empresa.dato.getPuntosDeAtencion()
                    resultado = self.mostrarPuntosAtencion(listaPuntosAtencion)
                    if resultado == False: continue
                    posicion = int(input("Ingrese un numero: "))
                    listaPuntosAtencion = empresa.dato.getPuntosDeAtencion()                         
                    punto = listaPuntosAtencion.buscarPosicion(posicion)
                    if punto == None: continue
                    while True:
                        print(" ----------Manejo de Puntos de Atencion---------- ")
                        print("| 1. Ver Estado                                  |")
                        print("| 7. Regresar al Menu Principal                  |")
                        print(" ------------------------------------------------ ")
                        try:
                            opcion = int(input("Ingrese una opcion: "))
                            if opcion == 1:
                                graficar = Grafico()
                                graficar.encabezado(empresa.dato.getNombre().upper())
                                self.graficarYCalcularTiemposEnPunto(punto, graficar)
                                self.graficarYCalcularTiemposEnEscritorio(punto, graficar)
                                graficar.exportar()
                                print("¡Reporte de estado generado exitosamente!")
                                os.system("reporte.pdf")
                            
                            elif opcion == 7: break
                            else: 
                                print("¡Ingrese una opcion valida!")
                        except FileExistsError:
                            print("error")
                elif opcion == 3:
                    self.listaEmpresas = listaEnlazada()
                    print("¡Sistema limpiado exitosamente!")              
                elif opcion == 4:
                    print("¡Ejecucion Finalizada!")
                    break
                elif opcion == 5:
                    empresaEnLista = self.listaEmpresas.valores()
                    while empresaEnLista != None:
                        print(empresaEnLista.dato.getId())
                        print(empresaEnLista.dato.getNombre())
                        print(empresaEnLista.dato.getAbreviatura())
                        puntosAtencionEnLista = empresaEnLista.dato.getPuntosDeAtencion().valores()
                        while puntosAtencionEnLista != None:
                            print(puntosAtencionEnLista.dato.getId())
                            print(puntosAtencionEnLista.dato.getNombre())
                            print(puntosAtencionEnLista.dato.getDireccion())
                            escritoriosEnLista = puntosAtencionEnLista.dato.getEscritorios().valores()
                            while escritoriosEnLista != None:
                                print(escritoriosEnLista.dato.getId())
                                print(escritoriosEnLista.dato.getIdentificacionEscritorio())
                                print(escritoriosEnLista.dato.getNombreEncargado())
                                print(escritoriosEnLista.dato.getEstado())
                                escritoriosEnLista = escritoriosEnLista.siguiente
                            puntosAtencionEnLista = puntosAtencionEnLista.siguiente
                        transaccionesEnLista = empresaEnLista.dato.getTransacciones().valores()
                        while transaccionesEnLista != None:
                            print(transaccionesEnLista.dato.getId())
                            print(transaccionesEnLista.dato.getNombre())
                            print(transaccionesEnLista.dato.getTiempo())
                            print(transaccionesEnLista.dato.getCantidad())
                            transaccionesEnLista = transaccionesEnLista.siguiente
                        empresaEnLista = empresaEnLista.siguiente
                else:
                    #except Exception as e:
                    print("¡Ingrese una opcion valida!")
            except ValueError:
                print("¡Ingrese solo numeros!")
    
    def recorrer(self, punto):
        listaClientes = punto.dato.getClientes().valores()
        if listaClientes != None:
            print("-------Tiempos en Espera Actualizados--------")
            while listaClientes != None:
                t = listaClientes.dato.getTiempoEnEspera() 
                print(listaClientes.dato.getNombre(),":", self.convertirTiempo(t))
                listaClientes = listaClientes.siguiente

    def atenderClientes(self, atenderATodos, punto):
        listaEscritoriosActivos = punto.dato.getEscritoriosActivos().valores()
        listaClientes = punto.dato.getClientes()
        if listaClientes.longitud() != 0:
            if listaEscritoriosActivos != None:
                print("-----------------Finalizados-----------------")
                while listaEscritoriosActivos != None:
                    listaclientesAtendidos = listaEscritoriosActivos.dato.getClientesAtendidos()
                    if listaClientes.longitud() > 0:
                        clienteAtendido = listaClientes.eliminarPrimero()
                        listaclientesAtendidos.insertar(clienteAtendido.dato)
                        print("Cliente", clienteAtendido.dato.getNombre(), "atendido en escritorio", listaEscritoriosActivos.dato.getIdentificacionEscritorio())                                                          
                    else: break  
                    listaEscritoriosActivos = listaEscritoriosActivos.siguiente
                    if atenderATodos:
                        if listaEscritoriosActivos == None:
                            listaEscritoriosActivos = punto.dato.getEscritoriosActivos().valores()
            else:
                print("¡No hay escritorios activos! No se pudo realizar la operacion.")
                return False
        else: 
            print("¡No hay clientes pendientes de atender!")
            return False

    def calcularTiempoEnEspera(self, listaEscritoriosActivos, listaClientesEnPunto, listaClientes):
        cantidadEscritoriosActivos = listaEscritoriosActivos.longitud()
        listaClientes = listaClientes.valores()
        if cantidadEscritoriosActivos == 0 or cantidadEscritoriosActivos == 1:
            tiempoEnEspera = 0
            while listaClientes != None and listaClientesEnPunto.longitud() > 1:
                tiempoEnEspera += listaClientes.dato.getTiempoEnAtencion()
                if listaClientes.siguiente != None:
                    listaClientes.siguiente.dato.setTiempoEnEspera(tiempoEnEspera)
                listaClientes = listaClientes.siguiente
        else:
            if listaClientesEnPunto.longitud() >= 1:
                tiempoEnEspera = listaClientesEnPunto.buscarPosicion(1).dato.getTiempoEnEspera()
            tiempoMax = 0
            while listaClientes != None:
                tiempoEnEspera += tiempoMax
                tiempoMax = 0 
                cantidadEscritoriosActivos = listaEscritoriosActivos.longitud()
                while cantidadEscritoriosActivos > 0 and listaClientes != None:
                    listaClientes.dato.setTiempoEnEspera(tiempoEnEspera)
                    tiempo = listaClientes.dato.getTiempoEnAtencion()
                    if tiempo > tiempoMax:
                        tiempoMax = tiempo
                    cantidadEscritoriosActivos -= 1
                    listaClientes = listaClientes.siguiente
            
    def mostrarEmpresas(self):         
        if self.listaEmpresas.valores() != None:
            numero = 0
            empresaEnLista = self.listaEmpresas.valores()
            print(" ----------------------------------------------------------------------- ")
            print("| No. |    Id     |            Nombre            |     Abreviatura      |")
            print("|-----------------------------------------------------------------------|")
            while empresaEnLista != None:
                numero += 1
                print("|", numero, (2-len(str(numero)))*(" "), "|", empresaEnLista.dato.getId(), (8-len(str(empresaEnLista.dato.getId())))*(" "), "|", empresaEnLista.dato.getNombre(),
                (27-len(empresaEnLista.dato.getNombre()))*(" "), ("|"), empresaEnLista.dato.getAbreviatura(), (19-len(str(empresaEnLista.dato.getAbreviatura())))*(" "), "|")
                empresaEnLista = empresaEnLista.siguiente
            print(" ----------------------------------------------------------------------- ")
            return True
        else:
            print("¡Sistema vacio!")
            return False
    
    def mostrarPuntosAtencion(self, listaPuntosAtencion):
        if listaPuntosAtencion.valores() != None:
            numero = 0
            listaPuntosAtencion = listaPuntosAtencion.valores()   
            print(" ------------------------------------------------------------------------- ")
            print("| No. |    Id     |            Nombre            |       Direccion        |")
            print("|-------------------------------------------------------------------------|")
            while listaPuntosAtencion != None:
                numero += 1
                print("|", numero, (2-len(str(numero)))*(" "), "|", listaPuntosAtencion.dato.getId(), (8-len(str(listaPuntosAtencion.dato.getId())))*(" "), "|", listaPuntosAtencion.dato.getNombre(), 
                (27-len(listaPuntosAtencion.dato.getNombre()))*(" "), "|", listaPuntosAtencion.dato.getDireccion(), (21-len(listaPuntosAtencion.dato.getDireccion()))*(" "), ("|"))
                listaPuntosAtencion = listaPuntosAtencion.siguiente
            print(" ------------------------------------------------------------------------- ")
            return True
        else:
            print("¡Sin puntos de atencion!")
            return False

    def mostrarTransacciones(self, listaTransacciones):
        if listaTransacciones.valores() != None:
            numero = 0
            listaTransacciones = listaTransacciones.valores()
            print(" --------------------------------------------------------- ")
            print("| No. |    Id     |            Nombre            | Tiempo |")
            print("|---------------------------------------------------------|")
            while listaTransacciones != None:
                numero += 1
                print("|", numero, (2-len(str(numero)))*(" "), "|", listaTransacciones.dato.getId(), (8-len(str(listaTransacciones.dato.getId())))*(" "), "|", listaTransacciones.dato.getNombre(), 
                (27-len(listaTransacciones.dato.getNombre()))*(" "), "|", listaTransacciones.dato.getTiempo(), (5-len(str(listaTransacciones.dato.getTiempo())))*(" "), ("|"))
                listaTransacciones = listaTransacciones.siguiente
            print(" --------------------------------------------------------- ")
            return True
        else:
            print("¡Sin transacciones!")
            return False

    def graficarYCalcularTiemposEnPunto(self, punto, graficar):
        tiempoMinEspera = 0
        tiempoPromEspera = 0
        tiempoMaxEspera = 0
        tiempoMinAtencion = 0
        tiempoPromAtencion = 0
        tiempoMaxAtencion = 0
        escritoriosActivos = 0
        escritoriosInactivos = 0
        clientesAtendidos = 0
        clientes = punto.dato.getClientes().longitud()
        if punto.dato.getClientes() != None:
            escritoriosActivos = punto.dato.getEscritoriosActivos().longitud()
            escritoriosInactivos = (punto.dato.getEscritorios().longitud()-escritoriosActivos)
            listaEscritorios = punto.dato.getEscritorios().valores()
            while listaEscritorios != None:
                clientesAtendidos += listaEscritorios.dato.getClientesAtendidos().longitud()
                listaclientesAtendidos = listaEscritorios.dato.getClientesAtendidos().valores()
                while listaclientesAtendidos != None:
                    tiempo = listaclientesAtendidos.dato.getTiempoEnEspera()
                    if tiempoMinEspera == 0:
                        tiempoMinEspera = tiempo
                    if tiempo < tiempoMinEspera:
                        tiempoMinEspera = tiempo
                    if tiempo > tiempoMaxEspera:
                        tiempoMaxEspera = tiempo
                    tiempoPromEspera += tiempo
                    tiempo = listaclientesAtendidos.dato.getTiempoEnAtencion()
                    if tiempoMinAtencion == 0:
                        tiempoMinAtencion = tiempo
                    if tiempo < tiempoMinAtencion:
                        tiempoMinAtencion = tiempo
                    if tiempo > tiempoMaxAtencion:
                        tiempoMaxAtencion = tiempo
                    tiempoPromAtencion += tiempo
                    listaclientesAtendidos = listaclientesAtendidos.siguiente  
                listaEscritorios = listaEscritorios.siguiente 
        if clientesAtendidos > 0:
            tiempoPromEspera = tiempoPromEspera/clientesAtendidos
            tiempoPromAtencion = tiempoPromAtencion/clientesAtendidos
        tiempoMinEspera = self.convertirTiempo(tiempoMinEspera)
        tiempoPromEspera = self.convertirTiempo(tiempoPromEspera)
        tiempoMaxEspera = self.convertirTiempo(tiempoMaxEspera)
        tiempoMinAtencion = self.convertirTiempo(tiempoMinAtencion)
        tiempoPromAtencion = self.convertirTiempo(tiempoPromAtencion)
        tiempoMaxAtencion = self.convertirTiempo(tiempoMaxAtencion)        
        graficar.puntoAtencion(punto.dato.getNombre(), escritoriosActivos, escritoriosInactivos, clientes, clientesAtendidos, tiempoMinEspera, tiempoPromEspera, tiempoMaxEspera, tiempoMinAtencion, tiempoPromAtencion, tiempoMaxAtencion)

    def graficarYCalcularTiemposEnEscritorio(self, punto, graficar):
        if punto.dato.getEscritoriosActivos() != None:
            listaEscritoriosActivos = punto.dato.getEscritoriosActivos().valores()
            numero = 0
            while listaEscritoriosActivos != None:
                numero += 1
                clientesAtendidos = listaEscritoriosActivos.dato.getClientesAtendidos().longitud()
                listaclientesAtendidos = listaEscritoriosActivos.dato.getClientesAtendidos().valores()
                tiempoMinAtencion = 0
                tiempoPromAtencion = 0
                tiempoMaxAtencion = 0
                while listaclientesAtendidos != None:
                    tiempo = listaclientesAtendidos.dato.getTiempoEnAtencion()
                    if tiempoMinAtencion == 0:
                        tiempoMinAtencion = tiempo
                    if tiempo < tiempoMinAtencion:
                        tiempoMinAtencion = tiempo
                    if tiempo > tiempoMaxAtencion:
                        tiempoMaxAtencion = tiempo
                    tiempoPromAtencion += tiempo
                    listaclientesAtendidos = listaclientesAtendidos.siguiente  
                if clientesAtendidos > 0:
                    tiempoPromAtencion = tiempoPromAtencion/clientesAtendidos
                tiempoPromAtencion = self.convertirTiempo(tiempoPromAtencion)
                tiempoMinAtencion = self.convertirTiempo(tiempoMinAtencion)
                tiempoMaxAtencion = self.convertirTiempo(tiempoMaxAtencion)
                graficar.escritorio(numero, listaEscritoriosActivos.dato.getIdentificacionEscritorio(), listaEscritoriosActivos.dato.getNombreEncargado(), tiempoMinAtencion, tiempoPromAtencion, tiempoMaxAtencion, clientesAtendidos)
                listaEscritoriosActivos = listaEscritoriosActivos.siguiente 

    def convertirTiempo(self, tiempo):
        tiempo = str(round(float(tiempo), 2))
        minuto = int(tiempo[:tiempo.index(".")])
        segundo = int(tiempo[tiempo.index(".")+1:])
        if segundo > 0 and segundo < 10: segundo = segundo*10
        hora = int((minuto-(minuto%60))/60)
        minuto = minuto%60 + int(segundo/60)
        segundo = segundo%60
        tiempo = ""
        if hora == 1: tiempo += str(int(hora))+" hora "
        elif hora > 1: tiempo += str(int(hora))+" horas "
        if minuto == 1: tiempo += str(int(minuto))+" minuto "
        elif minuto > 1: tiempo += str(int(minuto))+" minutos "
        if segundo == 1: tiempo += str(int(segundo))+" segundo"
        if segundo > 1: tiempo += str(int(segundo))+" segundos"
        if tiempo == "": return "0"
        else: return tiempo