from MathFunPyLib.Symbol import Symbol

if __name__ == "__main__":

    y = Symbol("y")
    x = Symbol("x")
    z = Symbol("z")

    func = 2+ ((z+4)**3) + 1222 +12 + (x *8+10+y+9)

    print(func)

    func.print_tree()