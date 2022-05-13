def mutable_cord_solver(func, low, up, accuracy=0.001):
    if func(low) == 0:
        return low
    elif func(up) == 0:
        return up
    elif func(low) * func(up) > 0:
        print("put different limits")
        return None
    else:
        l_f = func(low)
        l_u = func(up)
        k = 0
        x_list = [low]
        while abs(up - low) >= accuracy:
            x_k = (low * l_u - up * l_f) / (l_u - l_f)
            x_list.append(x_k)
            if func(low) * func(x_k) < 0:
                up = x_k
                l_u = func(x_k)
                if func(x_list[k]) * func(x_list[k+1]) > 0:
                    l_f = l_f/2
            else:
                low = x_k
                l_u = func(x_k)
                if func(x_list[k]) * func(x_list[k+1]) > 0:
                    l_u = l_u / 2
            k += 1
        return low, up


print(mutable_cord_solver(lambda x: x**2 - 16, 0, 8))
