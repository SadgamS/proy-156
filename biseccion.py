from math import *
from sympy import * #importamos la libreria sympy
from sympy import lambdify

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def metbisec():
    x = symbols('x') # establecemos a x como variable simbolicaç

    a = int(input('Introduzca el lim a = ')) # limite inferior
    b = int(input('Introduzca el lim b = ')) # limite superior

    ca = a
    cb = b
    #listas para generar la tabla

    fa=[]
    fb=[]
    Xc=[]
    fc=[]
    fn=[]

    tolerancia = float(input('Introduzca la tolerancia = '))

    c = 0.0

    expr = input('Introduzca f(x) = ') #introducimos la funcion por teclado


    expr = sympify(expr) # transformamos de cadena a una expresion sympy


    f = lambda xk: expr.subs(x, xk).evalf() #evaluamos la funcion y lo convertimos en un numero real

    N = float(log(b - a) - log(tolerancia) / log(2)) # calculamas el mumero de iteraciones

    N=int(round(N,1)) #lo redondeamos a una cifra y convertimos a entero

    print('Número de Iteraciones = ', N)

    if f(a) * f(b) > 0: # verificamos que exista una raiz
        print('No existe raiz en el intervalo')
        return

    else:
        for i in range(N):
            c = (a + b) / 2.0 # hallamos el punto medio

            fn.append(i+1); fa.append(round(a,5)); fb.append(round(b,5)); Xc.append(round(c,5));fc.append(round(f(c),5)) #guardamos los numeros en las listas con 5 cifras significativas para generar la tabla

            if f(a) * f(c) < 0: # la raiz esta en [a,c]
                b = c
            elif f(c) * f(b) < 0: # la raiz esta en [b, c]
                a = c
            else:
                break # encontramos la raiz


        d={"N":fn,"A":fa,"C":Xc,"B":fb,"F(c)":fc} # creamos un diccionario para guardas todos los datos para mostrar en la tabla
        tabla=pd.DataFrame(d) # generamos la tabla

        tabla.set_index("N",inplace=True) # especificamos que la Columna N es el indice

        print(tabla.to_string()) # mostramos la tabla completa
        print("")

        print('La raiz es %.5f' % (c))  # imprimir con formato

        #  Generamos la grafica
        lam_x = lambdify(x, expr, modules=['numpy'])
        x_vals = np.linspace(-10, 10, 30)
        y_vals = lam_x(x_vals)

        plt.title('Grafica de $f(x)$')
        plt.plot(x_vals, y_vals, label='Función')
        plt.grid(True)

        plt.axvline(x=ca, color='g', label='lim a')
        plt.axvline(x=cb, color='r', label='lim b')
        plt.plot([c], [f(c)], 'mD',label='raiz')
        plt.text(c,f(c), '%.6f' % (c), fontsize=15)
        plt.legend(loc='upper right')
        plt.show()