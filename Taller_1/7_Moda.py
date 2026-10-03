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


datos = [] #Datos. Lista de selección de datos.

datosf = [] #Datos filtrados. datosf. Lista de los datos únicos del conjunto de datos.

datosfc = [] #Datos contados. datosc. Lista que cuenta cuantas veces se repite dada su posición un dato único que parte de datos filtrados. 

datosm = [] #Datos maximos. datos m. Lista conformada por los valores que más se repiten del total de datos seleccionados. 

n = int(input("Selecciona la cantidad de datos: "))

for i in range(n):
    datos.append(int(input(f"Escoge el {i}° dato : ")))

print("------------------------------------------")
print(f"Los datos seleccionados han sido: {datos}")
print("------------------------------------------")


for i in range (n):

    it = datos[i]

#Datosf Va a ser el conjunto de datos únicos. 

    if it not in datosf: 
        datosf.append(it)

print("------------------------------------------")
print(f"Los terminos existentes en la lista de datos son los siguientes: {datosf}")
print("------------------------------------------")

for i in range (len(datosf)):

    idfc = datos.count(datosf[i])

    datosfc.append(idfc)

print("------------------------------------------")

print(f"Cada dato se repite respectivamente: {datosfc} ")

print("------------------------------------------")

for i in range (len(datosf)):

    if datosfc[i] == max(datosfc) and max(datosfc) > 1 : #gaD: se me vino esta idea después de tanto pensarlo, Toma la frecuencia de cada dato y luego lo compara con la frecuencia máxima de los datos.
                                                        #gaD: Y el max(datosfc) > 1 Es para evitar el caso en que la frecuencia de los datos es 1, es decir no se repite ningún dato. 

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