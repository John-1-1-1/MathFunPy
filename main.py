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
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "-": lambda x, y: x - y,
        "/": lambda x, y: x / y,
        "^": lambda x, y: x ** y
    }

    def __init__(self, name):
        self.name = name
        self.symb_a = None
        self.symb_b = None
        self.operation = None

    def __add_operation(self, other, operation):
        ret = Symbol("Func")

        ret.symb_a = self
        ret.symb_b = other
        ret.operation = operation

        return ret

    def __add__(self, other):
        return self.__add_operation(other, "+")

    def __sub__(self, other):
        return self.__add_operation(other, "-")

    def __mul__(self, other):
        return self.__add_operation(other, "*")

    def __truediv__(self, other):
        return self.__add_operation(other, "/")

    def __pow__(self, power, modulo=None):
        return self.__add_operation(power, "^")

    def __str__(self):
        if self.symb_a == None or self.symb_b == None:
            return self.name

        ret = str(self.symb_a) + " " + self.operation + " " + str(self.symb_b)

        if self.operation == "*" or self.operation == "/":
            ret = "(" + str(self.symb_a) + ") " + self.operation + " (" + str(self.symb_b) + ")"
        return ret



    def lambdify(self, *objects):

        objects = list(objects)

        if type(objects[0]) != str:
            objects = [i.name for i in objects]

        la_l = None
        la_r = None
        if self.symb_a != None:
            la_l = self.symb_a.lambdify(*objects)

        if self.symb_b != None:
            la_r = self.symb_b.lambdify(*objects)

        if self.operation == None:
            return lambda *params, data = objects.index(self.name): params[data]

        return lambda *params, function = self.operators[self.operation], la_ll = la_l, la_rr = la_r: function(la_ll(*params), la_rr(*params))


y = Symbol("y")
x = Symbol("x")
z = Symbol("z")

func = x +y * z

print(func)

f = func.lambdify(x,y,z)
print(f(1,22, 2))