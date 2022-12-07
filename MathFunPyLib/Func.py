from MathFunPyLib.Operation import Operation


class Func:
    def __init__(self, object: Operation):
        self.object = object

    def __str__(self):
        return f"<Func ({self.object})>"


    def __add_operation(self, other, operation):
        if self.object.name == operation:
            self.object.args.append(other)
        
        return self


    def __add__(self, other):
        return self.__add_operation(other, "+")

    def __radd__(self, other):
        return self.__add_operation(other, "+")

    def __sub__(self, other):
        return self.__add_operation(other, "-")

    def __rsub__(self, other):
        return self.__add_operation(other, "-")
