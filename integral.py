import math


def trapeze(f, a, b, e):
    i_h = 5
    i_h2 = 1
    n = 2
    while math.fabs(i_h - i_h2) > 3 * e:
        x = a
        h = (b - a) / n
        i_h = (f(a) + f(b)) / 2
        for i in range(1, n):
            x += h
            i_h += f(x)
        i_h *= h
        x = a
        n *= 2
        h2 = (b - a) / n
        i_h2 = (f(a) + f(b)) / 2
        for i in range(1, n):
            x += h2
            i_h2 += f(x)
        i_h2 *= h2
    return i_h2
