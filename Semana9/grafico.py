import os

class Grafico:

    def __init__(self):
        self.graphviz = ""

    def encabezado(self, nombreEmpresa):
        self.graphviz += 'digraph {\n    ranksep="0.1"\n    graph[pad="0.5"];\n    node [fontname="Arial" shape="plain"]\n    edge[dir="none" style="invisible"]\n'
        self.graphviz += '    NombreEmpresa[label="'+nombreEmpresa+'" fontcolor=blue]\n'

    def puntoAtencion(self, nombrePunto, activos, inactivos, clientesE, clientesA, tiempoMinimoE, tiempoPromedioE, tiempoMaximoE, tiempoMinimoA, tiempoPromedioA, tiempoMaximoA):
        self.graphviz += '    NombrePunto [label="\n'+nombrePunto+'" fontcolor=blue];\n'
        self.graphviz += '    TablaPunto [label=<<table border="0" cellborder="0" cellspacing="5">\n'
        self.graphviz += '    <tr><td>Escritorios</td><td>Clientes</td><td>Tiempo de Espera</td><td>Tiempo de Atencion</td></tr>\n'
        self.graphviz += '    <tr><td><table border="0" cellborder="1" cellspacing="0">\n'
        self.graphviz += '        <tr><td>Activos</td><td>Inactivos</td></tr>\n'
        self.graphviz += '        <tr><td>'+str(activos)+'</td><td>'+str(inactivos)+'</td>'
        self.graphviz += '    </tr></table></td><td><table border="0" cellborder="1" cellspacing="0">\n'
        self.graphviz += '        <tr><td>En espera</td><td>Atendidos</td></tr>\n'
        self.graphviz += '        <tr><td>'+str(clientesE)+'</td><td>'+str(clientesA)+'</td></tr></table></td>\n'
        self.graphviz += '    <td><table border="0" cellborder="1" cellspacing="0">\n'
        self.graphviz += '        <tr><td>Minimo</td><td>Promedio</td><td>Maximo</td></tr>\n'
        self.graphviz += '        <tr><td>'+tiempoMinimoE+'</td><td>'+tiempoPromedioE+'</td><td>'+tiempoMaximoE+'</td>\n'
        self.graphviz += '    </tr></table></td><td><table border="0" cellborder="1" cellspacing="0">\n'
        self.graphviz += '        <tr><td>Minimo</td><td>Promedio</td><td>Maximo</td></tr>\n'
        self.graphviz += '        <tr><td>'+tiempoMinimoA+'</td><td>'+tiempoPromedioA+'</td><td>'+tiempoMaximoA+'</td>\n'
        self.graphviz += '    </tr></table></td></tr></table>>];\n'
        self.graphviz += '    NombreEmpresa->NombrePunto\n'
        self.graphviz += '    NombrePunto->TablaPunto\n'
        self.graphviz += '    saltoLinea[label="." fontcolor=white]\n'
        self.graphviz += '    TablaPunto->saltoLinea\n'

    def escritorio(self, numero, identificacionEscritorio, nombreEncargado, tiempoMinimo, tiempoPromedio, tiempoMaximo, atendidos):
        if numero == 1: nodo = "saltoLinea" 
        else: nodo = "TablaEscritorio"+str(numero-1)
        self.graphviz += '    TablaEscritorio'+str(numero)+' [label=<<table border="0" cellborder="0" cellspacing="5">\n'
        self.graphviz += '        <tr><td><font color="blue">ID: '+identificacionEscritorio+'    Encargado: '+nombreEncargado+'</font></td></tr>\n'
        self.graphviz += '    <tr><td><table border="0" cellborder="0" cellspacing="5">\n'
        self.graphviz += '        <tr><td>Tiempo Atencion</td><td>Clientes</td></tr>\n'
        self.graphviz += '    <tr><td><table border="0" cellborder="1" cellspacing="0">\n'
        self.graphviz += '        <tr><td>Minimo</td><td>Promedio</td><td>Maximo</td></tr>\n'
        self.graphviz += '        <tr><td>'+tiempoMinimo+'</td><td>'+tiempoPromedio+'</td><td>'+tiempoMaximo+'</td>\n'
        self.graphviz += '    </tr></table></td><td><table border="0" cellborder="1" cellspacing="0">\n'
        self.graphviz += '        <tr><td>Atendidos</td></tr>\n'
        self.graphviz += '        <tr><td>'+str(atendidos)+'</td>\n'
        self.graphviz += '    </tr></table></td></tr></table></td></tr></table>>];\n'
        self.graphviz += '    '+nodo+'->TablaEscritorio'+str(numero)+'\n'
    
    def exportar(self):
        self.graphviz += "}"
        txt = 'grafica.txt'
        with open(txt, 'w') as grafica:
            grafica.write(self.graphviz)
        pdf = 'reporte.pdf'
        os.system("dot.exe -Tpdf " + txt + " -o " + pdf)