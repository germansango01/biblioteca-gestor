"""
historial.py
---------
Funciones para manejar el historial.
"""
#IMPORTACIONES
from pathlib import Path
import json
import datetime

# Ruta de historial.
HISTORY_PATH = Path("biblioteca-gestor") / "history.json"

# Variable global productos.
history = None

#CREAR LOAD_HISTORY() - ✔
#CREAR GET_HISTORY() - ✔
#CREAR SHOW_HISTORY() - ✔

def get_current_time():
    """
    Obtener la fecha y hora actual.

    Return:
        str: Cadena de texto con la fecha y hora actual.
    """
    # fecha actual.
    return datetime.datetime.now().isoformat()

def load_history():
    """
    Cargar el historial desde HISTORY_PATH, en caso de que no exista se crea uno inicial.
    
    Return:
        list: Lista de diccionarios de libros.
    """
    #VALIDACIÓN DE LA RUTA DEL HISTORIAL
    HISTORY_PATH.parent.mkdir(exist_ok=True) 
    
    #CREAR ARCHIVO SI NO EXISTE
    if not HISTORY_PATH.exists():
        return []
    
    #Cargar historial desde JSON.
    try:
        with HISTORY_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print(f"\n❌ Error: El archivo '{HISTORY_PATH}' contiene JSON mal formado y no se pudo cargar.")
        return []

def get_history():
    """
    Obtener historial.

    Return:
        list: lista de diccionarios con el historial.
    """
    global history

    # Validar productos.
    if history is None:
        history = load_history()
    return history    
    
    
def show_history() -> None:
    """
    Función para enseñar el historial de la biblioteca.
    """
    # Obtener historial de libros.
    libros = get_history()

    # Validar si no hay libros.
    if not libros:
        print("-" * 50)
        print("\nEl historial está vacío.\n")
        print("-" * 50)
        return

    # Mostrar historial.
    print("\n" + "=" * 50)
    print(f"{' ' * 10}Libros Disponibles")
    print("=" * 50)
    print(f"{'Id':<5} {'Titulo':<25} {'Autor':<10} {'Año':<10}")
    print("-" * 50)
    for libro in libros:
            print(f"{libro['id']:<5} {libro['status']:<25} €{libro['title']:<10} {libro['author']:<10} {libro['year']:<10} {libro['created_at']:<10}")
    print("-" * 50)

######################
def log_history(book_data):
    """
    Registrar una nueva entrada en el historial cuando se saca o devuelve un libro.
    
    """
    try:
        # Cargar historial existente.
        history = load_history()

        # Añadir la nueva compra.
        history.append(book_data)

        # Guardar el historial actualizado.
        save_libros(history)
        return True
    except Exception as e:
        print(f"❌ Error al registrar el libro en el historial: {e}")
        return False

def save_libros(books):
    """
    Guarda la lista completa del historial de prestamos y devoluciones
    
    """
    #VALIDACIÓN RUTA
    HISTORY_PATH.parent.mkdir(exist_ok=True)

    #Guardar movimientos en el JSON.
    try:
        with HISTORY_PATH.open("w", encoding="utf-8") as f:
            # Uso la variable 'books' que es más estándar.
            json.dump(books, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"❌ Error al guardar compras en '{HISTORY_PATH}': {type(e).__name__} - {e}")
