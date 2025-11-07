from books import Book

class BookManager:
    """
    Clase para manejar toda la interacción con los libros.
    Depende de Book para la lógica de negocio.
    """
    def __init__(self, books: Book):
        """
        Inicializa la interfaz con referencias a los gestores de datos.
        """
        self._books = books


    def show_books_list(self) -> None:
        """
        Muestra la lista de libros disponibles.
        """
        # Obtener libros.
        books = self._books.get_books()

        if not books:
            print("\n" + "=" * 75)
            print(f"📚 {'Biblioteca':^{75 - 4}}")
            print("=" * 75)
            print(f"\n{'⚠️  No hay libros disponibles en este momento.':^{75}}\n")
            print("-" * 75)
            return

        # Mostrar los libros disponibles.
        print("\n" + "=" * 75)
        print(f"📚 {'Biblioteca':^{75 - 4}}")
        print("=" * 75)
        print(f"{'ID':<5} {'Título':<30} {'Autor':<20} {'Año':<6} {'Disponible':<12}")
        print("-" * 75)

        for book in books:
            availability = '📗' if book.get('available', False) else '📕'
            print(f"{book['id']:<5} {book['title']:<30} {book['author']:<20} {book['year']:<6} {availability:^12}")

        print("-" * 75)

    def add_book_to_library(self):
        """
        Interfaz para añadir libros a la biblioteca.
        """
        # Obtener libros.
        books = self._books.get_books()

        # validar book id actual
        new_book_id = 0 if not books else len(books)

        #  Book title
        while True:
            try:
                title = input("Ingresa el título del libro a ingresar (o presiona Enter para cancelar): ").strip()
                if not title:
                    print("▶️ Acción cancelada por el usuario.")
                    return False

                book = self._books.find_book_title(title)

                if book:
                    print(f"❌ El libro con el título **{title}** ya existe en la biblioteca. Intenta con otro título.")
                    continue
                break
            except (EOFError, KeyboardInterrupt):
                print("\n ⚠️ Entrada interrumpida por el usuario.")
                return False

        #  Book author
        while True:
            try:
                author = input("Ingresa el autor del libro a ingresar (o presiona Enter para cancelar): ").strip()
                if not author:
                    print("▶️ Acción cancelada por el usuario.")
                    return False
                break
            except (EOFError, KeyboardInterrupt):
                print("\n ⚠️ Entrada interrumpida por el usuario.")
                return False

        #  Book year
        year = None
        while True:
            try:
                input_year = input("Ingresa el año de publicación del libro (o presiona Enter para cancelar): ").strip()
                if not input_year:
                    print("▶️ Acción cancelada por el usuario.")
                    return False

                year = int(input_year)

                # Validar año debe ser un número positivo
                if year <= 0:
                    print(f"❌ El año ingresado no es válido. Ingresa un número positivo (por ejemplo, 2024).")
                    continue
                break
            except ValueError:
                print("❌ Entrada no válida. Ingresa solo números enteros para el año.")
            except (EOFError, KeyboardInterrupt):
                print("\n ⚠️ Entrada interrumpida por el usuario.")
                return False

        # Formato de nuevo libro.
        new_book = {
            "id": new_book_id + 1,
            "title": title,
            "author": author,
            "year": year,
            "available": True
        }

        # Agregar a la biblioteca.
        add_to_library = self._books.add_book(new_book)

        # Validar ingreso del libro.
        if add_to_library:
            print(f"\n✅ Libro **{new_book['title']}** agregado correctamente a la biblioteca.")
            return True
        else:
            print(f"\n❌ No se pudo agregar el libro '{new_book['title']}' a la biblioteca debido a un error interno.")
            return False


    def lend_book_from_library(self):
        """
        Interfaz para prestar libro.
        """
        # Mostrar biblioteca.
        self.show_books_list()
        # Obtener libros.
        books = self._books.get_books()

        if not books:
            return False

        #  Seleccionar Book Id
        book_id = None
        while True:
            try:
                input_id = input("Ingresa el Id del libro a prestar (o presiona Enter para cancelar): ").strip()
                if not input_id:
                    print("▶️ Acción cancelada por el usuario.")
                    return False

                book_id = int(input_id)
                book = self._books.find_book(book_id)

                if not book:
                    print(f"❌ El libro con Id **{book_id}** no existe en la base de datos. Intenta de nuevo.")
                    continue
                break
            except ValueError:
                print("❌ Entrada no válida. Ingresa solo números para el ID del libro.")
            except (EOFError, KeyboardInterrupt):
                print("\n ⚠️ Entrada interrumpida por el usuario.")
                return False

        #  Prestar libro
        lend_book = self._books.lend_book(book_id)

        # Validar prestar libro.
        if lend_book:
            print(f"✅ Libro **{book['title']}** prestado correctamente.")
            return True
        else:
            print(f"❌ El libro **{book['title']}** no se pudo prestar. Es probable que ya esté prestado.")
            return False


    def restore_book_to_library(self):
        """
        Interfaz para devolver libro.
        """
        # Mostrar biblioteca.
        self.show_books_list()
        # Obtener libros.
        books = self._books.get_books()

        if not books:
            return False

        #  Seleccionar Book Id
        book_id = None
        while True:
            try:
                input_id = input("Ingresa el Id del libro a devolver (o presiona Enter para cancelar): ").strip()
                if not input_id:
                    print("▶️ Acción cancelada por el usuario.")
                    return False

                book_id = int(input_id)
                book = self._books.find_book(book_id)

                if not book:
                    print(f"❌ El libro con Id **{book_id}** no existe en el registro. Intenta de nuevo.")
                    continue
                break
            except ValueError:
                print("❌ Entrada no válida. Ingresa solo números para el ID del libro.")
            except (EOFError, KeyboardInterrupt):
                print("\n ⚠️ Entrada interrumpida por el usuario.")
                return False

        #  Retornar libro
        return_book = self._books.return_book(book_id)

        # validar retorno libro.
        if return_book:
            print(f"✅ Libro **{book['title']}** devuelto correctamente.")
            return True
        else:
            print(f"❌ No se pudo devolver el libro **{book['title']}**. Es probable que ya estuviera disponible (no prestado).")
            return False


    def find_book_from_library(self):
        """
        interfaz buscar libro
        """
        # Obtener libros.
        books = self._books.get_books()

        if not books:
            print(f"\n⚠️  No hay libros disponibles en este momento.")
            return False

        # Bucle para solicitar el libro.
        while True:
            try:
                # Book title
                title = input("Ingresa el título del libro a buscar (o presiona Enter para cancelar): ").strip()

                if not title:
                    print("▶️ Acción cancelada por el usuario.")
                    return False

                # Buscar el libro
                book = self._books.find_book_title(title)

                if book:
                    # Libro encontrado.
                    availability = '📗' if book.get('available', False) else '📕'
                    print("-" * 75)
                    print(f"{'ID':<5} {'Título':<30} {'Autor':<20} {'Año':<6} {'Disponible':<12}")
                    print(f"{book.get('id', 'N/A'):<5} {book.get('title', 'N/A'):<30} {book.get('author', 'N/A'):<20} {book.get('year', 'N/A'):<6} {availability:^12}")
                    print("-" * 75)

                    return True
                else:
                    # Libro no encontrado.
                    print(f"❌ El libro con el título **{title}** no existe en la biblioteca. Intenta con otro título.")
            except (EOFError, KeyboardInterrupt):
                print("\n ⚠️ Entrada interrumpida por el usuario.")
                return False
