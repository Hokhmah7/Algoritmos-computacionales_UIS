import re as re

print("Bienvenido al split changer de Hokhmha7. Invertimos frases y palabras a disposición. (^.^)")

print("--------------------------------------------------")
print("--------------------------------------------------")
print("--------------------------------------------------")

frase = input("Ingresa la frase que quieres invertir: ")

print("--------------------------------------------------")


palabra = input("Ingresa la palabra que deseas invertir: ")

#Como pongo la condición de que sea solamente una palabra. Si detecta un espacio. 

cpalabra = palabra.split() 

cp = len(cpalabra)



if cp == 1:
    #Separar palabra (spalabra) e invertirla (invpalabra)
    spalabra = list(palabra)

    n = len(spalabra)

    invpalabra = ""

    for i in range (n):
        letra = spalabra[i] 

        invpalabra = letra + invpalabra

    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("--------------------------------------------------")

    print(f"Tu palabra invertida es: ✨{invpalabra}✨")

    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("--------------------------------------------------")

    #Separar frase (sfrase) e invertirla (invfrase) 
    sfrase = frase.split()

    n = len(sfrase)

    invfrase = " "

    for i in range (n): 
        palabra = sfrase[i]

        invfrase = palabra + " " + invfrase

    print(f"Tu frase invertida es: 📝   {invfrase}📝")

    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("--------------------------------------------------")
else: 
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print(f"⚠️   Error, se encontraron {cp} palabras.⚠️")
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("⚠️   Querido amigo, escoge una palabra sin espacios.⚠️")
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("--------------------------------------------------")