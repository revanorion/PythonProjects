import math
import pylab
import numpy as np

ys = []

fun_str = input("Enter function with variable x: ")
samples = int(input("Enter number of samples: "))
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
xs = np.linspace(xmin, xmax, samples)
for x in xs:
    y = eval(fun_str)
    ys.append(y)

print('x'.rjust(10)+'y'.rjust(10))
print('-'*20)
for x in range(0, len(xs)):
    print('{0:+.4f}'.format(xs[x]).rjust(10) + '{0:+.4f}'.format(ys[x]).rjust(10))

pylab.xlabel("x")
pylab.ylabel("y")
pylab.title(fun_str)
pylab.plot(xs, ys, 'bo-')
pylab.show()
