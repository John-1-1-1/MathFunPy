from copy import deepcopy


class Number:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        if type(other) == Number:
            return Number(self.num + other.num)

    def __sub__(self, other):
        if type(other) == Number:
            return Number(self.num - other.num)

    def __mul__(self, other):
        if type(other) == Number:
            return Number(self.num * other.num)

    def __truediv__(self, other):
        if type(other) == Number:
            return Number(self.num / other.num)

    def __pow__(self, power, modulo=None):
        if type(power) == Number:
            return Number(self.num * power.num)

    def __str__(self):
        return str(self.num)

class Symbol:
    operators = {
        "+" : lambda x, y: x + y,
        "*" : lambda x, y: x * y
    }


    def __init__(self, name):
        self.name = name
        self.symb_a = None
        self.symb_b = None
        self.operation = None

    def __add__(self, other):

        ret = Symbol("") # TODO: Get Name


        ret.symb_a = self
        ret.symb_b = other
        ret.operation = "+"

        return ret

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __pow__(self, power, modulo=None):
        pass

    def __str__(self):
        if self.symb_a == None or self.symb_b == None:
            return self.name

        ret = str(self.symb_a) + self.operation + str(self.symb_b)
        return ret

    def lambdify(self, *params):
        pass


y = Symbol("y")
x = Symbol("x")
z = Symbol("z")

func = x+y+z+x+x+y

print(func)