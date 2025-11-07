from pathlib import Path
from historial import History
import json

# Book Class
class Book:
    """
    Clase para el manejo de los libros.
    """
    # Ruta de libros.
    BOOKS_PATH = Path("files") / "books.json"

    def __init__(self, history: History):
        """
        Inicializa el Book y carga los libros.
        """
        self._books = self._load_books()
        self._history = history


    def _load_books(self):
        """
        Cargar lista de libros desde BOOKS_PATH. Si no existe,
        retorna una lista vacía.
        """
        # Validar ruta.
        self.BOOKS_PATH.parent.mkdir(exist_ok=True)

        # Crear archivo si no existe.
        if not self.BOOKS_PATH.exists():
            return []

        # Cargar libros desde JSON.
        try:
            with self.BOOKS_PATH.open("r", encoding="utf-8") as f:
                data = json.load(f)
                # Asegurar que data es una lista
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            print(f"\n❌ Error: El archivo '{self.BOOKS_PATH}' contiene JSON mal formado y no se pudo cargar.")
            return []


    def get_books(self):
            """
            Obtener la lista de libros actualizada.

            Return:
                list: Una copia de la lista de libros.
            """
            return self._books.copy()


    def _save_books(self):
        """
        Guarda a la lista de libros actual (self._books) en formato JSON.
        """
        # Validar ruta de libros.
        self.BOOKS_PATH.parent.mkdir(exist_ok=True)

        # Guardar los libros en el JSON.
        try:
            with self.BOOKS_PATH.open("w", encoding="utf-8") as f:
                # Accede al atributo interno self._books
                json.dump(self._books, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"❌ Error al guardar libros en '{self.BOOKS_PATH}': {type(e).__name__} - {e}")


    def find_book(self, book_id):
            """
            Buscar un libro por id.

            Args:
                book_id (int): ID del libro a buscar.

            Return:
                dict or None: El diccionario del libro o None si no se encuentra.
            """
            # Validar libros.
            if not self._books:
                return None

            # Buscar libro por ID.
            for book in self._books:
                if book.get("id") == book_id:
                    return book
            return None


    def find_book_title(self, book_title):
            """
            Buscar un libro por title dentro de la lista de libros.

            Args:
                book_title (str): Title del libro a buscar.

            Return:
                dict or None: El diccionario del libro o None si no se encuentra.
            """
            # Validar libros.
            if not self._books:
                return None

            # Buscar libro por Title.
            for book in self._books:
                if book.get("title").lower() == book_title.lower():
                    return book
            return None


    def add_book(self, book_data):
            """
            Guardar un nuevo libro en la biblioteca.

            Args:
                book_data (dict): Un diccionario con los datos de la libro a registrar.

            Return:
                bool: True si el registro fue exitoso, False si falló.
            """
            try:
                # Añadir libro nuevo a biblioteca.
                self._books.append(book_data)

                # Guardar libro a la biblioteca.
                self._save_books()
                return True
            except Exception as e:
                print(f"❌ Error al registrar el libro: {e}")
                return False


    def lend_book(self, book_id):
        """
        Prestar el libro.

        Args:
            book_id (int): ID del libro a prestar.

        Return:
            bool: True si se prestó el libro con éxito, False en caso contrario.
        """
        # Buscar libro por ID.
        book = self.find_book(book_id)

        # Validar libro existe.
        if not book:
            return False

        # Validar estado actual.
        if book.get("available") is False:
            return False

        history_data = {
            "id": book['id'],
            "status": "taken",
            "title": book['title'],
            "author": book['author'],
            "year": book['year'],
            "created_at": self._history._get_current_time()
        }

        # Guardar historial y actualizar estatus
        self._history.log_history(history_data)
        book["available"] = False

        return True


    def return_book(self, book_id):
        """
        Devolver el libro.

        Args:
            book_id (int): ID del libro a devolver.

        Return:
            bool: True si se devolvio el libro con éxito, False en caso contrario
        """
        # Buscar libro por ID.
        book = self.find_book(book_id)

        # Validar libro existe.
        if not book:
            return False

        # Validar estado actual.
        if book.get("available") is True:
            return False

        history_data = {
            "id": book['id'],
            "status": "returned",
            "title": book['title'],
            "author": book['author'],
            "year": book['year'],
            "created_at": self._history._get_current_time()
        }

        # Guardar historial y actualizar estatus
        self._history.log_history(history_data)
        book["available"] = True

        return True
