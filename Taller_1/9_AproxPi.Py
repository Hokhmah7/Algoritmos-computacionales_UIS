import math as m
import numpy as np

#El programa debe aproximar el valor de pi mediante la serie de Leibniz.

#El programa debe recibir una tolerancia de aproximación.
    #Esta tolerancia es que tanto en cifras decimales debe aproximarse la serie de Leibniz. 

#El programa debe mostrar la aproximación. 

#El programa debe número de terminos utilizados.

#El programa debe mostrar el error respecto al valor de math.pi.


k = 0

piLeibniz = 0

t = float(input("Ingresa la tolerancia de aproximación mayor que 0: "))


if t > 0: 
    while k != -1:

        k = 1 + k
        
        piLeibniz += (((-1)**(k-1)) / (2 * (k-1) + 1))

        valorktermino = (((-1)**(k-1)) / (2 * (k-1) + 1))

        print(k)

        if abs(valorktermino) < t:
            break

    print("------------------------------------------")

    print(f"El número de terminos evaluados fueron: (╯°□°）╯ͼ..... {k}")

    print("------------------------------------------")

    print(f"La aproximación de Leibniz obtenida fue: ＼(＾O＾)／ {4*piLeibniz}")

    print("------------------------------------------")

    print(f"El error al valor real es de: {abs((4 * piLeibniz) - m.pi )}  📏")

    print("------------------------------------------")

    print(f"Valor de pi exacto dado por la biblioteca math: {m.pi}  🎯")

    print("------------------------------------------")

else: 
    print("------------------------------------------")

    print("ERROR: Valor erroneo de tolerancia.")

    print("------------------------------------------")