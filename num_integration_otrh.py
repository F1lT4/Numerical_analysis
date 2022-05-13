import sympy as sym


def block_inter(func, low, up, step=0.001):
    i = low
    area = 0
    while i < up:
        area += func(i) * step
        i += step
    return area


print(block_inter(lambda x: x**3 - 16, 0, 10, 0.0001))
# Declaring variables
x = sym.symbols('x')
# expression
exp = x**3 - 16


def block_inter_fault(func, low, up, step=0.001):
    global x
    i = low
    fault = 0
    d_func = sym.diff(func, x)
    while i < up:
        x = i
        fault += eval(str(d_func)) * (step**2) / 2
        i += step
    return fault


print(block_inter_fault(exp, 0, 10, 0.0001))
