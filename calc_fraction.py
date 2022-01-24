
def reduction(y, z):
    if abs(y) > abs(z):
        k = abs(y)
    else:
        k = abs(z)
    while k != 1:
        if y % k == 0 and z % k == 0:
            return k
        else:
            k -= 1
    return 1


class Fraction:
    def __init__(self, a=0, b=0):
        k = reduction(a, b)
        self.a = a // k
        self.b = b // k

    def __add__(self, other):
        y = self.a * other.b + self.b * other.a
        z = self.b * other.b
        k = reduction(y, z)
        return Fraction(y //k, z // k)

    def __sub__(self, other):
        if self.a * other.b - self.b * other.a == 0:
            y = 0
            z = self.b * other.b
        elif self.a * other.b - self.b * other.a != 0:
            y = self.a * other.b - self.b * other.a
            z = self.b * other.b
        k = reduction(y, z)
        return Fraction(y // k, z // k)

    def __mul__(self, other):
        y = self.a * other.a
        z = self.b * other.b
        k = reduction(y, z)
        return Fraction(y // k, z // k)

    def __truediv__(self, other):
        y = self.a * other.b
        z = self.b * other.a
        k = reduction(y, z)
        return Fraction(y // k, z // k)

    def __pow__(self, degree, modulo=None):
        y = self.a ** degree
        z = self.b ** degree
        k = reduction(y, z)
        return Fraction(y // k, z // k)

    def __str__(self):
        return str(self.a) + '/' + str(self.b)



