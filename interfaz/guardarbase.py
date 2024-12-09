import customtkinter as ctk
import acciones
import os

class GuardarBase(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.configure(fg_color="#d9f5db")  # Fondo igual al principal

        # Configuración de la ventana emergente (Toplevel)
        root = ctk.CTkToplevel()
        root.geometry('400x220')
        root.title('Guardar Base de Conocimientos')
        root.resizable(width=False, height=False)

        self.pack()

        # Etiqueta de título
        self.lbl_base = ctk.CTkLabel(self, text="Cargar/Guardar Base", font=("Helvetica", 24))
        self.lbl_base.pack(side="top", pady=10)

        # Etiqueta para el nombre del archivo
        self.lbl_file = ctk.CTkLabel(self, text="Nombre del archivo json: ", font=("Helvetica", 12))
        self.lbl_file.pack(side="top")
        
        # Campo de texto para ingresar el nombre del archivo
        self.txt_file = ctk.CTkEntry(self, width=250)
        self.txt_file.pack(side="top", padx=5, pady=5)

        # Estilo de los botones
        button_style = {
            "width": 50,
            "height": 40,
            "corner_radius": 10,
            "hover_color": "#388E3C",  # Definir hover_color solo en el diccionario
            "text_color": "white",
            "font": ("Helvetica", 12, "bold"),
        }

        # Crear los botones con el estilo
        self.btn_cargar = ctk.CTkButton(self, text="Cargar", command=self.cargar_base_json, **button_style)
        self.btn_cargar.pack(side="top", padx=5, pady=5)

        self.btn_guardar = ctk.CTkButton(self, text="Guardar", command=self.guardar_base_json, **button_style)
        self.btn_guardar.pack(side="top", padx=5, pady=5)

        self.quit = ctk.CTkButton(self, text="Cerrar", fg_color="#D32F2F",  # El argumento fg_color ahora está directamente aquí
                                  command=self.master.destroy, **button_style)
        self.quit.pack(side="bottom", padx=5, pady=5)

    def guardar_base_json(self):
        subcarpeta = "Base_De_Conocimiento"  # Nombre de la carpeta
        if not os.path.exists(subcarpeta):  # Si no existe la carpeta, la crea
            os.makedirs(subcarpeta)
        ruta_completa = os.path.join(subcarpeta, self.txt_file.get())  # Ruta completa de la carpeta
        print(f"Guardando archivo en: {ruta_completa}")
        acciones.guardar(ruta_completa)

    def cargar_base_json(self):
        subcarpeta = "Base_De_Conocimiento"
        ruta_completa = os.path.join(subcarpeta, self.txt_file.get())
        print(f"Cargando archivo desde: {ruta_completa}")  # Mostrar la ruta completa en la consola
        acciones.cargar(ruta_completa)
        self.master.destroy()

# Para ejecutar la ventana de ejemplo, debe ser llamada desde un contenedor principal (parent).
