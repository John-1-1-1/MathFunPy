from MathFunPyLib.Symbol import Symbol

if __name__ == "__main__":

    y = Symbol("y")
    x = Symbol("x")
    z = Symbol("z")

    func = 12 +y * z + 9 + 1222 + (3*x*5)

    print(func)

    f = func.lambdify(x,y,z)
    print(f(1,3, 2))