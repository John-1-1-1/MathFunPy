import copy

from MathFunPyLib.ClassFunc import ClassFunc
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
        self.obj = [object]
        self.next_obj = None

    def get_level_func(self, operation):
        for index, list_operation in self.priority.items():
            if operation in list_operation:
                return index
        return -1

    def _add_operation(self, other, operation):

        index_operation = [i.name for i in self.obj]
        index_operation = index_operation.index(operation) if index_operation.count(operation) > 0 else -1
        if index_operation != -1:
            self.obj[index_operation].args.append(other)
        elif self.get_level_func(self.obj[0].name) == self.get_level_func(operation):
            self.obj.append(self.operators[operation](other))

        elif self.get_level_func(self.obj[0].name) < self.get_level_func(operation):
            f = Func(self.operators[operation](other))
            f.next_obj = self
            return f

        elif self.get_level_func(self.obj[0].name) > self.get_level_func(operation):
            f = Func(self)
            f.next_obj = self.operators[operation](other)
            return f

        return self

    def __str__(self):
        return f"<Func ({', '.join([str(i) for i in self.obj])} || {self.next_obj})>"

    @staticmethod
    def get_func(operation, other, symbol):
        return Func.operators[operation](copy.deepcopy(symbol), other)