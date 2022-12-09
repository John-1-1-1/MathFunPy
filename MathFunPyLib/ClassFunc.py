

class ClassFunc:

    def _add_operation(self, other, operation):
        pass

    def __add__(self, other):
        return self._add_operation(other, "+")

    def __radd__(self, other):
        return self._add_operation(other, "+")

    def __sub__(self, other):
        return self._add_operation(other, "-")

    def __rsub__(self, other):
        return self._add_operation(other, "-")