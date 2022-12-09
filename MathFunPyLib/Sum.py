from MathFunPyLib.Operation import Operation


class Sum(Operation):

    def __init__(self, *args):
        super().__init__("+")
        self.args = list(args)

    def __str__(self):
        return  f"<Sum {'+'.join([str(i) for i in self.args])}>"