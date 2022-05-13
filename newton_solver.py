import sympy as sym
from random import randrange

# Declaring variables
x = sym.symbols('x')
# expression to solve
exp = x ** 2 - 5 * x + 6


def newtons_method(fun, x_1=randrange(-20, 20), accuracy=0.001, r_ound=None):
    global x
    x_prev = x_1  # first number
    d_fun = sym.diff(fun, x)  # fun'
    while True:
        x = x_prev
        ar_th = eval(str(fun))  # f(xk)
        par_n = eval(str(d_fun))  # f'(xk)
        x_cur = x_prev - ar_th / par_n  # xk+1 = xk - f(xk)/f'(xk)
        if abs(x_cur - x_prev) < accuracy:
            if r_ound:
                return round(x_cur, 2)
            else:
                return x_cur
        else:
            x_prev = x_cur
            continue
