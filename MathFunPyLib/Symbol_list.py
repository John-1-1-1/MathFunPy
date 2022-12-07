from MathFunPyLib.Number import Number

class info:

    operations_levels = {
        0: ("func"),
        1: ("()"),
        2: ("*", "/"),
        3: ("+", "-")
    }

    def __init__(self, index, operations):
        self.index = index


    def __level_operation(self, operation):
        for i, list_operations in operation:
            if operation in list_operations:
                return i
        else:
            return None




class Symbol_list:
    operators = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "-": lambda x, y: x - y,
        "/": lambda x, y: x / y,
        "^": lambda x, y: x ** y
    }

    def __init__(self, name):
        self.name = name
        self.info_list = []

    def diff(self, symbol):
        pass

    def __add_operation(self, other, operation):
        pass

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


    def lambdify(self, *objects):
        pass