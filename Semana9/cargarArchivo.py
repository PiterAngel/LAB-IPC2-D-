import xml.etree.ElementTree as ET
from listaEnlazada import listaEnlazada
from modeloEmpresa import Empresa
from modeloPuntoAtencion import PuntoAtencion
from modeloEscritorio import Escritorio
from modeloTransaccion import Transaccion
from modeloCliente import Cliente

class CargarArchivo:

    def __init__(self, listaEmpresas):
        self.listaEmpresas = listaEmpresas

    def leerArchivoConfiguracionSistema(self, ruta): 
        archivo_xml = ET.parse(ruta)
        empresas = archivo_xml.getroot()
  
        for empresa in empresas:
            listaPuntosAtencion = listaEnlazada()
            listaTransacciones = listaEnlazada()
            idEmpresa = empresa.attrib['id']
            nombreEmpresa = empresa.find('nombre').text
            abreviaturaEmpresa = empresa.find('abreviatura').text
            if self.listaEmpresas.buscarId(idEmpresa) == None:
                for puntosDeAtencion in empresa.findall('listaPuntosAtencion'):
                    for puntoDeAtencion in puntosDeAtencion:
                        idPuntoAtencion = puntoDeAtencion.attrib['id']
                        nombrePuntoServicio = puntoDeAtencion.find('nombre').text
                        direccionPuntoServicio = puntoDeAtencion.find('direccion').text
                        for escritorios in puntoDeAtencion.findall('listaEscritorios'):
                            listaEscritorios = listaEnlazada()
                            for escritorio in escritorios:
                                idEscritorio = escritorio.attrib['id']
                                identificacion = escritorio.find('identificacion').text
                                nombreEncargado = escritorio.find('encargado').text
                                nuevoEscritorio = Escritorio(idEscritorio, identificacion, nombreEncargado, False, listaEnlazada())
                                listaEscritorios.insertar(nuevoEscritorio)
                        nuevoPuntoAtencion = PuntoAtencion(idPuntoAtencion, nombrePuntoServicio, direccionPuntoServicio, listaEscritorios, listaEnlazada(), listaEnlazada())
                        listaPuntosAtencion.insertar(nuevoPuntoAtencion)
                for transacciones in empresa.findall('listaTransacciones'):
                    for transaccion in transacciones:
                        idTransaccion = transaccion.attrib['id']
                        nombreTransaccion = transaccion.find('nombre').text
                        tiempoAtencion = int(transaccion.find('tiempoAtencion').text)
                        nuevaTransaccion = Transaccion(id=idTransaccion, nombre=nombreTransaccion, tiempo=tiempoAtencion)
                        listaTransacciones.insertar(nuevaTransaccion)
                nuevaEmpresa = Empresa(idEmpresa, nombreEmpresa, abreviaturaEmpresa, listaPuntosAtencion, listaTransacciones)
                self.listaEmpresas.insertar(nuevaEmpresa)     

    def leerArchivoConfiguracionInicial(self, ruta):
        archivo_xml = ET.parse(ruta)
        estadoInicial = archivo_xml.getroot()

        for configInicial in estadoInicial:
            id = configInicial.attrib['id']
            idEmpresa = configInicial.attrib['idEmpresa']     
            idPunto = configInicial.attrib['idPunto']
            empresa = self.listaEmpresas.buscarId(idEmpresa)
            listaTransaccionesEmpresa = empresa.dato.getTransacciones()
            listaPuntos = empresa.dato.getPuntosDeAtencion()
            punto = listaPuntos.buscarId(idPunto)
            listaEscritorios = punto.dato.getEscritorios()
            listaEscritoriosActivos = punto.dato.getEscritoriosActivos()
            for escritoriosActivos in configInicial.findall('escritoriosActivos'):
                for escritorio in escritoriosActivos:
                    idEscritorio = escritorio.attrib['idEscritorio']
                    escritorio = listaEscritorios.buscarId(idEscritorio)
                    listaEscritoriosActivos.insertar(escritorio.dato)
                    escritorio.dato.setEstado(True)
            for clientes in configInicial.findall('listadoClientes'):  
                for cliente in clientes:
                    listaClientes = punto.dato.getClientes()
                    listaClientesEnPunto = punto.dato.getClientes()
                    punto.dato.setTurnoEnPunto()
                    dpiCliente = cliente.attrib['dpi']
                    nombreCliente = cliente.find('nombre').text
                    nuevoCliente = Cliente(dpiCliente, nombreCliente, listaEnlazada(), 0, 0)
                    listaTransaccionesCliente = nuevoCliente.getTransacciones()
                    for listadoTransacciones in cliente.findall('listadoTransacciones'):
                        for transaccion in listadoTransacciones:
                            idTransaccion = transaccion.attrib['idTransaccion']
                            cantidad = int(transaccion.attrib['cantidad'])
                            nuevaTransaccion = Transaccion(id=idTransaccion, cantidad=cantidad)
                            listaTransaccionesCliente.insertar(nuevaTransaccion)
                    tiempoEnAtencion = 0
                    listaTransaccionesCliente = listaTransaccionesCliente.valores()
                    while listaTransaccionesCliente != None:
                        transaccion = listaTransaccionesEmpresa.buscarId(listaTransaccionesCliente.dato.getId())
                        tiempoEnAtencion += transaccion.dato.getTiempo()*listaTransaccionesCliente.dato.getCantidad()
                        listaTransaccionesCliente = listaTransaccionesCliente.siguiente
                    nuevoCliente.setTiempoEnAtencion(tiempoEnAtencion) 
                    listaClientes.insertar(nuevoCliente)
                    ######################################################################
                    self.calcularTiempoEnEspera(listaEscritoriosActivos, listaClientesEnPunto, listaClientes)
                
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