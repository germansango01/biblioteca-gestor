import os
from tools import show_menu, opciones, despedida

from books import Book
from book_manager import BookManager


#Funcion del MAIN
def main():

    try:
        books = Book()
        book_manager = BookManager(books)

    except Exception as e:
        print(f"\n❌ Error fatal al inicializar el sistema: {e}")
        print("Asegúrate de que las clases Product, Purchase, Cart y utils existen.")
        return

    continuar = True
    while continuar:
        os.system("cls")
        show_menu()
        opcion = opciones("Elije una opcion(1-7): ")
        match opcion:
            case 1:
                book_manager.show_books_list()
            case 2:
                book_manager.add_book_to_library()
            case 3:
                book_manager.lend_book_from_library()
            case 4:
                book_manager.restore_book_to_library()
            case 5:
                pass
            case 6:
                pass
            case 7:
                despedida()
                continuar = False
            case _:
                print("Esa opción no está disponible")
        input('Pulse cualquier tecla para continuar...')

if __name__ == "__main__":
        main()

