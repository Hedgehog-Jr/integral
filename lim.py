import math


def get_ab_limit(number):
    f = [None] * 28
    f[0] = [0.8, 1.762]
    f[1] = [1.3, 2.621]
    f[2] = [0.6, 1.724]
    f[3] = [3.0, 4.254]
    f[4] = [0, 1.234]
    f[5] = [0, 1.047]
    f[6] = [1.2, 2.471]
    f[7] = [1.0, 2.835]
    f[8] = [1.0, 2.631]
    f[9] = [2.0, 3.104]
    f[10] = [0, 1.075]
    f[11] = [0, 4.0]
    f[12] = [0, math.pi / 2]
    f[13] = [0, math.pi / 4]
    f[14] = [0, 1.0]
    f[15] = [3.0, 29.0]
    f[16] = [0, math.log(5, math.e)]
    f[17] = [1.0, 4.0]
    f[18] = [0, math.pi]
    f[19] = [0, math.pi / 2]
    f[20] = [-1.0, 1.0]
    f[21] = [-1.0, 1.0]
    f[22] = [0, 1.0]
    f[23] = [0, 1.0]
    f[24] = [0, 1.0]
    f[25] = [0, 1.0]
    f[26] = [0, 1.0]
    f[27] = [0, 1.0]
    return f[number]


def get_abcd_limit(number):
    f = [None] * 7
    f[0] = [0, 4.0, 1.0, 2.0]
    f[1] = [3.0, 4.0, 1.0, 2.0]
    f[2] = [0, 2.0, 0, 1.0]
    f[3] = [-1.0, 1.0, -1.0, 1.0]
    f[4] = [0, math.pi / 2, 0, math.pi / 4]
    f[5] = [0, 1.0, 1.0, 2.0]
    f[6] = [0, 2.0, 0.5, 1.5]
    return f[number - 28]

