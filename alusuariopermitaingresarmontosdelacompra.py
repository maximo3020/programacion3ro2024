calculartotal=("montos")
sum("montos")

def aplicar_descuento(total):
    if total > 1000:
        total *= 0.9
    return total

def main():
    montos = []
    
    while True:
        try:
            monto = float(input("Ingrese el monto de la compra (0 para finalizar): "))
            
            if monto == 0:
                break
            elif monto < 0:
                print("Monto negativo. Ingrese un monto positivo.")
            else:
                montos.append(monto)
                
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")
    
    total = calculartotal(montos)
    total_con_descuento = aplicar_descuento(total)
    
    print(f"Total a pagar: ${total_con_descuento:.2f}")

if __name__ == "__main__":
    main()