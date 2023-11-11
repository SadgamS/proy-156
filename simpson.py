from math import *
from sympy import * #importamos la libreria sympy
from sympy import lambdify

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def metsimp():

    x = symbols('x') # establecemos a x como variable simbolica

    a = int(input('Introduzca el limite inferior a = '))  # limite inferior
    b = int(input('Introduzca el limite superior b = '))  # limite superior

    N=int(input('Introduzca el número de intervalos '))  #numero de intervalos

    if N % 2 == 0:  # verificamos si el intervalo es un numero par para continuar con el metodo

        expr=input('Introduzca f(x) = ') #introducimos la funcion por teclado

        expr = sympify(expr)  # transformamos de cadena a una expresion sympy

        f = lambda xk:expr.subs(x,xk).evalf()  # evaluamos la funcion y lo convertimos en un numero real

        y = []  # lista para almacenar los numeros obtenidos de la evalucion de f(x)

        x_val = np.linspace(a,b,N + 1)  # guardamos los numeros que estan en  el intervalo [a,b],
        # siendo la cantidad de numeros guardados-> N+1

        h = (b - a) / N  # numero de salto

        for i in range(len(x_val)):
            y.append(f(x_val[i]))  # insertamos los numeros de f(xi) en y

        s1 = np.sum(y[1:-1:2])  # sumatoria de los indices impares
        s2 = np.sum(y[2:-1:2])  # sumatoria de los indices pares

        r = (h / 3) * (f(a) + 4 * s1 + 2 * s2 + f(b))  # resultado del metodo de simpson compuesto

        d = {'x':x_val,'f(x)':y}  # diccionario para generar la tabla

        tabla = pd.DataFrame(d)  # creamos la tabla con la libreia PANDAS

        print(tabla.to_string())  # mostramos el contenido de la tabla completo
        print("")
        print('La solución es: ',r)

        # Graficamos la funcion

        lam_x = lambdify(x,expr,modules=['numpy'])
        x_vals = np.linspace(a-0.5,b+0.5,100)
        y_vals = lam_x(x_vals)

        fig,ax = plt.subplots()
        ax.plot(x_vals,y_vals,'r',linewidth=2)
        ax.set_ylim(bottom=0)

        lam_x1 = lambdify(x,expr,modules=['numpy'])
        x_vals1 = np.linspace(a,b)
        y_vals1 = lam_x1(x_vals1)

        fig.text(0.9,0.05,'$x$')
        fig.text(0.1,0.9,'$y$')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)



        plt.title('Gráfica de la función $f(x)$')
        plt.plot(x_vals,y_vals,color='navy',label='Función')
        plt.grid(True)

        plt.plot([a],[0],'ro',label='lim a')
        plt.plot([b],[0],'bo',label='lim b')


        plt.text(a,f(b),'Solución= %.4f' % (r),fontsize=16)

        plt.fill_between(x_vals1,y_vals1,facecolor='lightskyblue',edgecolor='k',label="$\int_a^b f(x)\mathrm{d}x$")
        plt.legend(loc='upper right')
        plt.show()
    else:
        print('El número de intervalos tiene que ser par')
        print('Vuelva a intentarlo')

