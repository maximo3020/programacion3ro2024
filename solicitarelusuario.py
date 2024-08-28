frase = input("Ingrese una frase: ")

# Solicitar al usuario el ingreso de una letra
letra = input("Ingrese una letra: ")

# Verificar que se ha ingresado exactamente un carácter para la letra
if len(letra) != 1:
    print("Por favor, ingrese exactamente una letra.")
else:
    # Recorrer la frase carácter por carácter
    for i in range(len(frase)):
        if frase[i] == letra:
            print(f"Se encontró la letra '{letra}' en la posición {i}.")
            break  # Finalizar la ejecución si se encuentra una coincidencia
        else:
            print(f"No hay coincidencia en la posición {i}.")








