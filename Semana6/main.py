import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import xml.etree.ElementTree as ET
import graphviz
from PIL import Image, ImageTk
import os
from estructuras import Pila, Cola

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Hospital - Gestión de Pacientes")
        self.root.geometry("500x500")

        self.pila_urgencias = Pila()
        self.cola_consultas = Cola()

        self.crear_interfaz()

    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Botones
        ttk.Button(main_frame, text="Cargar XML", command=self.cargar_xml).grid(row=0, column=0, pady=5)
        ttk.Button(main_frame, text="Visualizar Estructuras", command=self.visualizar_estructuras).grid(row=0, column=1, pady=5)

        # Frame para mostrar la imagen
        self.frame_imagen = ttk.Frame(main_frame)
        self.frame_imagen.grid(row=1, column=0, columnspan=2, pady=10)

        # Labels para mostrar información
        self.label_info = ttk.Label(main_frame, text="")
        self.label_info.grid(row=2, column=0, columnspan=2)

    def cargar_xml(self):
        archivos = filedialog.askopenfilenames(
            title="Seleccionar archivos XML",
            filetypes=[("XML files", "*.xml")]
        )

        for archivo in archivos:
            try:
                tree = ET.parse(archivo)
                root = tree.getroot()

                for paciente in root.findall('paciente'):
                    tipo = paciente.find('tipo').text
                    datos = {
                        'nombre': paciente.find('nombre').text,
                        'edad': paciente.find('edad').text,
                        'tipo': tipo
                    }

                    if tipo == 'urgencia':
                        self.pila_urgencias.apilar(datos)
                    else:
                        self.cola_consultas.encolar(datos)

                messagebox.showinfo("Éxito", f"Archivo {os.path.basename(archivo)} cargado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar el archivo: {str(e)}")

    def visualizar_estructuras(self):
        dot = graphviz.Digraph(comment='Estructuras de Datos Hospital')
        dot.attr(rankdir='LR')

        # Subgrafo para la Pila
        with dot.subgraph(name='cluster_0') as c:
            c.attr(label='Pila de Urgencias')

            actual = self.pila_urgencias.tope
            anterior_id = None

            while actual:
                nodo_id = str(id(actual))
                c.node(nodo_id, f"{actual.paciente['nombre']}\n{actual.paciente['edad']} años")

                if anterior_id:
                    c.edge(anterior_id, nodo_id)
                anterior_id = nodo_id
                actual = actual.siguiente

        # Subgrafo para la Cola
        with dot.subgraph(name='cluster_1') as c:
            c.attr(label='Cola de Consultas')

            actual = self.cola_consultas.frente
            anterior_id = None

            while actual:
                nodo_id = str(id(actual))
                c.node(nodo_id, f"{actual.paciente['nombre']}\n{actual.paciente['edad']} años")

                if anterior_id:
                    c.edge(anterior_id, nodo_id)
                anterior_id = nodo_id
                actual = actual.siguiente

        # Guardar y mostrar el grafo
        dot.render('estructuras_hospital', format='png', cleanup=True)

        # Mostrar la imagen en la interfaz
        imagen = Image.open('estructuras_hospital.png')
        # Redimensionar la imagen si es necesario
        imagen = imagen.resize((800, 600), Image.LANCZOS)
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Limpiar frame_imagen
        for widget in self.frame_imagen.winfo_children():
            widget.destroy()

        # Mostrar nueva imagen
        label_imagen = ttk.Label(self.frame_imagen, image=imagen_tk)
        label_imagen.image = imagen_tk  # Mantener referencia
        label_imagen.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()