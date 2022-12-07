import copy

from MathFunPyLib.Func import Func
from MathFunPyLib.Sub import Sub
from MathFunPyLib.Sum import Sum


class Symbol:
    operators = {
        "+": lambda *args: Sum(*args),
        "-": lambda *args: Sub(*args),
    }

    def __init__(self, name):
        self.name = name

    def __add_operation(self, other, operation):
        return Func(self.operators[operation](copy.deepcopy(self), other))


    def __add__(self, other):
        return self.__add_operation(other, "+")

    def __radd__(self, other):
        return self.__add_operation(other, "+")

    def __sub__(self, other):
        return self.__add_operation(other, "-")

    def __rsub__(self, other):
        return self.__add_operation(other, "-")

    def __str__(self):
        return self.name