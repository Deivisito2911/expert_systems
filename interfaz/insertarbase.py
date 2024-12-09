import customtkinter as ctk  # Usar customtkinter en lugar de tkinter
from tkinter import ttk
import acciones


class InsertarBase(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.configure(fg_color="#d9f5db")  # Fondo igual al principal

        # Configuración de la ventana emergente (Toplevel)
        root = ctk.CTkToplevel()
        root.geometry('380x450')
        root.title('Insertar un Filum')
        root.resizable(width=False, height=False)

        self.pack()

        # Etiqueta de título
        self.lbl_base = ctk.CTkLabel(self, text="Insertar un Filum", font=("Helvetica", 24))
        self.lbl_base.pack(side="top", pady=10)

        # Árbol de vista para entradas
        self.entradas = ttk.Treeview(self)
        self.entradas.pack(side="top")
        self.entradas.tag_bind("tag_select", "<<TreeviewSelect>>", self.item_selected)
        self.fill_base_tree_view()

        # Etiqueta para nombre del Filum
        self.lbl_entry = ctk.CTkLabel(self, text="Nombre del Filum", font=("Helvetica", 12))
        self.lbl_entry.pack(side="top")

        # Entrada para nombre del Filum
        self.txt_entry = ctk.CTkEntry(self, width=250)
        self.txt_entry.pack(side="top", padx=5, pady=5)

        # Etiqueta para característica
        self.lbl_prop = ctk.CTkLabel(self, text="Característica", font=("Helvetica", 12))
        self.lbl_prop.pack(side="top")

        # Entrada para característica
        self.txt_prop = ctk.CTkEntry(self, width=250)
        self.txt_prop.pack(side="top", padx=5, pady=5)

        # Estilo de los botones
        button_style = {
            "width": 50,
            "height": 40,
            "corner_radius": 10,
            "hover_color": "#388E3C",  # Definir hover_color solo en el diccionario
            "text_color": "white",
            "font": ("Helvetica", 12, "bold"),
        }

        # Botón para agregar propiedad
        self.btn_insertar = ctk.CTkButton(self, text="Agregar", command=self.add_propiedad, **button_style)
        self.btn_insertar.pack(side="top", padx=5, pady=5)

        # Botón de salida
        self.quit = ctk.CTkButton(self, text="Salir", fg_color="#D32F2F", command=self.master.destroy, **button_style)
        self.quit.pack(side="bottom", padx=5, pady=5)

    def fill_base_tree_view(self):
        self.entradas.delete(*self.entradas.get_children())
        base = self.entradas.insert("", "end", text="Base")  # Usar "end" en lugar de ""
        base_entries = acciones.get_base_entries()
        for entry in base_entries:
            nombre = self.entradas.insert(base, "end", text=entry.name, tags=("tag_select",))  # Usar "end" en lugar de ""
            for prop in entry.properties:
                self.entradas.insert(nombre, "end", text=prop.name)  # Usar "end" en lugar de ""

    def add_propiedad(self):
        entrada = self.txt_entry.get()
        propiedad = self.txt_prop.get()

        acciones.insertar(entrada, propiedad)
        self.txt_prop.delete(0, "end")
        self.fill_base_tree_view()

    def item_selected(self, event):
        id = event.widget.focus()
        text = self.entradas.item(id)["text"]
        self.txt_entry.delete(0, ctk.END)
        self.txt_entry.insert(0, text)
