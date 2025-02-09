# Sistema Experto en Python
    Un sistema experto desarrollado en Python.

## Descripción del Sistema

    El siguiente sistema es un sistema experto tradicional diseñado para la identificación de fílum de especies a partir de características ingresadas en la "Base de conocimientos" del sistema. Este sistema carga dichas características y, utilizando reglas predefinidas, puede identificar a qué fílum pertenecen las especies, proporcionándonos una descripción detallada.

    La interfaz de usuario estándar permite varias operaciones, tales como:

    Consulta de características

    Adición de nuevas características

    Adición de nuevos fílum

    Otras opciones versátiles

    Este sistema destaca por su versatilidad, ya que no se limita únicamente a la identificación de fílum de especies. Dependiendo de la base de datos del usuario que se cargue, el sistema puede interpretar las características y evaluarlas según las reglas definidas. Estas proposiciones lógicas se utilizan para modelar el conocimiento y tomar decisiones, resultando en la identificación del fílum ingresado.

    Siguiendo el formato del archivo example.json incluido en el sistema, puedes aplicar este sistema experto en distintas áreas de desarrollo. No solo se limita a la identificación de fílum de especies, sino que es un sistema experto versátil que amplía su usabilidad en diversas aplicaciones.

## Instalación

### Instalar pipenv:

    bash
    pip install --user pipenv

### Instalar customtkinter:

    bash
    pip install --user customtkinter

### Instalar pillow:

    bash
    pip install pillow

## Ejecución

### Para ejecutar el sistema, utiliza el siguiente comando:

    bash
    pipenv run main.py

### Si ya tienes Python instalado, simplemente ejecuta:

    bash
    python main.py