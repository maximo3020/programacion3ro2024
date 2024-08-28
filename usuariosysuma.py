sumadigitos=("numero")
"""Devuelve la suma de los dígitos de un número entero positivo."""
sum(int(digit) for digit in str)

def main():
    cantidad_pares = 0
    
    while True:
        try:
            numero = int(input("Ingresa un número entero positivo (o -1 para terminar): "))
            
            if numero == -1:
                break
            
            if numero < 0:
                print("Por favor, ingresa un número entero positivo.")
                continue
            
            suma = sumadigitos(numero)
            print(f"La suma de los dígitos de {numero} es: {suma}")
            
            if numero % 2 == 0:
                cantidad_pares += 1
        
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")
    
    print(f"Cantidad de números pares ingresados: {cantidad_pares}")

if __name__ == "__main__":
    main()