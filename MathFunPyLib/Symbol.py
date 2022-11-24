from MathFunPyLib.Number import Number


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

        if type(other) == int and type(self.symb_b) == Number:
            self.symb_b = Number(self.operators[operation](self.symb_b.num, other))
            return self

        if type(other) == Symbol or type(self) == Symbol:
            ret = Symbol("Func")

            ret.symb_a = self
            ret.symb_b = other if type(other) == Symbol else Number(other)
            ret.operation = operation

            return ret


    def __add__(self, other):
        return self.__add_operation(other, "+")

    def __radd__(self, other):
        return self.__add_operation(other, "+")

    def __sub__(self, other):
        return self.__add_operation(other, "-")

    def __rsub__(self, other):
        return self.__add_operation(other, "-")

    def __mul__(self, other):
        return self.__add_operation(other, "*")

    def __rmul__(self, other):
        return self.__add_operation(other, "*")

    def __truediv__(self, other):
        return self.__add_operation(other, "/")

    def __rtruediv__(self, other):
        return self.__add_operation(other, "/")

    def __pow__(self, power, modulo=None):
        return self.__add_operation(power, "^")

    def __str__(self):
        if self.symb_a == None or self.symb_b == None:
            return self.name

        ret = str(self.symb_a) + " " + self.operation + " " + str(self.symb_b)

        if self.operation == "*" or self.operation == "/":
            ret = "(" + str(self.symb_a) + " " + self.operation + " " + str(self.symb_b) + ")"
        return ret

    def lambdify(self, *objects):

        if type(objects[0]) != str:
            objects = [i.name for i in objects]
        else:
            objects = list(objects)

        la_l = None
        la_r = None

        if type(self.symb_a) == Number:
            la_l = lambda *params, num = self.symb_a.num: num
        elif self.symb_a != None:
            la_l = self.symb_a.lambdify(*objects)
        if type(self.symb_b) == Number:
            la_r = lambda *params, num = self.symb_b.num: num
        elif self.symb_b != None:
            la_r = self.symb_b.lambdify(*objects)

        if self.operation == None:
            return lambda *params, data = objects.index(self.name): params[data]

        return lambda *params, function = self.operators[self.operation], la_ll = la_l, la_rr = la_r: function(la_ll(*params), la_rr(*params))