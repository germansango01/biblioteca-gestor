import os
from tools import show_menu, opciones
from historial import show_history, log_history

book1 = {
        "id": 1,
        "title": "German",
        "author": "Contreras",
        "year": 1987,
        "status": "Lend",
       "created_at": "2025-11-06"
    }


cargar = log_history(book1)


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
                show_history()
            case 7:
                 pass
                 continuar = False  
            case _:
                print("Esa opción no está disponible")
     
if __name__ == "__main__":
        main()
    
    