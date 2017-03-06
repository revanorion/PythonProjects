import math
import pylab
import numpy as np


def solve_quadratic(a, b, c):
    sqrt_inner = math.pow(b, 2) - 4 * a * c
    return "no real solutions" if sqrt_inner < 0 \
        else "one solution: " + str((-b - math.sqrt(sqrt_inner)) / (2 * a)) \
        if sqrt_inner == 0 \
        else "two solutions: x1=" + str((-b - math.sqrt(sqrt_inner)) / (2 * a)) + \
             " x2=" + str((-b + math.sqrt(sqrt_inner)) / (2 * a))

while 1:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    print(solve_quadratic(a, b, c))
    xs = np.linspace(-5, 5, 100)
    ys = []
    for x in xs:
        ys.append(a * math.pow(x, 2) + b * x + c)
    pylab.plot(xs, ys, 'bo-')
    pylab.show()
