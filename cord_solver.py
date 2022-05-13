def cord_solver(func, low, up, accuracy=0.001):
    if func(low) == 0:
        return low
    elif func(up) == 0:
        return up
    elif func(low) * func(up) > 0:
        print("put different limits")
        return None
    else:
        c = 1
        while abs(func(c)) >= accuracy:
            c = (low * func(up) - up * func(low)) / (func(up) - func(low))
            if func(low) * func(c) <= 0:
                up = c
            else:
                low = c
        return c


print(cord_solver(lambda x: x**3 - 16, 0, 52))
