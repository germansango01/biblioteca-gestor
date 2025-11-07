from pathlib import Path
import json
import datetime

class History:

    HISTORY_PATH = Path("files") / "history.json"
    history = None

    def __init__(self):
        """
        Inicializa el historial de li.
        """
        # El historial se almacena como un atributo de instancia
        self._history = self._load_history()


    def _load_history(self):
        """
            Cargar el historial desde HISTORY_PATH, en caso de que no exista se crea uno inicial.

            Return:
            list: Lista de diccionarios de libros.
        """
        # Validar ruta.
        self.HISTORY_PATH.parent.mkdir(exist_ok=True)

        # Crear archivo si no existe.
        if not self.HISTORY_PATH.exists():
            return []

        # Cargar historial desde JSON.
        try:
            with self.HISTORY_PATH.open("r", encoding="utf-8") as f:
                data = json.load(f)
                # Asegurar que data es una lista
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            print(f"\n❌ Error: El archivo '{self.HISTORY_PATH}' contiene JSON mal formado y no se pudo cargar.")
            return []


    def _get_current_time(self):
        """
        Obtener la fecha y hora actual en formato ISO.

        Return:
            str: Cadena de texto con la fecha y hora actual.
        """
        return datetime.datetime.now().isoformat()


    def _save_history(self):
        """
        Guarda la lista completa del historial en formato JSON.
        """
        # Validar ruta.
        self.HISTORY_PATH.parent.mkdir(exist_ok=True)

        # Guardar el historial en el JSON.
        try:
            with self.HISTORY_PATH.open("w", encoding="utf-8") as f:
                # Usa el atributo interno self._history
                json.dump(self._history, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"❌ Error al guardar compras en '{self.HISTORY_PATH}': {type(e).__name__} - {e}")


    def log_history(self, book_data):
        """
        Registrar un nuevo libro al historial de prestamos y devoluciones.

        Args:
            book_data (dict): Un diccionario con los datos del libro.

        Return:
            bool: True si el registro fue exitoso, False si falló.
        """
        try:
            # Agregar el timestamp.
            if "timestamp" not in book_data:
                book_data["created_at"] = self._get_current_time()

            # Añadir el libro al historial.
            self._history.append(book_data)

            # Guardar el historial actualizado
            self._save_history()
            return True
        except Exception as e:
            print(f"❌ Error al registrar la compra en el historial: {e}")
            return False


    def show_history(self) -> None:
        """
        Función para enseñar el historial de la biblioteca.
        """
        # Obtener historial de libros.
        libros = self._history.copy()

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
        print(f"{'Id':<3} {'Estado':<10} {'Titulo':<15} {'Autor':<10} {'Año':<10} {'Fecha':<10}")
        print("-" * 50)
        for libro in libros:
                print(f"{libro['id']:<3} {libro['status']:<10} {libro['title']:<15} {libro['author']:<10} {libro['year']:<10} {libro['created_at']:<10}")
        print("-" * 50)
