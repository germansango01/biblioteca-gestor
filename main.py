import os
#Funcion del MAIN
def main():
    continuar = True
    while continuar:
        os.system("cls")
        menu()
        opcion = opciones("Elije opcion(1-5):")         
        match opcion:
            case 1:
                show_productos()
            case 2:
                add_album()
            case 3:
                del_carrito()
            case 4:
                total_compra()
            case 5:
                mensaje_salida()
                continuar = False  
            case _:
                print("Esa opción no está disponible")
     
if __name__ == "__main__":
        main()
    
    