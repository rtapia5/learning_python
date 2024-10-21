
import math
"""
a = int(input("Enter number for 'a': "))
b = int(input("Enter number for 'b': "))
c = int(input("Enter number for 'c': "))
b2 = b * b
fourAC = 4 * a * c
clump = abs(b2 - fourAC)
print("b^2 =", b2)
print("4ac =", fourAC)
print("clump =", clump)
sqr = math.sqrt(clump)
print("sqr =", sqr)

print("a =", a, "b =", b, "c =", c)

x1 = (( ((-1) * b) + sqr)/2*a)
x2 = (( ((-1) * b) - sqr)/2*a)

print("x1 =", x1)
print("x2 =", x2)
"""

"""this shoukld be the same thing as the above (code enclosed in block comment) only in function form"""

def quadratic_formula(a, b, c):
    b2 = b * b
    fourAC = 4 * a * c
    clump = abs(b2 - fourAC)
    
    sqr = math.sqrt(clump)
    x1 = (( (-1) * b + sqr)/ (2*a))
    x2 = (( (-1) * b - sqr)/ (2*a))

    return x1, x2



quadratic = quadratic_formula(2,3,4)

print(quadratic)