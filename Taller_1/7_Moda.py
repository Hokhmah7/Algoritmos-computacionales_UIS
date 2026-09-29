print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")

print("Bienvenido al Modainador de un conjunto de datos de Hokhmah7. (づ｡◕‿‿◕｡)づ")

print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")

#El programa tiene que tomar un conjunto de datos. 
#El programa tiene que analisar cada dato. 
#El programa tiene que identificar que datos son iguales. 
#El programa tiene que contar cuantas veces se repite el mismo dato. 
#El programa tiene que decir cual es el dato que más se repite. 
#El programa tiene que identificar si hay más de dos datos que más se repiten y expresarlos.
#El programa tiene que dar una respuesta sino hay ningún dato repetido. 


datos = []

datosf = []

datosfc = []

datosm = [] #Lista conformada por los valores que más se repiten del total de datos seleccionados. 

n = int(input("Selecciona la cantidad de datos: "))

for i in range(n):
    datos.append(int(input(f"Escoge el {i}° dato : ")))

print(datos)



for i in range (n):

    it = datos[i]

#Datosf Va a ser el conjunto de datos únicos. 

    if it not in datosf: 
        datosf.append(it)

print(datosf)


for i in range (len(datosf)):

    idfc = datos.count(datosf[i])

    datosfc.append(idfc)

print(f"Los datos seleccionados fueron: {datosfc} ")

for i in range (len(datosf)):

    if datosfc[i] == max(datosfc) and max(datosfc) > 1 : #Gloria a DIOS se me vino esta idea después de tanto pensarlo sin ia ni nada después de una semana entera sin hablar con nadie sobre este tema.

        datosm.append(datosf[i])


print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")

if len(datosm) == 0: 
    print("NO hay ningún dato que se repite.")

elif len(datosm) == 1:
    print(f"El dato que más se repite es {datosm[0]} un total de {max(datosfc)} veces.")

elif len(datosm) > 1: 
    print(f"Es multimodal, los datos que más se repiten son {datosm} un total de {max(datosfc)} veces.")

print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")