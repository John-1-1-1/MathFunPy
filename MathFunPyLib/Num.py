
class Num:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return str(self.value)

    def lambdify(self):
        return self.value