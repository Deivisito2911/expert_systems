import customtkinter as ctk
import interfaz.insertarbase as insertar_base
import interfaz.guardarbase as guardar_base
import interfaz.consultarbase as consultar_base


class Interfaz(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.title('Sistema Experto UDO 2024')
        self.resizable(width=False, height=False)

        # Configuración de colores y temas
        ctk.set_appearance_mode("light")  # Modo claro
        ctk.set_default_color_theme("green")  # Tema verde

        # Fondo degradado
        self.configure(fg_color=("white", "#d9f5db"))  # Gradiente simulado (no animado)

        # Cabecera
        self.lbl_base = ctk.CTkLabel(self, text="Sistema Experto UDO 2024", font=("Helvetica", 28, "bold"))
        self.lbl_base.pack(pady=20)

        # Botones principales con estilo
        button_style = {
            "width": 300,
            "height": 50,
            "corner_radius": 10,
            "fg_color": "#4CAF50",  # Verde oscuro
            "hover_color": "#388E3C",  # Más oscuro al pasar el mouse
            "text_color": "white",
            "font": ("Helvetica", 16, "bold"),
        }

        self.txt_insertar = ctk.CTkButton(
            self,
            text="Insertar / Visualizar Filum",
            command=insertar_base.InsertarBase,
            **button_style
        )
        self.txt_insertar.pack(pady=10)

        self.txt_consultar = ctk.CTkButton(
            self,
            text="Consultar Filum",
            command=consultar_base.ConsultarBase,
            **button_style
        )
        self.txt_consultar.pack(pady=10)

        self.txt_guardar = ctk.CTkButton(
            self,
            text="Cargar / Guardar",
            command=guardar_base.GuardarBase,
            **button_style
        )
        self.txt_guardar.pack(pady=10)

        # Botón de salida
        self.quit = ctk.CTkButton(
            self,
            text="Salir del sistema",
            fg_color="#D32F2F",  # Rojo oscuro
            hover_color="#B71C1C",  # Más oscuro al pasar el mouse
            font=("Helvetica", 16, "bold"),
            command=self.destroy
        )
        self.quit.pack(pady=20)


# Inicialización de la interfaz
if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()
