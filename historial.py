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
#CREAR GET_HISTORY
#CREAR SHOW_HISTORY

def load_history():
    """
    Cargar el historial desde HISTORY_PATH, en caso de que no exista se crea uno inicial.
    
    Return:
        list: Lista de diccionarios de libros.
    """
    #VALIDACIÓN DE LA RUTA DEL HISTORIAL
    HISTORY_PATH.parent.mkdir(exist_ok=True) 
    
    #Cargar historial desde JSON.
    try:
        with HISTORY_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data
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
    print(f"{' ' * 10}Productos Disponibles")
    print("=" * 50)
    print(f"{'Id':<5} {'Producto':<25} {'Precio':<10} {'Stock':<10}")
    print("-" * 50)
    for libro in libros:
        if libro['stock'] > 0:
            print(f"{libro['id']:<5} {libro['status']:<25} €{libro['title']:<10.2f} {libro['autor']:<10} {libro['year']:<10} {libro['fecha']:<10}")
    print("-" * 50)
