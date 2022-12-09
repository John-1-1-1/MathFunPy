from MathFunPyLib.Operation import Operation


class Mul(Operation):

    def __init__(self, *args):
        super().__init__("*")
        self.args = list(args)

    def __str__(self):
        ret = ""
        if len(self.args) > 1:
            ret = "*".join([str(i) for i in self.args])
        else:
            ret = str(self.args[0])
        return f"<Mul {ret}>"