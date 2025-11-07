import os
from tools import show_menu, opciones, despedida
from historial import History

new_historial = History()

#Funcion del MAIN
def main():
    continuar = True
    while continuar:
        os.system("cls")
        show_menu()
        opcion = opciones("Elije una opción (1-7): ")
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
                new_historial.show_history()
            case 7:
                despedida()
                continuar = False
            case _:
                print("Esa opción no está disponible")
                print("")
        input('Pulse cualquier tecla para continuar...')


if __name__ == "__main__":
        main()
