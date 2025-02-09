import customtkinter as ctk
from experto_general.response import Response
from acciones import engine
from PIL import Image, ImageTk
import os

class ConsultarBase(ctk.CTkFrame):
    def __init__(self, parent):
        
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        # Paleta de colores
        self.color_verde = "#07bb87"
        self.color_verde_hover = "#007a5f"

        # Etiqueta de la pregunta
        self.lbl_question = ctk.CTkLabel(self, text="", font=("Helvetica", 20))
        self.lbl_question.pack(pady=30)  # Movido hacia arriba

        # Imagen de la característica
        self.lbl_imagen_caracteristica = ctk.CTkLabel(self, text="")
        self.lbl_imagen_caracteristica.pack(pady=5)  # Movido hacia arriba

        # Botones "Sí" y "No"
        button_frame = ctk.CTkFrame(self)  # Contenedor para botones
        button_frame.pack(pady=10)

        self.btn_yes = ctk.CTkButton(
            button_frame,
            text="Sí",
            command=lambda: self._get_question(Response.YES),
            text_color="#333333",
            fg_color=self.color_verde,
            hover_color=self.color_verde_hover,
        )
        self.btn_yes.pack(side="left", padx=50)

        self.btn_no = ctk.CTkButton(
            button_frame,
            text="No",
            command=lambda: self._get_question(Response.NO),
            text_color="#333333",
            fg_color=self.color_verde,
            hover_color=self.color_verde_hover,
        )
        self.btn_no.pack(side="right", padx=50)

        # Iniciar preguntas
        self.questions = engine.generate()
        self._get_question(Response.NO)

    def _get_question(self, response: Response):
        try:
            engine.set_response(response)
            question = next(self.questions)
            if question:
                # Obtener la ruta del directorio actual
                current_dir = os.path.dirname(__file__)
                self.lbl_question.configure(text=f"¿{question.name}?")

                # Intentar cargar imagen de la característica
                image_name_png = f"{question.name}.png"
                image_name_jpg = f"{question.name}.jpg"
                image_path = None
                #Carga de ruta de las imagenes
                if os.path.exists(os.path.join(current_dir, "..","..","assets", "images", image_name_png)):
                    image_path = os.path.join(current_dir, "..","..","assets", "images", image_name_png)
                elif os.path.exists(os.path.join(current_dir, "..","..","assets", "images", image_name_jpg)):
                    image_path = os.path.join(current_dir, "..","..","assets", "images", image_name_jpg)

                if image_path:
                    image = Image.open(image_path)
                    self.imagen_caracteristica = ctk.CTkImage(light_image=image, size=(200, 200))
                    self.lbl_imagen_caracteristica.configure(image=self.imagen_caracteristica, text="")
                else:
                    self.lbl_imagen_caracteristica.configure(text="Imagen no disponible")
                    print(f"No se encontró imagen para: {question.name}")

            else:
                self._finished()
        except StopIteration:
            self._finished()

    def _finished(self):
        # Limpiar los widgets existentes
        for widget in self.winfo_children():
            widget.pack_forget()

        # Mostrar el resultado
        if engine.result:
            # Obtener la ruta del directorio actual
            current_dir = os.path.dirname(__file__)
            # Crear el nombre del archivo de imagen
            image_name_png = f"{engine.result.name}.png"
            image_name_jpg = f"{engine.result.name}.jpg"
            image_path = None
            #Carga ruta de las imagenes
            if os.path.exists(os.path.join(current_dir, "..","..","assets", "images", image_name_png)):
                image_path = os.path.join(current_dir, "..","..","assets", "images", image_name_png)
            elif os.path.exists(os.path.join(current_dir, "..","..","assets", "images", image_name_jpg)):
                image_path = os.path.join(current_dir, "..","..","assets", "images", image_name_jpg)

            try:
                if image_path:
                    image = Image.open(image_path)
                    self.imagen = ctk.CTkImage(light_image=image, size=(120, 120))

                    # Crear frame para el contenido y colocarlo arriba
                    frame_contenido = ctk.CTkFrame(self)
                    frame_contenido.pack(fill="both", expand=True, pady=10)

                    #Usar un frame para las imagenes y el texto para centrar todo
                    frame_central = ctk.CTkFrame(frame_contenido)
                    frame_central.pack(expand=True, pady=10)

                    # Imagen izquierda
                    self.lbl_imagen_izquierda = ctk.CTkLabel(frame_contenido, image=self.imagen, text="")
                    self.lbl_imagen_izquierda.pack(side="left", padx=10)

                    # Texto del resultado
                    result_text = (
                        f"El Phylum es: {engine.result.name}\n\n"
                        f"{engine.result.description}\n\n"
                        f"Características coincidentes:\n" + "\n".join(f"- {prop.name}" for prop in engine.result.properties)
                    )
                    label_texto = ctk.CTkLabel(frame_contenido, text=result_text, font=("Helvetica", 12), wraplength=400)
                    label_texto.pack(side="left", padx=10)

                    # Imagen derecha
                    self.lbl_imagen_derecha = ctk.CTkLabel(frame_contenido, image=self.imagen, text="")
                    self.lbl_imagen_derecha.pack(side="right", padx=10)

                    #Centrar el frame central
                    frame_contenido.update_idletasks()
                    frame_central.place(relx=0.5, rely=0.5, anchor="center")

                else:
                    print(f"No se encontró imagen para el Phylum: {engine.result.name}")

            except Exception as e:
                print(f"Error al cargar la imagen: {e}")

        else:
            result_text = "No se encontró ningún phylum que cumpla con las características dadas."
            label_final = ctk.CTkLabel(self, text=result_text, font=("Helvetica", 12), wraplength=400)
            label_final.pack(padx=10, pady=20)
