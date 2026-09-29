import numpy as np


print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")
print("Bienvenido al programa que cálcula la desviación estandar muestral y poblacional usando listas de números enteros pares  (DesTarLi) de Hokhmah7. Que la desviación a la grandeza que hay para tí, sea imperceptible. (^.^) 🛣️")
print("------------------------------------------")


#Programa que lea números variables de números enteros. 

#El programa identifique que números son pares e impares.

#El programa tenga la opción de escoger entre cálcular la desviación estandar poblacional o la muestral y deje indicado su diferencia.

#Anotar complicaciónes con listas y al hacerlo sin listas. 

m = 1
pdatos = []
datos = []

while m != 4:
    
    print("Escoge una opción:")

    print("1. Agregar datos.")

    print("2. Desviación estandar poblacional.")

    print("3. Desviación estandar muestral.")

    print("4. Salir.")

    print("------------------------------------------")
    m = int(input("Opción: "))



    if m == 1: #Apartado para escoger números pares.
        print("Recuerda que:")

        print("- Si los datos a ingresar representan *toda la población*, debes escoger la opción (2.) la desviacion estandar poblacional. Denotada normalmente como: N.")
        print("------------------------------------------")
        print("- Si los datos a ingresar representan una *muestra o porción* de los datos poblacional, debes escoger la opción (3.) Desviación estandar muestral denotada como: n.")
        print("------------------------------------------")
        print("Matemáticamente su diferencia radica en el denominador siendo en la muestral (n-1).")
        print("------------------------------------------")

        n = int(input("Cuantos datos vas a escoger: "))

        print("------------------------------------------")

        datos = []
        pdatos = []

        for i in range (n): 
            dato = [int(input(f"Dato {i}: "))] 
            #gaD: Por la idea de hacer un dataselector de una vez con un for. 
            #La ingeniosa forma de construirlo con el {i} que va variando a medida que va recorriendo el número total de datos.
            #Además de la idea de hacer una lista que escoja el dato seleccionado.

            datos += dato
            #Nota: Aquí para concatenar los datos también se podría  con un dato.append

        print("------------------------------------------")

        print(f"Los datos escogidos son los siguientes: {datos}")

        print("------------------------------------------")


        for i in range (len(datos)):

            if datos[i] % 2 == 0:
                 pdatos.append(datos[i])
        

        print("------------------------------------------")

        print(f"Los datos pares son los siguientes: {pdatos}")

        print("------------------------------------------")

        #Fuera del if que calcule la media de todos los datos escogidos. 
        mpar = sum(pdatos)/len(datos)

        print(f"gaD: Lo hemos logrado la media par es: {mpar}")

        print("------------------------------------------")

    if m == 2: #Desviación estandar poblacional 
        if len(pdatos) == 0:
            

            print("------------------------------------------")
            print("Upsss, no has escogido ningún dato. (¿_?)")
            print("------------------------------------------")

        else:
            ldesviacion = []

            for i in range(len(pdatos)):

                idesviacion = (pdatos[i] - mpar) ** 2

                ldesviacion.append(idesviacion)
            print("------------------------------------------")
            print(f"gaD: Para los datos pares la desviación cuadrática a la media par es: {ldesviacion}" )
            print("------------------------------------------")

            desvpob = np.sqrt(sum(ldesviacion)/len(pdatos))

            
            print("------------------------------------------")
            print(f"gaD: La desviacion estandar poblacional es:(•◡•)/ {desvpob} ")
            print("------------------------------------------")

    if m == 3: 
        if len(pdatos) == 0:    
            print("------------------------------------------")
            print("Upsss, no has escogido ningún dato. (¿_?)")
            print("------------------------------------------")

        else:
            ldesviacion = []

            for i in range(len(pdatos)):

                idesviacion = (pdatos[i] - mpar) ** 2

                ldesviacion.append(idesviacion)
            print("------------------------------------------")
            print(f"gaD: Para los datos pares la desviación cuadrática a la media par es: {ldesviacion}" )
            print("------------------------------------------")

            desvpob = np.sqrt(sum(ldesviacion)/len(pdatos)-1)

            
            print("------------------------------------------")
            print(f"gaD: La desviacion estandar muestral es:(•◡•)/ {desvpob} ")
            print("------------------------------------------")


        


        




print("------------------------------------------")
print("------------------------------------------")
print("Hasta luego, que la alegría brille en ti como el sol en su apojeo.(^ ^) ✨")
print("------------------------------------------")
print("------------------------------------------")