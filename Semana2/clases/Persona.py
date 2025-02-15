class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, yo soy {self.nombre}, tengo {self.edad} años "

    def despedir(self):
        return "Adios"
