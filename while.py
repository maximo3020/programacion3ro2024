prod=1
rta="si"
while rta=="si" or rta=="si":
    opcion =input("seleccione una opcion\n1. agregar producto a la lista\n2. mostrar producto en la lista\n3.salir")
    if opcion=="1":
        productoAgregar=input("ingrese el nombre del producto a agregar a la lista")
        prod.append(productoAgregar)
    elif opcion=="2":
        print("los productos en la lista son:\n_______________________")
        for p in prod:
            print(p,"\n___________________________")

    elif opcion=="3":
        rta=input("esta seguro de salir del sistema si/no: ")
        if rta=="si" or rta=="si" or rta=="si":
            print("saliendo del sistema")
    else:
        print("ingreso una opcion no valida")