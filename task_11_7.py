class ComplexNumber:

    def __init__(self, cmplx):
        self.cmplx = cmplx

    def __str__(self):
        return str(self.cmplx)

    def __add__(self, other):
        return ComplexNumber(self.cmplx + other.cmplx)

    def __sub__(self, other):
        return ComplexNumber(self.cmplx - other.cmplx)

    def __mul__(self, other):
        return ComplexNumber(self.cmplx * other.cmplx)

    def __truediv__(self, other):
        return ComplexNumber(self.cmplx / other.cmplx)


a = ComplexNumber(1 + 2j)

b = ComplexNumber(3 + 4j)

add = a + b
sub = a - b
mul = a * b
div = a / b

print(add)
print(sub)
print(mul)
print(div)
