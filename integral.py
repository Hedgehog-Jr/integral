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


def simpson(f, a, b, e):
    i_h = 5
    i_h2 = 1
    n = 1
    while math.fabs(i_h - i_h2) > 15 * e:
        x = a
        h = (b - a) / (2 * n)
        i_h = f(x)
        for i in range(1, 2 * n):
            x += h
            if i % 2 == 0:
                i_h += 2 * f(x)
            else:
                i_h += 4 * f(x)
        x += h
        i_h += f(x)
        i_h *= h / 3
        n *= 2
        x = a
        h2 = (b - a) / (2 * n)
        i_h2 = f(x)
        for i in range(1, 2 * n):
            x += h2
            if i % 2 == 0:
                i_h2 += 2 * f(x)
            else:
                i_h2 += 4 * f(x)
        x += h2
        i_h2 += f(x)
        i_h2 *= h2 / 3
    return i_h2
