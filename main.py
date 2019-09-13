import f_x


def main():
    f = [f_x.f1, f_x.f2, f_x.f3, f_x.f4, f_x.f5, f_x.f6, f_x.f7, f_x.f8, f_x.f9, f_x.f10]
    #f += [f_x.f11, f_x.f12, f_x.f13, f_x.f14, f_x.f15, f_x.f16, f_x.f17, f_x.f18, f_x.f19, f_x.f20]
    #f += [f_x.f21, f_x.f22, f_x.f23, f_x.f24, f_x.f25, f_x.f26, f_x.f27, f_x.f28, f_x.f29, f_x.f30]
    #f += [f_x.f31, f_x.f32, f_x.f33, f_x.f34, f_x.f35]
    x = float(input("Введите x\n"))
    print(f[0](x))
    print(f[1](x))


main()

