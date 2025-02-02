import customtkinter as ctk
from experto_general.response import Response
from acciones import engine
from PIL import Image

class ConsultarBase(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        # Paleta de colores
        self.color_verde = "#07bb87"
        self.color_verde_hover = "#007a5f"

        self.lbl_base = ctk.CTkLabel(self, text="")
        self.lbl_base.pack(pady=10)

        # Etiqueta de la pregunta
        self.lbl_question = ctk.CTkLabel(self, text="", font=("Helvetica", 20))
        self.lbl_question.pack(pady=50)

        # Botones "Sí" y "No"
        self.btn_yes = ctk.CTkButton(
            self,
            text="Sí",
            command=lambda: self._get_question(Response.YES),
            text_color="#333333",
            fg_color=self.color_verde,
            hover_color=self.color_verde_hover,
        )
        self.btn_yes.pack(side="left", padx=100, pady=10)

        self.btn_no = ctk.CTkButton(
            self,
            text="No",
            command=lambda: self._get_question(Response.NO),
            text_color="#333333",
            fg_color=self.color_verde,
            hover_color=self.color_verde_hover,
        )
        self.btn_no.pack(side="right", padx=100, pady=10)

        # Iniciar preguntas
        self.questions = engine.generate()
        self._get_question(Response.NO)

    def _get_question(self, response: Response):
        try:
            engine.set_response(response)
            question = next(self.questions)
            if question:
                self.lbl_question.configure(text=f"¿{question.name}?")
            else:
                self._finished()
        except StopIteration:
            self._finished()

    def _finished(self):
        # Limpiar los widgets existentes
        self.lbl_question.pack_forget()
        self.btn_yes.pack_forget()
        self.btn_no.pack_forget()

        # Mostrar el resultado
        if engine.result:
            # Crear el nombre del archivo de imagen
            image_name = f"{engine.result.name}.png"  # Asume que las imágenes son PNG

            # Construir la URL de la imagen (ajusta la URL base según tu configuración)
            #image_url = f"{image_name}"  # Reemplaza con tu URL base

            try:
                # Intentar abrir la imagen desde la URL
                #image = Image.open(image_url)  # Necesita una URL válida o una ruta de archivo
                self.imagen = ctk.CTkImage(
                    light_image= Image.open(rf"interfaz\{image_name}"),
                    size=(200, 200)
                )
                self.lbl_imagen = ctk.CTkLabel(
                    self,
                    image=self.imagen,
                    text=""
                )
                self.lbl_imagen.pack(pady=20)

            except Exception as e:  # Captura cualquier excepción al cargar la imagen
                print(f"Error al cargar la imagen: {e}")

            # Mostrar el texto con la información
            result_text = (
                f"El filum es: {engine.result.name}\n\n"
                f"{engine.result.description}\n\n"
                f"Características coincidentes:\n" +
                "\n".join(f"- {prop.name}" for prop in engine.result.properties)
            )
        else:
            result_text = "No se encontró ningún filum que cumpla con las características dadas."

        ctk.CTkLabel(self, text=result_text, font=("Helvetica", 12), wraplength=400).pack(padx=10, pady=20)