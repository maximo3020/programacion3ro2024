contardigitospareseimpares=()
pares = 0
impares = 0
for digito in str("numero"):
        if int(digito) % 2 == 0:
            pares += 1
        else:
            impares += 1
            pares, impares

def main():
    total_pares = 0
    total_impares = 0
    
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo (0 para terminar): "))
            if numero < 0:
                print("Por favor, ingrese solo números enteros positivos.")
                continue
        except ValueError:
            print("Entrada no válida. Ingrese un número entero positivo.")
            continue
        
        if numero == 0:
            break
        
        pares, impares = contardigitospareseimpares(numero)
        
        print(f"Para el número {numero}:")
        print(f"- Dígitos pares: {pares}")
        print(f"- Dígitos impares: {impares}")
        
        total_pares += pares
        total_impares += impares
    
    print("\nResumen final:")
    print(f"Total de dígitos pares: {total_pares}")
    print(f"Total de dígitos impares: {total_impares}")