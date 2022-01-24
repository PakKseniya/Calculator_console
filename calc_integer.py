
class CalcInteg:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        if other.num == 0:
            return ZeroDivisionError('Делить на ноль нельзя')
        else:
            return self.num / other.num

    def __pow__(self, degree, modulo=None):
        if self.num == 0:
            return 0
        elif degree == 0:
            return 1
        elif degree < 0:
            return 1 / self.num ** degree
        else:
            return self.num ** degree

    def __str__(self):
        return str(self.num)
