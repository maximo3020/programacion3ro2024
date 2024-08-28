numerosentero=[]
while True:
 numero=int(input("ingrese un numero entero:"))
 numerosentero.append(numero)
 if numero==0:
  break
print()
print(max(numerosentero))