def dichotomy_solver(func, low, up, accuracy=0.001):
    if func(low) == 0:
        return low
    elif func(up) == 0:
        return up
    elif func(low) * func(up) > 0:
        print("put different limits")
        return None
    else:
        while abs(up - low) > accuracy:
            mid = (low + up) / 2
            if func(low) * func(mid) <= 0:
                up = mid
            else:
                low = mid
            if func(low) == 0:
                return low
            elif func(up) == 0:
                return up
        return low, up


print(dichotomy_solver(lambda x: x**3 - 16, 0, 4))
