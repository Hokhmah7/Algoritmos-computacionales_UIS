n = int(input("Escoge un valor: "))

datos = []

for i in range (n):
    datos.append(int(input(f"Dato {i}: ")))

print(datos)
print(sum(datos))