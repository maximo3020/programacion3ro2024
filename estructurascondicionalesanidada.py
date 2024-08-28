n=int(input("ingrese un numero: "))
if n==10:
    print(n,"es igual a 10")
elif n<100 and n>9:
    print(n," es una decena")
elif n<10:
    print(n,"es una unidad")
elif n>99 and n<1000:
    print(n,"es una centena")
elif n>999 and n<100000:
    print(n,"es una milesima")