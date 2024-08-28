suma = 0
while True:
        try:
            numero = int(input("Ingresa un número entero (0 para terminar): "))
            if numero == 0:
                break
            elif numero > 0:
                suma += numero
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
    
print("La suma de todos los números positivos ingresados es:", suma)