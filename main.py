import lab5


def main():
    f = [lab5.f1, lab5.f2, ]
    x = float(input("Введите x\n"))
    print(f[0](x))
    print(f[1](x))


main()

