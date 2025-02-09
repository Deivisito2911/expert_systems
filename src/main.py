"""
Sistema experto
"""
import interfaz.menu as menu
from acciones import engine


def main():
    try:#Intenta con rutas probadas en linux
        engine.base.from_json("GRUPO F/src/Base_De_Conocimiento/Phylumcopy.json")  # Direccion de base de conocimiento por defecto
    except:#Intenta con rutas probadas en windows
        engine.base.from_json("Base_De_Conocimiento/Phylumcopy.json")  # Direccion de base de conocimiento por defecto
    app = menu.Interfaz()
    app.mainloop()


if __name__ == '__main__':
    main()
