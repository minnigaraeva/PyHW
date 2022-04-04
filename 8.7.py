class ComplexNumber:
    def __init__(self, integer, compl):
        self.integer = integer
        self.compl = compl

    def __str__(self):
        if self.compl > 0:
            return f'{self.integer} + {self.compl}j'
        return f'{self.integer} - {abs(self.compl)}j'

    def __add__(self, other):
        return ComplexNumber(self.integer + other.integer, self.compl + other.compl)

    def __mul__(self, other):
        return ComplexNumber(self.integer * other.integer - self.compl * other.compl, self.integer * other.compl + other.integer * self.compl)


a = ComplexNumber(3, 6)
b = ComplexNumber(4, -2)
print(a)
print(b)
print(a * b)
print(a + b)
