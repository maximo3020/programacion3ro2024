listasdcalor=["empanadas","ensalada de tomate","matambre a la pizza"]
listasdfrios=["polenta","guiso","locro"]
clima=int(input("ingrese clima:"))
if clima>25 or clima<40:
 print ("comidas para el calor: ",listasdcalor)
else :
 print ("comidas para el frio:",listasdfrios)