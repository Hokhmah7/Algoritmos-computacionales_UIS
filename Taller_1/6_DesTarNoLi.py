print("Bienvenido al programa que haya la desviación estandar de números pares sin listas (DesTarNoLi) Hokhmah7.")

#1. Escoger un conjunto de datos.
#2. Identificar si son pares o impares.
#3. Hallar la media de los números pares. 
#4. Hallar la desviación estandar para cada dato par. 
#5. Sumar cada desviación y hallar la raíz cuadrada de la suma.


#MEDIA:

sdatos = 0
cdatos = 0

m = 0

while m != 4: 
    print("1. Escoger datos.")
    print("2. Desviación estandar poblacional.")
    print("3. Desviación estandar muestral.")
    print("4. Salir.")

    m = int(input("Escoge una opción: "))

    if m == 1: 

        m2 = 1

        while m2 != 0:

            dato = int(input("Escoge un dato: "))


            if dato % 2 != 0: 
                print("Error, no es par.")

            if dato % 2 == 0: 
                sdatos += dato
                cdatos += 1 

                #Como el valor de los datos no los guardamos por no usar listas.
                #Tenemos que hallar al momento la media para cada iteración.
                #Y evaluar directamente la desviacion cuadrática de los datos y no al momento 
                #Dios mío no sé que hacer aquí. Sino se guarda la variable dato. 
                #Como voy a restar dato con la media que es la suma de los datos entre el total de datos. >:(
                #Como hago que escoja el usuario todos sus datos. Los sume y divida en el total de datos (media), luego "recuerde" el primer, segundo y tercero y los reste secuencialmente con la media.  
                #El orden lógico es primero escoja los datos, cuente la cantidad de datos y luego. Al primer dato 
                #Luego le reste la media (Que es la división entre los datos seleccionados ya sumados previamente y el total de datos ya contado previamente.)

                print("------------------------------------------")
                print(f"La suma par de los datos es: {sdatos}")
                print("------------------------------------------")
                print(f"La cantidad de datos pares es: {cdatos}")
                print("------------------------------------------")
                m2 = int(input("agregar otro dato (1), terminar (0): "))
                print("------------------------------------------")

        m = sdatos/cdatos

        print(f"gaD (^u^)---> La media es: {m}")

        print("------------------------------------------")


                

    if m == 2: 
        if cdatos == 0:
            print("Error, no has escogido ningún dato.")

        else: 
            m = sdatos / cdatos

            devp = (dato / m) ** 2

