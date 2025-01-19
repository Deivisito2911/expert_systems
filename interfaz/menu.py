import customtkinter as ctk
import interfaz.insertarbase as insertar_base
import interfaz.guardarbase as guardar_base
import interfaz.consultarbase as consultar_base


class Interfaz(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('800x500')
        self.title('Sistema Experto UDO 2024')
        self.resizable(width=False, height=False)
        self.iconbitmap(r"interfaz\icon.ico")  # Solucionado el problema de la ruta

        # Cabecera simple
        self.lbl_base = ctk.CTkLabel(
            self,
            text="Sistema Experto UDO 2024",
            font=("Helvetica", 20, "bold"),
        )
        self.lbl_base.pack(pady=10)

        # Contenedor del área de contenido principal
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.8)

        # Contenedor de botones del menú principal
        self.menu_buttons_frame = ctk.CTkFrame(self)
        self.menu_buttons_frame.pack(pady=20)

        # Botones principales
        self.btn_insertar = self.create_button(
            self.menu_buttons_frame, "Insertar", self.show_insertar_base
        )
        self.btn_insertar.pack(side="left", padx=20)

        self.btn_consultar = self.create_button(
            self.menu_buttons_frame, "Consultar", self.show_consultar_base
        )
        self.btn_consultar.pack(side="left", padx=20)

        self.btn_guardar = self.create_button(
            self.menu_buttons_frame, "Guardar", self.show_guardar_base
        )
        self.btn_guardar.pack(side="left", padx=20)

        self.btn_salir = self.create_button(self, "Salir", self.destroy)
        self.btn_salir.pack(side="bottom", pady=10)

        # Botón para volver al menú principal
        self.btn_volver = None  # Se crea dinámicamente

    def create_button(self, parent, text, command):
        """Crea un botón con estilo uniforme."""
        return ctk.CTkButton(
            parent,
            text=text,
            command=command,
            fg_color="#009268",
            hover_color="#007a5f",
            text_color="white",
            font=("Helvetica", 12, "bold"),
        )

    def show_insertar_base(self):
        self.show_option(insertar_base.InsertarBase)

    def show_consultar_base(self):
        self.show_option(consultar_base.ConsultarBase)

    def show_guardar_base(self):
        self.show_option(guardar_base.GuardarBase)

    def show_option(self, FrameClass):
        """Muestra la vista correspondiente y oculta el menú principal."""
        self.menu_buttons_frame.pack_forget()  # Ocultar botones principales

        # Limpiar contenido anterior en el frame principal
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Mostrar el contenido de la opción seleccionada
        content = FrameClass(self.content_frame)
        content.pack(fill="both", expand=True)

        # Crear botón de volver
        if self.btn_volver is None:
            self.btn_volver = self.create_button(
                self,
                "← Volver",
                self.volver_al_menu,
            )
        self.btn_volver.pack(side="top", pady=10)

    def volver_al_menu(self):
        """Vuelve al menú principal y oculta el contenido actual."""
        # Ocultar botón de volver
        if self.btn_volver:
            self.btn_volver.pack_forget()

        # Limpiar contenido actual
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Mostrar botones del menú principal
        self.menu_buttons_frame.pack(pady=20)


# Inicialización de la interfaz
if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()
