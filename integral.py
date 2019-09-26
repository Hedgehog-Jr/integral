import math
import copy


def trapeze(f, a, b, eps):
    # вычисление интеграла при n = 2
    n = 2
    x = a
    h = (b - a) / n
    i_h = (f(a) + f(b)) / 2
    for i in range(1, n):
        x += h
        i_h += f(x)
    i_h *= h
    # вычисление интеграла при n = 4
    x = a
    n *= 2
    h = (b - a) / n
    i_h2 = (f(a) + f(b)) / 2
    for i in range(1, n):
        x += h
        i_h2 += f(x)
    i_h2 *= h
    # проверка на точность
    while math.fabs(i_h - i_h2) > 3 * eps:
        i_h = copy.deepcopy(i_h2)
        x = a
        h = (b - a) / n
        i_h2 = (f(a) + f(b)) / 2
        for i in range(1, n):
            x += h
            i_h2 += f(x)
        i_h2 *= h

    return i_h2


def simpson(f, a, b, eps):
    n = 1
    # вычисление интеграла при n = 1
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
    # вычисление интеграла при n = 2
    n *= 2
    x = a
    h = (b - a) / (2 * n)
    i_h2 = f(x)
    for i in range(1, 2 * n):
        x += h
        if i % 2 == 0:
            i_h2 += 2 * f(x)
        else:
            i_h2 += 4 * f(x)
    x += h
    i_h2 += f(x)
    i_h2 *= h / 3
    # проверка на точность
    while math.fabs(i_h - i_h2) > 15 * eps:
        i_h = copy.deepcopy(i_h2)
        n *= 2
        x = a
        h = (b - a) / (2 * n)
        i_h2 = f(x)
        for i in range(1, 2 * n):
            x += h
            if i % 2 == 0:
                i_h2 += 2 * f(x)
            else:
                i_h2 += 4 * f(x)
        x += h
        i_h2 += f(x)
        i_h2 *= h / 3
    return i_h2


def cubature(f, a, b, c, d, eps):
    integral1 = 0
    integral2 = 0
    # вычисление интеграла при n = m = 2
    n = 2
    m = 2
    hx = (b - a) / (2 * n)
    hy = (d - c) / (2 * m)
    for i in range(0, n):
        for j in range(0, m):
            x2 = a + (2 * i) * hx
            y2 = c + (2 * j) * hy
            x2_1 = x2 + hx
            x2_2 = x2_1 + hx
            y2_1 = y2 + hy
            y2_2 = y2_1 + hy
            integral1 += f(x2, y2) + 4 * f(x2_1, y2) + f(x2_2, y2) + 4 * f(x2, y2_1) + 16 * f(x2_1, y2_1)
            integral1 += 4 * f(x2_2, y2_1) + f(x2, y2_2) + 4 * f(x2_1, y2_2) + f(x2_2, y2_2)
    integral1 *= hx * hy / 9
    # вычисление интеграла при n = m = 4
    n *= 2
    m *= 2
    hx = (b - a) / (2 * n)
    hy = (d - c) / (2 * m)
    for i in range(0, n):
        for j in range(0, m):
            x2 = a + (2 * i) * hx
            y2 = c + (2 * j) * hy
            x2_1 = x2 + hx
            x2_2 = x2_1 + hx
            y2_1 = y2 + hy
            y2_2 = y2_1 + hy
            integral2 += f(x2, y2) + 4 * f(x2_1, y2) + f(x2_2, y2) + 4 * f(x2, y2_1) + 16 * f(x2_1, y2_1)
            integral2 += 4 * f(x2_2, y2_1) + f(x2, y2_2) + 4 * f(x2_1, y2_2) + f(x2_2, y2_2)
    integral2 *= hx * hy / 9
    # проверка на точность
    while math.fabs(integral1 - integral2) > 15 * eps:
        integral1 = copy.deepcopy(integral2)
        integral2 = 0
        n *= 2
        m *= 2
        hx = (b - a) / (2 * n)
        hy = (d - c) / (2 * m)
        for i in range(0, n):
            for j in range(0, m):
                x2 = a + (2 * i) * hx
                y2 = c + (2 * j) * hy
                x2_1 = x2 + hx
                x2_2 = x2_1 + hx
                y2_1 = y2 + hy
                y2_2 = y2_1 + hy
                integral2 += f(x2, y2) + 4 * f(x2_1, y2) + f(x2_2, y2) + 4 * f(x2, y2_1) + 16 * f(x2_1, y2_1)
                integral2 += 4 * f(x2_2, y2_1) + f(x2, y2_2) + 4 * f(x2_1, y2_2) + f(x2_2, y2_2)
        integral2 *= hx * hy / 9
    return integral1

