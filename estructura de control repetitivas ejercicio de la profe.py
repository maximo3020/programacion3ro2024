l=[]
while True:#condición a evaluar
    opcion=input("Menú de opciones\n1-Agregar producto\n2-Eliminar producto\n3-Modificar productor\n4-Mostar productos\n5-Salir \n")
    if opcion=="1":#    variable para la opcion 1
         elementoAgregar=input("Ingrese elemento a agregar:") #preguntamos que elemento quiere agregar
         l.append(elementoAgregar)  #agregamos el elemento
    elif opcion=="2": #variable para la opcion 2
        elementoAeliminar=input("Ingrese el nombre del elemento a eleminar: ") #preguntamos que elemento que quiere eliminar
        if elementoAeliminar in l:#preguntamos si el elemento esta en la lista
           l.remove(elementoAeliminar) #si el elemento esta en la lista lo eliminamos
           print("Elemento eliminado exitosamente")  #mostrar que el elimento se elimino   
        else:
            print("El elemento que desea eliminar no se encuentra en la lista")   # mostrar que el elemento que se busca no esta en su lista   
    elif opcion=="3":#variable para la opcion 3
        elementoAmodificar=input("Ingrese el nombre del elmento a modificar: ")#preguntamos que elemento quiere modificar
        if elementoAmodificar in l:#preguntamos si el elemento esta en la lista
            elementoModificacion=input("Ingrese el nombre por el que quiere modificar: ")#preguntamos al usuario que nombre quiere modificar
            # Find the index of the element to modify
            index = l.index(elementoAmodificar)
            l[index] = elementoModificacion # Use the index to modify the element
        else:
            print("El elemento que desea modificar no se encuentra en la lista")#si el elemento no esta en la lista no se modifica 
           
    elif opcion=="4":#variable para la opcion 4
        print("Elementos en la lista: \n",l)  # se imprime el contenido de la lista
    elif opcion=="5":  #variable para la opcion 5          
        print("Saliendo del sistema")
        break#se corta el ciclo
    else:
        print("La opción ingresada es invalida")  #  el usuario ingresa un numero que no esta en el menu no se ejecuta en el programa
   










