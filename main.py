import os
from tools import show_menu, opciones, despedida
import historial


book1 = {
        "id": 1,
        "title": "German",
        "author": "Contreras",
        "year": 1987,
        "status": "Lend",
       "created_at": "2025-11-06"
    }


cargar = historial.Loader(book1)


#Funcion del MAIN
def main():
    continuar = True
    while continuar:
        os.system("cls")
        show_menu()
        opcion = opciones("Elije una opcion(1-7):")         
        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                historial.show
            case 7:
                 despedida()
                 continuar = False  
            case _:
                print("Esa opción no está disponible")
                print("")
        input('Pulse cualquier tecla para continuar...')
     
if __name__ == "__main__":
        main()
    
    