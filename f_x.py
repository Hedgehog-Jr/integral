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


def f11(x):
    return 3 * x / pow(1 + pow(x, 3), 0.5)


def f12(x):
    return 1 / (1 + pow(x, 0.5))


def f13(x):
    return math.sin(x) * pow(math.cos(x), 2)


def f14(x):
    return (math.sin(x) + math.cos(x)) / (3 + math.sin(2 * x))


def f15(x):
    return 1 / (math.exp(x) + math.exp(-x))


def f16(x):
    return pow(x - 2, 2/3) / (pow(x - 2, 2/3) + 3)


def f17(x):
    return math.exp(x) * (math.exp(x) - 1) / (math.exp(x) + 3)


def f18(x):
    return x / pow(2 + 4 * x, 0.5)


def f19(x):
    return 1 / (3 + 2 * math.cos(x))


def f20(x):
    return pow(4 - pow(math.sin(x), 2), 0.5) / 2


def f21(x):
    return math.exp(2 * x) / pow(1 - pow(x, 2), 0.5)


def f22(x):
    return 1 / (pow(1 - pow(x, 2), 0.5) * (1 + pow(x, 2)))


def f23(x):
    return math.sin(x) / pow(x, 0.5)


def f24(x):
    return 1 / (pow(x, 0.5) * (math.exp(0.4 * x) + 1.5))


def f25(x):
    return pow(x, 0.5) / math.sin(pow(x, 2))


def f26(x):
    return pow(x, 0.5) / (1 + pow(x, 2))


def f27(x):
    return 1 / pow((1 + pow(x, 2)) * (4 + 3 * pow(x, 2)), 0.5)


def f28(x):
    exit(28)


def f29(x, y):
    return pow(x, 2) / (1 + pow(y, 2))


def f30(x, y):
    return 1 / pow(x + y, 2)


def f31(x, y):
    return pow(x, 2) + 2 * y


def f32(x, y):
    return 4 - pow(x, 2) - pow(y, 2)


def f33(x, y):
    return math.sin(x + y)


def f34(x, y):
    exit(34)


def f35(x, y):
    exit(35)

