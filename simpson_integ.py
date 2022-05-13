import sympy as sym


def simpson_inter(func, low, up, step=0.001):
    i = low
    area = 0
    total_steps = (up - low) / step
    k = -1
    while i < up:
        k += 1
        if k == 0:
            area += func(i)
        elif k == total_steps:
            area += func(i)
        elif k % 2 == 0:
            area += 2 * func(i)
        else:
            area += 4 * func(i)
        i += step

    area = area * step / 3
    return area


print(simpson_inter(lambda y: y**5 - 16, 0, 10, 0.0001))
# Declaring variables
x = sym.symbols('x')
# expression
exp = x**5 - 16


def simpson_inter_fault(func, low, up, step=0.001):
    global x
    i = low
    fault = 0
    d_4_func = sym.diff(sym.diff(sym.diff(sym.diff(func, x))))
    while i < up:
        x = i
        fault += eval(str(d_4_func)) * ((step/2)**5) / 90
        i += step
    return fault


print(simpson_inter_fault(exp, 0, 10, 0.0001))
