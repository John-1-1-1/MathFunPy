class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        if type(other) == Number:
            return Number(self.num + other.num)

    def __sub__(self, other):
        if type(other) == Number:
            return Number(self.num - other.num)

    def __mul__(self, other):
        if type(other) == Number:
            return Number(self.num * other.num)

    def __truediv__(self, other):
        if type(other) == Number:
            return Number(self.num / other.num)

    def __pow__(self, power, modulo=None):
        if type(power) == Number:
            return Number(self.num * power.num)

    def __str__(self):
        return str(self.num)
