import math


def f1(x):
    return pow(1 + pow(x, 3), 0.5)


def f2(x):
    return pow(pow(x, 3) - 1, -0.5)


def f3(x):
    return pow(x + pow(x, 3), 0.5)


def f4(x):
    return (1 + pow(x, 2)) / (1 + pow(x, 3))


def f5(x):
    return pow(math.sin(x), 2) / pow(1 + pow(x, 3), 0.5)


def f6(x):
    return math.exp(x / 2) / pow(x + 1, 0.5)


def f7(x):
    return pow(1 + 2 * pow(x, 3), 0.5)


def f8(x):
    return 1 / (pow(math.log10(x), 2) + 1)


def f9(x):
    return (1 + x + pow(x, 2)) / pow(pow(x, 3) - 1, 0.5)


def f10(x):
    return 0.1 * pow(x, 2) / math.log10(x)













