print("Bienvenido a la calculadora de números pares con menu de selección (ParMeMe) de Hokhmah7. Nos alegra que tan linda sonrisa haya confiado en nosotros. (^.^)")

n = 0

valores = []

while n != 3: 
    print("¿Quieres agregar un número?")

    print("1. SI")

    print("2. NO")

    print("3. SALIR")

    n = int(input("¿Cual opción deseas escoger? ---> "))
    print("------------------------------------------")
    print("------------------------------------------")
    print("------------------------------------------")
   

    if n == 1:
        numero = [int(input("¿Cual número deseas agregar? ---> "))]

        valores = valores + numero  

        print("------------------------------------------")
        print("------------------------------------------")
        print("------------------------------------------")
        print(f"Los valores seleccionados hasta ahora son: {valores}")


    if n == 2: 
        print(f"Vamos a hayar los números pares de los siguientes valores: {valores}")

        lpar = []
        for i in valores: 
            cpar = i % 2
            if cpar == 0:
                lpar.append(i)



        print("------------------------------------------")
        print(f"Los números pares son: {lpar}")
        print("------------------------------------------")

        if len(lpar) == 0:
            print("------------------------------------------")
            print("🚨Error:2 No se ha seleccionado un número par🚨") 
            print("------------------------------------------")

        else: 
            spar = 0
            for i in lpar:
                spar = spar + i

            print(f"La suma par es: {spar}")
            print("------------------------------------------")

            mpar = spar / len(lpar)

            print(f"¡Lo hicimos! La media par es:(づ ᴗ _ᴗ)づ♡  {mpar} ♡")



print("------------------------------------------")
print("🌇Aquí acaba el programa, pero no tu historia, sea esta una gran aventura.🌇")
print("------------------------------------------")
        


            

                
                


