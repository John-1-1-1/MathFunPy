import copy

from MathFunPyLib.ClassFunc import ClassFunc
from MathFunPyLib.Func import Func

class Symbol(ClassFunc):

    def __init__(self, name):
        self.name = name

    def _add_operation(self, other, operation):
        return Func(Func.get_func(operation,other, self))

    def __str__(self):
        return self.name