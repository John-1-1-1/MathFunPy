from MathFunPyLib.Operation import Operation


class Sub(Operation):

    def __init__(self, *args):
        super().__init__("-")
        self.args = list(args)

    def __str__(self):
        ret = ""
        if len(self.args) > 1:
            ret = "-" + "-".join([str(i) for i in self.args])
        else:
            ret = "-"+str(self.args[0])
        return ret

    def lambdify(self):
        return sum([-i for i in self.args])