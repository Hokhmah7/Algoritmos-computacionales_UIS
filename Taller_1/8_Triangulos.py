#El programa debe pedir tres valores enteros. 
#El programa debe rechazar valores negativos o nulos. 
#El programa debe repetir la petición de lados hasta que escoja un valor centinela. 
#El programa debe verificar si los lados pueden formar un triangulo por medio de la desigualdad triangular.
    #La sedigualdad triangular establece que para dos lados cualesquiera su suma debe ser siempre mayor al lado restante.
#El programa luego de verificar que efectivamente se puede formar un triangulo debe clasificarlo entre los tres tipos de triangulos. Equilatero, isosceles o escaleno.
#El programa debe clasificarlo segun sus angulos: Rectangulo acutangulo y obtusangulo.
#Fin

n = 0

lados = []




while n != 3: 

    print("Identificador de triangulos.")

    print("1. Escoger lados del triangulo.")

    print(f"2. Análisis del triangulo de lados: {lados}.")

    print("3. Salir del programa.")

    print("------------------------------------------")

    n = int(input("Escoge una opción: "))

    print("------------------------------------------")

    if n == 1: 

        lados = []  #gaD: Reinicia.

        for i in range (3):

            while True:
                l = int(input(f"Escoge el {i + 1}° lado del triangulo: "))
                print("------------------------------------------")

                if l <= 0: #Aquí va a 
                    print("Error, no existen lados negativos o nulos. Vuelve a escoger los tres lados. ⛔")
                    print("------------------------------------------")

                else: #Aquí va a escoger máximo tres veces el lado y los va a colocar en una lista. 
                    lados.append(l)
                    break
        print("------------------------------------------")


    if n == 2: 

        print("------------------------------------------")
        print(f"Los lados escogidos son: (˶ ˘ ³˘){lados}")
        print("------------------------------------------")

        # Verificar si es posible formar un triangulo.
        # Para verificar que es posible formar un triangulo se debe cumplir la desigualdad triangular.
        # Es decir la suma de los dos lados más pequeños debe ser estrictamente mayor al lado más grande, por tanto:

        if (sum(lados) - max(lados)) <= max(lados):

            print("------------------------------------------")
            print("Los lados escogidos lamentablemente no pueden formar un triangulo. (ㅠ﹏ㅠ)")
            print("------------------------------------------")

        if (sum(lados) - max(lados)) > max(lados):

            print("------------------------------------------")
            print("Los lados escogidos, sí pueden formar un triangulo !!! ⸜( ˶>ᴗ<˶)⸝♡ ")
            print("------------------------------------------")


            #Tipo de tringulo dado sus lados.

            print("Dado sus lados...  📏")

            if lados[0] == lados[1] == lados [2]: #Equilatero

                print("Tú triangulo es equilatero: Todos sus lados son iguales.")
                
                print("------------------------------------------")

            if lados[0] == lados[1] != lados[2] or lados[0] == lados [2] != lados[1] or lados[1] == lados[2] != lados[0]: #Isosceles

                print("Tú triangulo es isosceles: Solamente dos de sus lados son iguales.") 

                print("------------------------------------------")
                

            if lados[0] != lados[1] != lados[2]: #Escaleno

                print("Tú triangulo es escaleno: Todos sus lados son diferentes.")

                print("------------------------------------------")

            #Tipo de triángulo dado sus angulos:

            print("Dado sus ángulos... 🧭")

            if max(lados)**2 == lados[0]**2 + lados[1]**2 + lados[2]**2 - max(lados)**2: #Rectangulo: lado más grande al cuadrado es igual a la suma del cuadrado de los otros dos lados.

                print("Tú triangulo es rectángulo: Es decir tiene un ángulo recto de 90°. (c^2 = a^2 + b^2, siendo c el lado más grande.) ")

            if max(lados)**2 < lados[0]**2 + lados[1]**2 + lados[2]**2 - max(lados)**2: #Acútangulo: lado más grande al cuadrado es menor que la suma de los otros dos lados al cuadrado.
                print("Tú triángulo es acutangulo: Es decir todos sus ángulos son menores de 90°. (c^2 < a^2 + b^2, siendo c el lado más grande.)")

            if max(lados)**2 > lados[0]**2 + lados[1]**2 + lados[2]**2 - max(lados)**2: #Obtusángulo: Lado más largo (El opuesto al ángulo obtuso) es siempre mayor a la suma del cuadrado de los otros dos lados. Esto es así por teorema del coseno, en el que al evaluarlo para el lado obtuso da que el coseno cómo es mayor a 90° siempre será negativo.
                print("Tú triángulo es obtusángulo: Es decir hay un ángulo mayor a 90°. (c^2 > a^2 + b^2, siendo c el lado más grande.)")

            print("------------------------------------------")




    if n > 3:

        print("------------------------------------------")
        print("Error, no es una opción correcta. ⛔")
        print("------------------------------------------")



print("------------------------------------------")
print("El programa ha terminado ten un buen día. 🌇")
print("------------------------------------------")



