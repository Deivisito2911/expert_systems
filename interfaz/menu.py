import customtkinter as ctk
import interfaz.insertarbase as insertar_base
import interfaz.guardarbase as guardar_base
import interfaz.consultarbase as consultar_base


class Interfaz(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.title('Sistema Experto para Selección de Agares')
        self.resizable(width=False, height=False)

        # Configuración de colores y fuentes globales
        ctk.set_appearance_mode("light")  # Modo claro
        ctk.set_default_color_theme("blue")  # Tema azul (similar a Facebook)

        # Cabecera
        self.lbl_base = ctk.CTkLabel(self, text="Sistema Experto Agares", font=("Helvetica", 28, "bold"))
        self.lbl_base.pack(pady=20)

        # Botones principales con estilo
        self.txt_insertar = ctk.CTkButton(
            self,
            text="Insertar / Visualizar",
            width=300,
            height=50,
            command=insertar_base.InsertarBase
        )
        self.txt_insertar.pack(pady=10)

        self.txt_consultar = ctk.CTkButton(
            self,
            text="Consultar",
            width=300,
            height=50,
            command=consultar_base.ConsultarBase
        )
        self.txt_consultar.pack(pady=10)

        self.txt_guardar = ctk.CTkButton(
            self,
            text="Cargar / Guardar",
            width=300,
            height=50,
            command=guardar_base.GuardarBase
        )
        self.txt_guardar.pack(pady=10)

        # Botón de salida
        self.quit = ctk.CTkButton(
            self,
            text="Salir",
            width=300,
            height=50,
            fg_color="red",
            hover_color="#ff6666",
            command=self.destroy
        )
        self.quit.pack(pady=20)


# Inicialización de la interfaz
if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()
