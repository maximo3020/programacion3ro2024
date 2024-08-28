mostrarmenu=("")
print("Menú:")
print("1 - Comenzar programa")
print("2 - Imprimir listado")
print("3 - Finalizar programa")

def comenzar_programa():
    print("Has seleccionado comenzar el programa.")

def imprimir_listado():
    print("Aquí está el listado.")

def main():
    while True:
        mostrarmenu()
        try:
            opcion = int(input("Selecciona una opción (1, 2, 3): "))
            if opcion == 1:
                comenzar_programa()
            elif opcion == 2:
                imprimir_listado()
            elif opcion == 3:
                print("Finalizando el programa.")
                break
            else:
                print("Opción incorrecta. Por favor, selecciona 1, 2 o 3.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

if __name__ == "__main__":
    main()