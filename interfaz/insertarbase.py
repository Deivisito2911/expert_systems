import customtkinter as ctk
from tkinter import ttk
import acciones


class InsertarBase(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.pack(fill="both", expand=True)

        # Contenedor principal con dos secciones: izquierda (árbol) y derecha (campos)
        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.pack(side="left", fill="both", expand=False, padx=20, pady=80)

        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=50, pady=80)

        # Árbol de vista (lado izquierdo)
        self.lbl_base = ctk.CTkLabel(
            self.left_frame, text="Vista de la Base de Conocimientos", font=("Helvetica", 16)
        )
        self.lbl_base.pack(pady=5)

        self.entradas = ttk.Treeview(self.left_frame)
        self.entradas.pack(fill="both", expand=True, pady=10)
        self.entradas.bind("<<TreeviewSelect>>", self.item_selected)
        self.fill_base_tree_view()

        # Campos para entrada de datos (lado derecho)
        self.lbl_entry = ctk.CTkLabel(self.right_frame, text="Nombre del Filum")
        self.lbl_entry.pack(pady=10)

        self.txt_entry = ctk.CTkEntry(self.right_frame)
        self.txt_entry.pack(padx=10)

        self.lbl_prop = ctk.CTkLabel(self.right_frame, text="Característica")
        self.lbl_prop.pack(pady=5)

        self.txt_prop = ctk.CTkEntry(self.right_frame)
        self.txt_prop.pack(pady=5)

        self.btn_insertar = ctk.CTkButton(
            self.right_frame, text="Agregar", command=self.add_propiedad
        )
        self.btn_insertar.pack(pady=10)

    def fill_base_tree_view(self):
        """Rellena el árbol de vista con los datos actuales."""
        self.entradas.delete(*self.entradas.get_children())
        base = self.entradas.insert("", "end", text="Base")
        base_entries = acciones.get_base_entries()
        for entry in base_entries:
            nombre = self.entradas.insert(base, "end", text=entry.name)
            for prop in entry.properties:
                self.entradas.insert(nombre, "end", text=prop.name)

    def add_propiedad(self):
        """Agrega una nueva propiedad al filum y actualiza la vista."""
        entrada = self.txt_entry.get()
        propiedad = self.txt_prop.get()
        acciones.insertar(entrada, propiedad)
        self.txt_prop.delete(0, "end")
        self.fill_base_tree_view()

    def item_selected(self, event):
        """Maneja la selección de un elemento en el árbol."""
        id = event.widget.focus()
        text = self.entradas.item(id)["text"]
        self.txt_entry.delete(0, "end")
        self.txt_entry.insert(0, text)
