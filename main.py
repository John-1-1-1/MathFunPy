from MathFunPyLib.Symbol import Symbol

if __name__ == "__main__":

    y = Symbol("y")
    x = Symbol("x")
    z = Symbol("z")

    func = y+ 1222

    print(func)

    f = func.lambdify(y)
    print(func.diff())
    print(f(2))
    print(func.diff().lambdify(y)(4))