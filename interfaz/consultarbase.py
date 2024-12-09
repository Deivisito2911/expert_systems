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
        self.btn_yes.pack(side="left", padx=20, pady=50)

        self.btn_no = ctk.CTkButton(self, text="No", command=self._send_no, **button_style)
        self.btn_no.pack(side="left", padx=0, pady=50)

        # Empacar el marco
        self.pack(padx=20, pady=20)

        # Iniciar las preguntas
        self.questions = engine.generate()
        self._get_question(Response.NO)

        # Marco para mostrar los resultados
        self.result_frame = ctk.CTkFrame(self)
        self.result_frame.pack(pady=15, padx=10, fill="both", expand=True)

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
        # Limpiar cualquier mensaje previo
        if hasattr(self, "result_label"):
            self.result_label.destroy()  # Elimina el Label existente antes de crear uno nuevo

        if engine.result is None:
            # Mensaje de error si no se encontró un filum
            self.result_label = ctk.CTkLabel(
                self.result_frame,
                text="No se encontró ningún filum que cumpla con las características dadas.",
                font=("Helvetica", 14),
                text_color="red",
                wraplength=400,
            )
        else:
            # Mensaje de éxito si se encontró un filum
            reason = "Características coincidentes:\n"
            for prop in engine.result.properties:
                reason += f"- {prop.name}\n"

            # Construir el mensaje completo
            result_text = (
                f"El filum es: {engine.result.name}\n\n"
                f"{engine.result.description}\n\n"
                f"{reason}"
            )

            # Mostrar el resultado
            self.result_label = ctk.CTkLabel(
                self.result_frame,
                text=result_text,
                font=("Helvetica", 14),
                justify="left",
                wraplength=400,
            )

        # Empacar el resultado
        self.result_label.pack(pady=5, padx=5)
