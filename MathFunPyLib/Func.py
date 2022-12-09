import copy

from MathFunPyLib.ClassFunc import ClassFunc
from MathFunPyLib.Operation import Operation
from MathFunPyLib.Sub import Sub
from MathFunPyLib.Sum import Sum



class Func(ClassFunc):

    operators = {
        "+": lambda *args: Sum(*args),
        "-": lambda *args: Sub(*args),
    }

    priority = {
        0:(),
        1:(),
        2:(),
        3:(),
        4:(),
        5:("+", "-")
    }

    def __init__(self, object: Operation):
        self.objects_list = [object]

    def get_level_func(self, operation):
        for index, list_operation in self.priority.items():
            if operation in list_operation:
                return index
        return -1

    def _add_operation(self, other, operation):
        index_operation = [i.name for i in self.objects_list]
        index_operation = index_operation.index(operation) if index_operation.count(operation) > 0 else -1
        if index_operation != -1:
            self.objects_list[index_operation].args.append(other)
        elif self.get_level_func(self.objects_list[0].name) == self.get_level_func(operation):
            self.objects_list.append(self.operators[operation](other))

        return self

    def __str__(self):
        return f"<Func ({', '.join([str(i) for i in self.objects_list])})>"

    @staticmethod
    def get_func(operation, other, symbol):
        return Func.operators[operation](copy.deepcopy(symbol), other)