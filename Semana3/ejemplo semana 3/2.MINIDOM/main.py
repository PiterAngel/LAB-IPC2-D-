from xml.dom import minidom

documento = minidom.parse("C:\\Users\\Piter\\Desktop\\USAC\\PRIMER SEMESTRE 2025\\AUXILIATURA\\CLASES\\GIT\\LAB-IPC2-D-\\Semana3\\ejemplo semana 3\\2.MINIDOM\\empleados.xml")


# Nodo raiz

empresa = documento.documentElement

# Mostrar los departamentos y valores
departamentos = empresa.getElementsByTagName("departamento")

for departamento in departamentos:
    nombre_departamento =departamento.getAttribute("departamento")
    print("Departamento: ", nombre_departamento)

    empleados = departamento.getElementsByTagName("empleado")
    for empleado in empleados:
        id_empleado = empleado.getAttribute("id")
        nombre = empleado.getElementsByTagName("nombre")[0].firstChild.data
        salario = empleado.getElementsByTagName("salario")[0].firstChild.data
        print(f"\t ID: {id_empleado}, Nombre: {nombre}, Salario: {salario}" )