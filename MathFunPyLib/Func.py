import copy

from MathFunPyLib.ClassFunc import ClassFunc
from MathFunPyLib.Num import Num
from MathFunPyLib.Operation import Operation
from MathFunPyLib.Div import Div
from MathFunPyLib.Mul import Mul
from MathFunPyLib.Sub import Sub
from MathFunPyLib.Sum import Sum



class Func(ClassFunc, Operation):

    operators = {
        "+": lambda *args: Sum(*args),
        "-": lambda *args: Sub(*args),
        "*": lambda *args: Mul(*args),
        "/": lambda *args: Div(*args)
    }

    priority = {
        0:(),
        1:(),
        2:(),
        3:(),
        4:("*", "/"),
        5:("+", "-")
    }

    def __init__(self, object: Operation):
        super().__init__("Func")
        self.args = [object]

    def get_level_func(self, operation):
        for index, list_operation in self.priority.items():
            if operation in list_operation:
                return index
        return -1

    def _add_operation(self, other, operation):
        if isinstance(other, Operation):
            other = Num("num", other)
        self.args.append(self.operators[operation](copy.deepcopy(other)))
        return self

    def __str__(self):
        return "("+' '.join([str(i) for i in self.args]) + ")"

    @staticmethod
    def get_func(operation, other, symbol):
        return Func.operators[operation](copy.deepcopy(symbol), other)

    def lambdify(self):
        pass