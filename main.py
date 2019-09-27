import f_x
from lim import get_ab_limit, get_abcd_limit
from integral import trapeze, simpson, cubature


def main():
    f = [f_x.f1, f_x.f2, f_x.f3, f_x.f4, f_x.f5, f_x.f6, f_x.f7, f_x.f8, f_x.f9, f_x.f10]
    f += [f_x.f11, f_x.f12, f_x.f13, f_x.f14, f_x.f15, f_x.f16, f_x.f17, f_x.f18, f_x.f19, f_x.f20]
    f += [f_x.f21, f_x.f22, f_x.f23, f_x.f24, f_x.f25, f_x.f26, f_x.f27, f_x.f28, f_x.f29, f_x.f30]
    f += [f_x.f31, f_x.f32, f_x.f33, f_x.f34, f_x.f35]
    number = -1
    while (number < 1) or (number > 35):
        number = int(input("Введите номер функции: "))
    number -= 1
    if number < 28:
        a, b = get_ab_limit(number)
        print("Метод трапеции при eps = 1e-4: ")
        trapeze(f[number], a, b, 1e-4)
        print("Метод трапеции при eps = 1e-5: ")
        trapeze(f[number], a, b, 1e-5)
        print("Метод Симпсона при eps = 1e-4: ")
        simpson(f[number], a, b, 1e-4)
        print("Метод Симпсона при eps = 1e-5: ")
        simpson(f[number], a, b, 1e-5)
    else:
        a, b, c, d = get_abcd_limit(number)
        print("Кубатурная формула Симпсона при eps = 1e-10:")
        cubature(f[number], a, b, c, d, 1e-10)


main()

