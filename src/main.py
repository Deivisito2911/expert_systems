"""
Sistema experto
"""
import interfaz.menu as menu
from acciones import engine


def main():
    engine.base.from_json("Base_De_Conocimiento/Filumcopy.json")  # Direccion de base de conocimiento por defecto
    app = menu.Interfaz()
    app.mainloop()


if __name__ == '__main__':
    main()
