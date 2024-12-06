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

        # Configuración de colores y temas
        ctk.set_appearance_mode("light")  # Modo claro
        ctk.set_default_color_theme("green")  # Tema verde

        # Fondo principal
        self.configure(fg_color="#d9f5db")  # Color uniforme sin bordes blancos

        # Cabecera centrada
        self.lbl_base = ctk.CTkLabel(
            self,
            text="Sistema Experto UDO 2024",
            font=("Helvetica", 28, "bold"),
            text_color="#4CAF50",
        )
        self.lbl_base.pack(pady=10)  # Centrado con padding superior

        # Variables para el sidebar
        self.sidebar_open = False
        self.sidebar_width = 200

        # Contenedor del sidebar sin bordes blancos
        self.sidebar_frame = ctk.CTkFrame(self, width=self.sidebar_width, fg_color="#4CAF50", corner_radius=0)
        self.sidebar_frame.place(x=-self.sidebar_width, y=0, relheight=1)

        # Botones del sidebar con iconos ASCII
        self.add_sidebar_buttons()

        # Botón para abrir/cerrar el sidebar
        self.menu_button = ctk.CTkButton(
            self,
            text="☰",  # Icono de menú
            width=50,
            height=50,
            fg_color="#D32F2F",
            hover_color="#B71C1C",
            font=("Helvetica", 20, "bold"),
            text_color="white",
            corner_radius=10,  # Ajuste para evitar esquinas blancas
            command=self.toggle_sidebar
        )
        self.menu_button.place(x=10, y=10)

        # Configurar evento de cierre de ventana con animación
        self.protocol("WM_DELETE_WINDOW", self.animate_close_window)

    def add_sidebar_buttons(self):
        """Añadir botones con iconos ASCII al sidebar."""
        button_style = {
            "width": 50,
            "height": 50,
            "corner_radius": 10,
            "fg_color": "#4CAF50",
            "hover_color": "#388E3C",
            "text_color": "white",
            "font": ("Courier", 20, "bold"),
        }

        self.btn_insertar = ctk.CTkButton(
            self.sidebar_frame,
            text="📥",  # Icono ASCII para insertar
            command=insertar_base.InsertarBase,
            **button_style
        )
        self.btn_insertar.pack(pady=(70, 10), padx=10, anchor="w")  # Alineado a la izquierda

        self.btn_consultar = ctk.CTkButton(
            self.sidebar_frame,
            text="🔍",  # Icono ASCII para consultar
            command=consultar_base.ConsultarBase,
            **button_style
        )
        self.btn_consultar.pack(pady=10, padx=10, anchor="w")  # Alineado a la izquierda

        self.btn_guardar = ctk.CTkButton(
            self.sidebar_frame,
            text="💾",  # Icono ASCII para guardar
            command=guardar_base.GuardarBase,
            **button_style
        )
        self.btn_guardar.pack(pady=10, padx=10, anchor="w")  # Alineado a la izquierda

        # Botón "Salir" ajustado y movido hacia abajo
        self.btn_salir = ctk.CTkButton(
            self.sidebar_frame,
            text="❌",  # Icono ASCII para salir
            command=self.destroy,
            width=50,  # Tamaño reducido
            height=50,
            corner_radius=10,
            fg_color="#D32F2F",  # Rojo oscuro específico para este botón
            hover_color="#B71C1C",
            text_color="white",
            font=("Courier", 20, "bold"),
        )
        self.btn_salir.pack(side="bottom", pady=(20, 20), padx=10, anchor="w")  # Alineado a la izquierda y al fondo

    def toggle_sidebar(self):
        """Abrir/cerrar el sidebar con animación."""
        if self.sidebar_open:
            self.animate_sidebar(-self.sidebar_width)
            self.sidebar_open = False
        else:
            self.animate_sidebar(0)
            self.sidebar_open = True

    def animate_sidebar(self, target_x):
        """Animar el movimiento del sidebar."""
        step = 20 if target_x > self.sidebar_frame.winfo_x() else -20
        for x in range(self.sidebar_frame.winfo_x(), target_x, step):
            self.sidebar_frame.place(x=x, y=0)
            self.sidebar_frame.update()
        self.sidebar_frame.place(x=target_x, y=0)

    def animate_close_window(self):
        """Animar el cierre de la ventana."""
        for size in range(800, 0, -20):  # Reducir tamaño gradualmente
            self.geometry(f"{size}x{int(size * 0.625)}")
            self.update()
        self.destroy()


# Inicialización de la interfaz
if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()
