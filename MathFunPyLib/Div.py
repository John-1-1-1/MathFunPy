from MathFunPyLib.Operation import Operation
from functools import reduce

class Div(Operation):

    def __init__(self, *args):
        super().__init__("/")
        self.args = list(args)

    def __str__(self):
        if len(self.args) > 1:
            return "/".join([str(i) for i in self.args])
        else:
            return str(self.args[0])

    def lambdify(self):
        return reduce(lambda x,y: x*y,[1/i for i in self.args])