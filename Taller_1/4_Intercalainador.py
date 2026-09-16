print("Bienvenido al intercalainador de ceros de Hokhmah7 (^_^)")

print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")

numero = input("Escoge el número que quieres *intercerocalar*: ")

print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")

print(f"Intercerocalando el número: 🛠️   {numero}🛠️.")

print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")

lnumero = list(numero)

print(lnumero)

terminos = len(lnumero)

cerocalado = ""

for i in range (terminos): 
    ilnumero = lnumero[i] 

    oadder = ilnumero + "0" 

    cerocalado = cerocalado + oadder 

print(cerocalado)


