link del colab=  https://colab.research.google.com/drive/1uwkZCsbtVoliVn4cM-FHunIccHkaQ1ii?authuser=0

violenciaDeGénero="La violencia contra las mujeres es una expresión de la relación de desigualdad entre varones y mujeres, es una violencia basada en la afirmación de la superioridad de un sexo sobre otro: de los varones sobre las mujeres. Afecta a toda la organización de nuestra sociedad y debe ser analizada dentro del contexto en el que vivimos tomando en cuenta la singularidad y subjetividad."

tipos={"Violencia física": "La más visible y reconocida como violencia de género, se considera violencia física todo aquel acto en que se inflige un daño físico a la víctima que a través de la agresión directa. Dicho daño puede ser temporal o permanente.",
"Violencia psicológica":" incluye la presencia de humillaciones, amenazas y coacciones (utilizándose en algunos casos la amenaza de agresión física a la víctima o a allegados)",
"violencia sexual":" podría considerarse dentro de la violencia física, la violencia sexual se refiere concretamente a aquel tipo de situaciones en que una persona es forzada o coaccionada para llevar a cabo actividades de índole sexual en contra de su voluntad, o bien en que la sexualidad es limitada o impuesta por otra persona",
"violencia economica":"Este tipo de violencia se basa en la reducción y privación de recursos económicos a la pareja o su prole como medida de coacción, manipulación o con la intención de dañar su integridad",
"violencia social":"La violencia social se basa en la limitación, control y la inducción al aislamiento social de la persona. Se separa a la víctima de familia y amigos, privandola de apoyo social y alejándose de su entorno habitual",
"violencia patrimonial":"Se considera violencia patrimonial la usurpación o destrucción de objetos, bienes y propiedades de la persona víctima de violencia con intención de dominarla o producirle un daño psicológico",
"violencia vicaria":"Un gran número de parejas en las que se produce violencia de género tienen hijos. En muchas ocasiones el agresor decide amenazar, agredir e incluso matar a dichos hijos con el propósito de dañar a su pareja o ex-pareja"
       }

print("Se presentarán una serie de enunciados y usted deberá responder a que tipo de violencia se refiere ")
print("")

vf=input("todo aquel acto en que se inflige un daño físico a la víctima que a través de la agresión directa. \n Dicho daño puede ser temporal o permanente. \n A qué tipo de violencia de Género se refiere:\n 1.● Violencia fica \n 2.● Violencia psicologica \n 3.● Violencia sexual \n 4.● violencia economica\n 5.● violencia social\n 6.● violencia patrimonial\n 7.● violencia vacaria")

if vf=="1":
  print("Correcto")
else:
   print("Incorrecto")
   print("")

print("________________")
vps=input(" incluye la presencia de humillaciones, amenazas y coacciones (utilizándose en algunos casos la amenaza de agresión física a la víctima o a allegados)")

if vps=="1":
  print("Correcto")
else:
   print("Incorrecto")
   print("")

print("___________")

vs=input("No es necesario que exista penetración ni que se produzca el acto sexual. Incluye la presencia de violaciones dentro de la pareja")
if vs=="1":
   print("correcto")
else:
   print("incorrecto")
   print("")
print("__________")
ve=input(" como tal el hecho de obligar a depender económicamente del agresor, impidiendo el acceso de la víctima al mercado laboral mediante amenaza, coacción o restricción física")
if vs=="1":
   print("correcto")
else:
   print("incorrecto")
   print("")
print("____________")
vso=input(" En ocasiones se pone a la víctima en contra de su entorno, produciendo que la víctima o entorno decidan desvincularse")
if vso=="1":
   print("correcto")
else:
   print("incorrecto")
   print("")
print("_________")
vpa=input("En muchos sentidos, estos bienes son el fruto de décadas de trabajo, y destruirlos es una manera de hacer ver que todos esos esfuerzos no han servido de nada")
if vpa=="1":
   print("correcto")
else:
   print("incorrecto")
   print("")
print("__________")
vv=input("Este tipo de violencia es denominada violencia vicaria, que también incluye el daño causado a los menores por la observación de malos tratos entre los progenitores")
if vv=="1":
   print("correcto")
else:
   print("incorrecto")
   print("")
print("__________")

print(violenciaDeGénero)
print("__________________")
for c, v in tipos.items():
   print(c," : ",v)
   print("____________")
   
