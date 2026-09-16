import numpy as np
import math as m


#Menu repetible

opciones = 1

while opciones != 4:  
    print("--------------------------------------------------")
    print("Bienvenido a la calculadora de funciones trigonométricas de Hokhmah por series de Taylor, calculamos:  ")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Salir")    
    
    opciones = int(input("Ingresa una opción: "))    

    if opciones == 1: 
        print("--------------------------------------------------")
        angulo = int(input("Angulo en grados a calcular: "))
        
        radianes = np.pi * angulo / 180
        
        print("--------------------------------------------------")
        
        print(f"Angulo escogido a radianes: {radianes}")
        
        print("--------------------------------------------------")
        
        n = int(input("Ingresa el número de términos para la serie de Taylor: "))
        
        
        suma = 0
        for i in range(n):
            termino = (((-1)**i) / (m.factorial(2*i+1))) * (radianes**(2*i+1))
            suma += termino #El += toma el valor suma y le suma termino, lo mismo que suma = suma + termino
            # Este proceso se hace para remplazar normalmente como se haría 
        
        
        print("--------------------------------------------------")
        print(f"Su respuesta es:✨ {suma} ✨")
        
    if opciones == 2:    
        print("--------------------------------------------------")
        
        angulo = int(input("Angulo en grados a calcular: "))
        
        radianes = np.pi * angulo / 180
        
        print("--------------------------------------------------")
        
        print(f"Angulo escogido a radianes: {radianes}")
        
        print("--------------------------------------------------")
        
        n = int(input("Ingresa el número de términos para la serie de Taylor: "))
        
        suma = 0
        
        for i in range(n):
            iesimotermino = (((-1)**i)/(m.factorial(2*i))) * (radianes**(2*i))
            suma += iesimotermino 
        
        print("--------------------------------------------------")
        print(f"Su respuesta es:✨ {suma} ✨")
        
    if opciones == 3:
        print("--------------------------------------------------")
        print("Lamentamos informar que la calculadora aún no tiene la opción tangente de un angulo implementada. (◕︵◕)")

    if opciones == 4: 
        print("--------------------------------------------------")

        print("Gracias por usar la calculadora de hokhmah, ten un lindo día. (^.^) ")
        
        print("--------------------------------------------------")
    
    if opciones > 4 or opciones < 1:
        print("--------------------------------------------------")

        print("Ha ocurrido un error, por favor escoge un valor entre 1 y 4, gracias por su comprensión. (?_?) ")    