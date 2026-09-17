print("Bienvenido a la calculadora de números pares con menu de selección (ParMeMe) de Hokhmah7. Nos alegra que tan linda sonrisa haya confiado en nosotros. (^.^)")

n = 0

valores = []

while n != 3: 

    print("¿Quieres agregar un número?")

    print("1. SI")

    print("2. NO")

    print("3. SALIR")

    n = int(input("¿Cual opción deseas escoger? ---> "))

   

    if n == 1:
        numero = [int(input("¿Cual número deseas agregar? ---> "))]

        valores = valores + numero  

        print(valores)

    if n == 2: 
        print(f"Vamos a hayar los números pares de los siguientes valores: {valores}")

        nvalores = len(valores)

        for i in range (nvalores): 
            itermino = valores[i]

            print(itermino)