import sympy as sym


def trapezoid_inter(func, low, up, step=0.001):
    i = low
    j = low + step
    area = 0
    while j < up:
        area += (func(i) + func(j)) * step / 2
        i += step
        j += step
    return area


print(trapezoid_inter(lambda x: x**5 - 16, 0, 10, 0.1))
# Declaring variables
x = sym.symbols('x')
# expression
exp = x**5 - 16


def trapezoid_inter_fault(func, low, up, step=0.001):
    global x
    i = low
    j = i + step
    fault = 0
    d_func = sym.diff(func, x)
    d_d_func = sym.diff(d_func, x)
    while j < up:
        x = (i + j) / 2
        fault -= eval(str(d_d_func)) * (step**3) / 12
        i += step
        j += step
    return fault


print(trapezoid_inter_fault(exp, 0, 10, 0.1))
