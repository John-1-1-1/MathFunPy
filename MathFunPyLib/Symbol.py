from MathFunPyLib.Number import Number


class listSymbols:
    def __init__(self):
        self.listSymbols = []


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

    def diff(self, symbol):

        if type(self.symb_a) == Symbol:
            self.symb_a = self.symb_a.diff()

        if type(self.symb_b) == Symbol:
            self.symb_b = self.symb_b.diff()

        if type(self.symb_a) == Number and self.operation in ['-', '+']:
            return self.symb_b

        if type(self.symb_b) == Number and self.operation in ['-', '+']:
            return self.symb_a

        #if type(self.symb_a) == Symbol and self.operation == "^":
        #    self.symb_a = self.symb_a * self.symb_b.copy()
        #    self.symb_b = self.symb_b - 1



        return self

    def __add_operation(self, other, operation):

        if operation == self.operation:
            if type(self.symb_a) != list:
                self.symb_a = [self.symb_a, other]
            else:
                self.symb_a = [*self.symb_a, other]
            return self

        if type(other) != Symbol:
            other = Number(other)

        if type(other) == Number and type(self.symb_b) == Number and \
                 self.operation in ["+", "-"] and operation in ["+", "-"]:
            self.symb_b = self.operators[operation]( self.symb_b, other)
            return self

        if type(self.symb_a) == Symbol and self.operation in ["+", "-"] and operation in ["+", "-"]:
            self.symb_a = self.symb_a.__add_operation(other, operation)
            return self
        else:
            ret = Symbol("Func")

            ret.symb_a = self
            ret.symb_b = other
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

        ret = "("+str(self.symb_a) + " " + self.operation + " " + str(self.symb_b)+")"

        if self.operation == "*" or self.operation == "/":
            ret = f"({str(self.symb_a)} {self.operation} {str(self.symb_b)})"
        return ret

    def print_tree(self, n = 1):
        print("-" * n, self.name, end = "")
        if self.operation != None:
            print(" ", self.operation, end=" ")
        if type(self.symb_a) == Number:
            print(self.symb_a.num, end=" ")
        if type(self.symb_b) == Number:
            print(self.symb_b.num, end=" ")
        print()
        if self.symb_a != None and type(self.symb_a) == Symbol:
            self.symb_a.print_tree(n+1)
        if self.symb_b != None and type(self.symb_b) == Symbol:
            self.symb_b.print_tree(n+1)
        #print("-" * n, self.symb_a.name if type(self.symb_a) == Symbol else self.symb_a.num, self.operation)
        #print("-" * n, self.symb_b.name if type(self.symb_b) == Symbol else self.symb_b.num)





    def lambdify(self, *objects):

        if type(objects[0]) != str:
            objects = [i.name for i in objects]
        else:
            objects = list(objects)

        obj_lambda = lambda symbol: (lambda *params, num = symbol.num: num) \
            if type(symbol) == Number else symbol.lambdify(*objects) \
            if symbol != None else None

        la_l = obj_lambda(self.symb_a)
        la_r = obj_lambda(self.symb_b)

        if self.operation == None:
            return lambda *params, data = objects.index(self.name): params[data]

        return lambda *params, function = self.operators[self.operation], la_ll = la_l, la_rr = la_r: function(la_ll(*params), la_rr(*params))