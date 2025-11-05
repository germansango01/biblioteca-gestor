import os
from tools import show_menu, opciones

#Funcion del MAIN
def main():
    continuar = True
    while continuar:
        os.system("cls")
        show_menu()
        opcion = opciones("Elije una opcion(1-6):")         
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
                pass
                continuar = False  
            case _:
                print("Esa opción no está disponible")
     
if __name__ == "__main__":
        main()
    
    