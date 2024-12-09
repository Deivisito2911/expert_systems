import customtkinter as ctk
import acciones
import os

class GuardarBase(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.pack()
        self.pack(padx=10, pady=50)

        # Etiqueta de título
        self.lbl_base = ctk.CTkLabel(self, text="Cargar/Guardar Base", font=("Helvetica", 16))
        self.lbl_base.pack(pady=20)

        # Etiqueta para el nombre del archivo
        self.lbl_file = ctk.CTkLabel(self, text="Nombre del archivo json: ")
        self.lbl_file.pack()

        # Campo de texto para ingresar el nombre del archivo
        self.txt_file = ctk.CTkEntry(self, width=250)
        self.txt_file.pack(pady=10)

        # Botones para cargar y guardar
        self.btn_cargar = ctk.CTkButton(self, text="Cargar", command=self.cargar_base_json)
        self.btn_cargar.pack(pady=15)

        self.btn_guardar = ctk.CTkButton(self, text="Guardar", command=self.guardar_base_json)
        self.btn_guardar.pack(pady=15)

    def guardar_base_json(self):
        subcarpeta = "Base_De_Conocimiento"
        if not os.path.exists(subcarpeta):  # Si no existe la carpeta, la crea
            os.makedirs(subcarpeta)
        ruta_completa = os.path.join(subcarpeta, self.txt_file.get())
        print(f"Guardando archivo en: {ruta_completa}")
        acciones.guardar(ruta_completa)

    def cargar_base_json(self):
        subcarpeta = "Base_De_Conocimiento"
        ruta_completa = os.path.join(subcarpeta, self.txt_file.get())
        print(f"Cargando archivo desde: {ruta_completa}")
        acciones.cargar(ruta_completa)
        self.master.destroy()
