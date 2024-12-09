import tkinter.messagebox as messagebox
import customtkinter as ctk
from experto_general.response import Response
from acciones import engine

class ConsultarBase(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        # Configuremos el fondo de esta ventana igual que en el principal
        self.configure(fg_color="#d9f5db")  # Color de fondo similar al principal

        # Etiqueta con la pregunta
        self.lbl_question = ctk.CTkLabel(self, text="Característica", font=("Helvetica", 28))
        self.lbl_question.pack(side="top", pady=20)

        # Estilo de los botones, consistente con la ventana principal
        button_style = {
            "width": 20,
            "height": 30,
            "corner_radius": 10,
            "fg_color": "#4CAF50",
            "hover_color": "#388E3C",
            "text_color": "white",
            "font": ("Helvetica", 24, "bold"),
        }

        # Botones "Sí" y "No"
        self.btn_yes = ctk.CTkButton(self, text="Sí", command=self._send_yes, **button_style)
        self.btn_yes.pack(side="left", padx=30, pady=5)

        self.btn_no = ctk.CTkButton(self, text="No", command=self._send_no, **button_style)
        self.btn_no.pack(side="right", padx=5, pady=5)

        # Empacar el marco
        self.pack(padx=20, pady=20)

        # Iniciar las preguntas
        self.questions = engine.generate()
        self._get_question(Response.NO)

    def _send_yes(self):
        self._get_question(Response.YES)

    def _send_no(self):
        self._get_question(Response.NO)

    def _get_question(self, response: Response):
        try:
            engine.set_response(response)
            question = next(self.questions)

            if question is not None:
                self.lbl_question.configure(text=f"¿{question.name}?")  # Cambiar 'config' por 'configure'
            else:
                self._finished()

        except StopIteration:
            self._finished()

    def _finished(self):
        if engine.result is None:
            messagebox.showerror("Error", "No se encontró ningún filum que cumpla con las características dadas.")
        else:
            reason = f"Características coincidentes:\n"
            for prop in engine.result.properties:
                reason += f"- {prop.name}\n"
            messagebox.showinfo("Filum encontrado",
                                f"El filum es: {engine.result.name}\n\n{engine.result.description}\n\n" + reason)
        self.destroy()
