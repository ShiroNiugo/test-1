
from fractions import Fraction
a = Fraction(6, 4)
b = Fraction(7, 12)

"""
print(a, b, a+b, a*b)
"""

c=a*b
print(c.numerator, c.denominator, c, float(c))

print(c.limit_denominator(8))

x = 5.75
y = Fraction(*x.as_integer_ratio())
print(y, Fraction(23,4))