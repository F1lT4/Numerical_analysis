def block_inter(func, low, up, step=0.001):
    i = low
    area = 0
    while i < up:
        area += func(i + step / 2) * step
        i += step
    return area


print(block_inter(lambda x: x**3 - 16, 0, 10))
