from MathFunPyLib.Operation import Operation


class Div(Operation):

    def __init__(self, *args):
        super().__init__("/")
        self.args = list(args)

    def __str__(self):
        if len(self.args) > 1:
            return "/".join([str(i) for i in self.args])
        else:
            return str(self.args[0])