n = int(input("Ingrese un número entero: "))

b = int(input("Ingrese un número entero entre 2 y 9: "))



if 2 <= b <=9: 

    a = n 

    valor = ""

    while a >= b:
        residuo = a % b

        a = a // b #El símbolo "//" divide n con b y arroja solamente la parte entera de la división.

        valor =  str(residuo) + valor #gaD: Primero: residuo1 + "", Segundo: residuo2 + residuo1. Nota que el primer valor en este orden de la suma pone el orden invertido a como sería naturalmente (residuo1+residuo2+residuo3...)  

    MrHide = str(a) + valor

    print(f"Residuo final: {a}")

    print(f"Tu número {n} en base {b} es el siguiente:{MrHide}")
    