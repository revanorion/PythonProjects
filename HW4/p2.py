import copy, math


class Poly:
    def __init__(self, coeff):
        self.coefficients = {}
        degree = 0
        if isinstance(coeff, list) | isinstance(coeff, tuple):
            for x in coeff:
                self.coefficients.update({degree: float(x)})
                degree += 1
        elif isinstance(coeff, dict):
            self.coefficients = coeff

    def get_string(self):
        result = ""
        for x in self.coefficients:
            if self.coefficients[x] != 0:
                if x == 0:
                    result += str(self.coefficients[x])
                elif self.coefficients[x] > 0:
                    result += '+'
                else:
                    result += '-'
                if x != 0 and abs(self.coefficients[x]) > 1:
                    result += str(abs(self.coefficients[x]))
                if x > 1:
                    result += 'X^' + str(x)
                elif x != 0:
                    result += 'X'
                if result[0] == '+':
                    result = result[1:]
        return result

    def __str__(self):
        return self.get_string()

    def __repr__(self):
        return self.get_string()

    def __getitem__(self, item):
        if item in self.coefficients:
            return self.coefficients[item]
        else:
            raise ValueError('Index not in bounds')

    def __add__(self, other):
        coefficients = copy.deepcopy(self.coefficients)
        for coefficent_loc in other.coefficients:
            if coefficent_loc in self.coefficients:
                coefficients[coefficent_loc] = coefficients[coefficent_loc] + other[coefficent_loc]
            else:
                coefficients.update({coefficent_loc, other[coefficent_loc]})
        return Poly(coefficients)

    def mult(self, other):
        coefficients = copy.deepcopy(self.coefficients)
        if isinstance(other, int) | isinstance(other, float):
            for degree in coefficients:
                coefficients[degree] *= other
            return Poly(coefficients)
        elif isinstance(other, Poly):
            coefficients2 = copy.deepcopy(other.coefficients)
            result = {}
            for degree1 in coefficients:
                for degree2 in coefficients2:
                    if (degree1 + degree2) in result:
                        result[degree1 + degree2] += coefficients[degree1] * coefficients2[degree2]
                    else:
                        result.update({degree1 + degree2: coefficients[degree1] * coefficients2[degree2]})
            return Poly(result)
        else:
            return 0

    def __mul__(self, other):
        return self.mult(other)

    def __rmul__(self, other):
        return self.mult(other)

    def __eq__(self, other):
        for degree in self.coefficients:
            if degree in other.coefficients and other.coefficients[degree] == self.coefficients[degree]:
                continue
            return False
        for degree in other.coefficients:
            if degree in self.coefficients and other.coefficients[degree] == self.coefficients[degree]:
                continue
            return False
        return True

    def __ne__(self, other):
        for degree in self.coefficients:
            if degree in other.coefficients and other.coefficients[degree] == self.coefficients[degree]:
                return False
        for degree in other.coefficients:
            if degree in self.coefficients and other.coefficients[degree] == self.coefficients[degree]:
                return False
        return True

    def solve_x(self, X):
        result = 0.0
        for degree in self.coefficients:
            result += self.coefficients[degree] * math.pow(X, degree)
        return result

    def eval(self, X):
        if isinstance(X, int) | isinstance(X, float):
            return self.solve_x(X)
        elif isinstance(X, list):
            result = []
            for Xvalue in X:
                result.append(self.solve_x(Xvalue))
            return result


def test_poly():
    p1 = Poly([1, -2, 1])  # poly of grade 2: p1(X)=1-2X+X2
    p2 = Poly((0, 1))  # create poly of grade 1 with a tuple: p2(X)=X, (a0==0)
    print(p1)  # print calls __str__ and prints 1.0-2.0X+X^2
    print(p1 == p2)  # returns False
    print(p1 == Poly((1, -2, 1)))  # return True
    print(p1 != p2)  # returns True
    p3 = p1 + p2  # sum, __add__
    print(p3)  # prints 1.0-X+X^2.0 (use default number of decimals)
    print(p1[1])  # indexing the coefficients: returns -2 (a1 for p1)
    p4 = p2 * p1  # product with another Poly: p4 becomes X-2X^2+X^3
    p5 = p1 * 2  # product with int or float: p5 becomes 2-4X+2X^2
    p6 = 3 * p1  # product with int or float: p6 becomes 3-6X+3X^2 (__rmul__)
    print(p4)
    print(p5)
    print(p6)
    print(p1.eval(2))  # evaluate p1 at point 2: prints 1.0
    print(p1.eval([0, -1, 1]))  # evaluate p1 for a list of points: prints [1,4,0]


test_poly()
