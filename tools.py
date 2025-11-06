#HERRAMIENTAS DEL MAIN
"""
tools.py
---------
Funciones utilitarias para interacción con el usuario y presentación de información.
"""
#MENÚ DEL PROGRAMA
def show_menu():
    """
    Muestra el menú principal con las opciones disponibles.
    """
    print("""
    Gestor de biblioteca 📚
        -------
        1️⃣  Libros disponibles
        2️⃣  Añadir libro
        3️⃣  Prestar libro
        4️⃣  Devolver libro
        5️⃣  Buscar libro
        6️⃣  Mostrar historial
        7️⃣  Salir del programa
        """)

#OPCIONES del menú
def opciones(mensaje):
        """
    -Solicita al usuario una opción numérica y valida que esté dentro de un rango.
    -Return:
        int: Opción válida introducida por el usuario.
    """
        try:
            opcion = int(input(mensaje))
            return opcion
        except ValueError:
            return print("¡Error ❌! Solo números")

def despedida():
    print(f"Gracias por usar nuestro gestor 📖")
