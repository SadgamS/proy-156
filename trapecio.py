import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols  # importamos la libreria sympy
from sympy import lambdify
from sympy import sympify

x = symbols('x') # establecemos a x como variable simbolica

a = int(input('Introduzca a = '))
b = int(input('Introduzca b = '))
n = int(input('Introduzca n = '))
expr = input('Introduzca f(x) = ')
expr = sympify(expr)

#evaluamos la funcion
f = lambda valor: expr.subs(x, valor).evalf()

#def f(valor):
#    return expr.subs(x, valor).evalf()

# valor = 2
# 2**2
# 4


h = (b - a) / n
# I = (h/2)*(f(a)+ 2*sumatoria(f(xi)) + f(b))
s = 0
for i in range(1, n):
    print('i: ', i)
    s = s + f(a + h * i)
I = (h / 2) * (f(a) + 2 * s + f(b))
print('El aproximado es: ', I)

# Graficamos la funcion
lam_x = lambdify(x, expr, modules=['numpy'])
x_vals = np.linspace(a - 5, b + 5, 100)
y_vals = lam_x(x_vals)

plt.title(expr)
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x_vals, y_vals)
plt.grid(True)
plt.show()