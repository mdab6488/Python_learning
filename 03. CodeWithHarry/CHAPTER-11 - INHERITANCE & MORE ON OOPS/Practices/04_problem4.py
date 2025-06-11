class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, cnumber):
        return Complex(self.r + cnumber.r, self.i + cnumber.i)

    def __mul__(self, cnumber):
        real_part = self.r * cnumber.r - self.i * cnumber.i
        imag_part = self.r * cnumber.i + self.i * cnumber.r

        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"

print()
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1 * c2)