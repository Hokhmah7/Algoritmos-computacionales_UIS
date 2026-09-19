#Programa que: 
#1. Seleccione números
#2. Identifique si es par.
#3. Sume los pares 
#4. Divida la suma por el total de números pares. 
#5. Si no hay números pares seleccionados haga algo.

#¿Como identifica sin listas que de los valores escogidos ninguno es par? 


print("------------------------------------------")
print("------------------------------------------")
print("------------------------------------------")
print("Bienvenido a la calculadora de números pares con menu de selección sin listas (ParMeMeNOLI) de Hokhmah7. \nNos alegra que tan linda sonrisa haya confiado en nosotros. (^.^)")
print("------------------------------------------")


#Nuestro criterio de finalización para seleccionar números en este caso va a ser que el usuario ingrese el número de ()

#Antes de entrar al ciclo while definimos nuestras variables que van a funcionar como acumuladores. 
suma_par = 0 #Va a cumplir la función de sumar los números que el programa identifica como pares.
contador_par = 0 #Va a cumplir la función de contar cuantos números pares están ingresando. 

#Iniciamos el ciclo while del cual vamos a tener tres condiciones en mente: 1) Si es par el número. 2) Si no es par. 3) Si queremos parar el ciclo con cero.
while True:

    print("------------------------------------------")
    n = int(input("Selecciona un número par, pon (0) para finalizar el programa: "))
    print("------------------------------------------")

    if n % 2 == 0: #La condición de paridad.
        suma_par = suma_par + n
        contador_par = contador_par + 1
        print(f"La suma de los números pares seleccionados es: {suma_par}")
        print(f"La cantidad de números pares seleccionados es: {contador_par}")

    if n % 2 != 0: #Condición que identifica un número impar. 
        
        print("------------------------------------------")
        print("🚨 Error. El número seleccionado no es par.🚨")
        print("------------------------------------------")

       
    if n == 0: #Condición que finaliza el programa y da la respuesta. 
        m_par = suma_par / contador_par

        print("------------------------------------------")
        print("------------------------------------------")
        print("------------------------------------------")

        print(f"gaD: La media aritmética es 🏆 {m_par}🏆. Cada logro es digno de ser aplaudido por más pequeño que fuese, al fin y al cabo se logró. (^.^)")

        print("------------------------------------------")
        print("------------------------------------------")
        print("------------------------------------------")

        break

# Se observa que a diferencia del caso con listas aquí no puedo hacer un acumulador visual que muestre los datos seleccionados.
# 






        



