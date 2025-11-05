from pathlib import Path
import json

# Book Class
class Book:
    """
    Clase para el manejo de los libros.
    """
    # Ruta de libros.
    BOOKS_PATH = Path("files") / "books.json"

    def __init__(self):
        """
        Inicializa el Book y carga los libros.
        """
        self._books = self._load_books()


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

        # Cargar compras desde JSON.
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
            Buscar un libro por id dentro de la lista de libros.

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


    def lend_book(self, book_id, qty):
        """
        Prestar el libro.

        Args:
            book_id (int): ID del libro cuyo stock se debe reducir.
            qty (int): Cantidad a reducir.

        Return:
            bool: True si el stock se redujo con éxito, False en caso contrario.
        """
        # Buscar libro por ID.
        book = self.find_book(book_id)

        # Validar libro existe.
        if not book:
            return False

        # Validar stock.
        if book.get("stock", 0) >= qty:
            book["stock"] = book.get("stock", 0) - qty
            return True
        # Stock insuficiente.
        return False


    def return_book(self, book_id, qty):
        """
        Devolver el libro.

        Args:
            book_id (int): ID del libro cuyo stock se debe aumentar.
            qty (int): Cantidad a aumentar.

        Return:
            bool: True si el stock se aumentó con éxito, False en caso contrario
        """
        # Buscar libro por ID.
        book = self.find_book(book_id)

        # Validar libro y cantidad.
        if not book or qty <= 0:
            return False

        # Aumentar stock.
        book["stock"] = book.get("stock", 0) + qty
        return True
