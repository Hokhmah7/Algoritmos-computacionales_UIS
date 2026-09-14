import numpy as np


#Menu repetible

opciones = 1

while opciones < 4: 
    print("--------------------------------------------------")
    print("Bienvenido a la calculadora de funciones trigonométricas de Hokhmah, podemos calcular por ti:  ")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Salir")    
    
    opciones = int(input("Ingresa una opción: "))    

    if opciones == 1: 
        angulo = int(input("Angulo en grados a calcular: "))
        
        radianes = np.pi * angulo / 180
        
        print(f"Angulo escogido a radianes: {radianes}")
        
        
        
        
        
        
        
        
        


#Calculo del seno



#Calculo del coseno