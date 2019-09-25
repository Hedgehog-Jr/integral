import math


def trapeze(f, a, b, eps):
    i_h = 3 * eps
    i_h2 = eps
    n = 2
    while math.fabs(i_h - i_h2) > 3 * eps:
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


def simpson(f, a, b, eps):
    i_h = 3 * eps
    i_h2 = eps
    n = 1
    while math.fabs(i_h - i_h2) > 15 * eps:
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


def cubature(f, a, b, c, d):
    n = 1000
    m = 1000
    hx = (b - a) / (2 * n)
    hy = (d - c) / (2 * m)
    integral = 0
    for i in range(0, n):
        for j in range(0, m):
            x2 = a + (2 * i) * hx
            y2 = c + (2 * j) * hy
            x2_1 = x2 + hx
            x2_2 = x2_1 + hx
            y2_1 = y2 + hy
            y2_2 = y2_1 + hy
            integral += f(x2, y2) + 4 * f(x2_1, y2) + f(x2_2, y2) + 4 * f(x2, y2_1) + 16 * f(x2_1, y2_1)
            integral += 4 * f(x2_2, y2_1) + f(x2, y2_2) + 4 * f(x2_1, y2_2) + f(x2_2, y2_2)
    integral *= hx * hy / 9
    return integral

