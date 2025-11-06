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
        # Usamos el book para obtener los datos
        books = self._books.get_books()

        if not books:
            print("-" * 70)
            print("\nNo hay libros disponibles en este momento.\n")
            print("-" * 70)
            return

        # Mostrar los libros disponibles.
        print("\n" + "=" * 70)
        print(f"{' ' * 10}Biblioteca")
        print("=" * 70)
        print(f"{'Id':<5} {'Titulo':<20} {'Autor':<20} {"Año":<10} {'Disponible':<4}")
        print("-" * 70)


        for book in books:


                print(f"{book['id']:<5} {book['title']:<20} {book['author']:<20} {book['year']:<10} {'SI' if book['available'] else 'NO':<4}")



        print("-" * 70)


    def add_book_to_library(self):
        """
        Interfaz para añadir libros a la biblioteca.
        """
        books = self._books.get_books()
        # validar id actual
        current_id = 0 if not books else len(books)

        # --- Book name---
        while True:
            try:
                title = input("Ingresa el titulo del libro a ingresar (o presiona Enter para cancelar): ").strip()
                if not title:
                    print("▶️ Acción cancelada por el usuario.")
                    return False

                book = self._books.find_book_title(title)

                if book:
                    print(f"❌ El libro con el titulo {title} ya existe. Intenta de nuevo.")
                    continue
                break
            except (EOFError, KeyboardInterrupt):
                print("\n ⚠️ Entrada interrumpida por el usuario.")
                return False

        # --- Book author ---
        while True:
            try:
                author = input("Ingresa el author del libro a ingresar (o presiona Enter para cancelar): ").strip()
                if not author:
                    print("▶️ Acción cancelada por el usuario.")
                    return False
                break
            except (EOFError, KeyboardInterrupt):
                print("\n ⚠️ Entrada interrumpida por el usuario.")
                return False

        # --- Book year ---
        year = None
        while True:
            try:
                input_year = input("Ingresa el año del libro a ingresar (o presiona Enter para cancelar): ").strip()
                if not input_year:
                    print("▶️ Acción cancelada por el usuario.")
                    return False

                year = int(input_year)

                if year <= 1:
                    print(f"❌ ingrese un año valido. Intenta de nuevo.")
                    continue
                break
            except ValueError:
                print("❌ Entrada no válida. Ingresa solo números para el ID del producto.")
            except (EOFError, KeyboardInterrupt):
                print("\n ⚠️ Entrada interrumpida por el usuario.")
                return False

        # Formato de nuevo libro.
        new_book = {
            "id": current_id + 1,
            "title": title,
            "author": author,
            "year": year,
            "available": True
        }

        # --- Agregar a la biblioteca ---
        add_to_library = self._books.add_book(new_book)

        if add_to_library:
            print(f"\n✅ Libro {new_book['title']} agragado a la biblioteca.")
            return True
        else:
            print("\n❌ No se pudo agregar el libro a la biblioteca.")
            return False


    def lend_book_from_library(self):
        """
        Interfaz para prestar libro.
        """

        self.show_books_list()
        books = self._books.get_books()

        if not books:
            return False

        # --- Seleccionar ID ---
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
                    print(f"❌ El libro con Id {book_id} no está disponible. Intenta de nuevo.")
                    continue
                break
            except ValueError:
                print("❌ Entrada no válida. Ingresa solo números para el ID del producto.")
            except (EOFError, KeyboardInterrupt):
                print("\n ⚠️ Entrada interrumpida por el usuario.")
                return False

        # --- Presat libro ---
        lend_book = self._books.lend_book(book_id)

        if lend_book:
            print(f"✅ Libro {book["title"]} prestado correctamente.")
            return True
        else:
            print("❌ No se pudo prestar el libro.")
            return False


    def restore_book_to_library(self):
        """
        Interfaz para devolver libro.
        """

        self.show_books_list()
        books = self._books.get_books()

        if not books:
            return False

        # --- Seleccionar ID ---
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
                    print(f"❌ El libro con Id {book_id} no está disponible. Intenta de nuevo.")
                    continue
                break
            except ValueError:
                print("❌ Entrada no válida. Ingresa solo números para el ID del producto.")
            except (EOFError, KeyboardInterrupt):
                print("\n ⚠️ Entrada interrumpida por el usuario.")
                return False

        # --- Retornar libro ---
        lend_book = self._books.return_book(book_id)

        if lend_book:
            print(f"✅ Libro {book["title"]} devuelto correctamente.")
            return True
        else:
            print("❌ No se pudo devolver el libro.")
            return False

