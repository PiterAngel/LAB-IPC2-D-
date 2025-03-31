import tkinter as tk
from tkinter import ttk, messagebox
import re

class FormularioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Registro")
        self.root.geometry("500x600")

        # Estilo
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 11))
        style.configure('TEntry', font=('Arial', 11))
        style.configure('TButton', font=('Arial', 11))

        # Frame principal
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Variables
        self.nombre_var = tk.StringVar()
        self.apellido_var = tk.StringVar()
        self.telefono_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.direccion_var = tk.StringVar()

        # Expresiones regulares
        self.regex_patterns = {
            'nombre': r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s]{2,30}$',
            'apellido': r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s]{2,30}$',
            'telefono': r'^\d{4}-?\d{4}$',
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'direccion': r'^[A-Za-z0-9\s,.-]{10,100}$'
        }

        # Crear campos
        self.crear_campo("Nombre:", self.nombre_var, 0)
        self.crear_campo("Apellido:", self.apellido_var, 1)
        self.crear_campo("Teléfono:", self.telefono_var, 2)
        self.crear_campo("Email:", self.email_var, 3)
        self.crear_campo("Dirección:", self.direccion_var, 4)

        # Botón de registro
        ttk.Button(main_frame, text="Registrar", command=self.validar_formulario).grid(row=5, column=0, columnspan=2, pady=20)

        # Labels para mostrar errores
        self.error_labels = {}
        for i, campo in enumerate(['nombre', 'apellido', 'telefono', 'email', 'direccion']):
            self.error_labels[campo] = ttk.Label(main_frame, text="", foreground="red", font=('Arial', 8))
            self.error_labels[campo].grid(row=i, column=2, padx=5, sticky='w')

    def crear_campo(self, label_text, variable, row):
        main_frame = self.root.winfo_children()[0]
        ttk.Label(main_frame, text=label_text).grid(row=row, column=0, padx=5, pady=5, sticky='e')
        ttk.Entry(main_frame, textvariable=variable, width=30).grid(row=row, column=1, padx=5, pady=5)

    def validar_campo(self, campo, valor, patron):
        if re.match(patron, valor):
            self.error_labels[campo].config(text="✓", foreground="green")
            return True
        else:
            self.error_labels[campo].config(text="✗ Formato inválido", foreground="red")
            return False

    def validar_formulario(self):
        campos = {
            'nombre': self.nombre_var.get(),
            'apellido': self.apellido_var.get(),
            'telefono': self.telefono_var.get(),
            'email': self.email_var.get(),
            'direccion': self.direccion_var.get()
        }

        valido = True
        for campo, valor in campos.items():
            if not self.validar_campo(campo, valor, self.regex_patterns[campo]):
                valido = False

        if valido:
            messagebox.showinfo("Éxito", "Registro completado correctamente")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Por favor, corrija los campos marcados")

    def limpiar_campos(self):
        self.nombre_var.set("")
        self.apellido_var.set("")
        self.telefono_var.set("")
        self.email_var.set("")
        self.direccion_var.set("")
        for error_label in self.error_labels.values():
            error_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioApp(root)
    root.mainloop()