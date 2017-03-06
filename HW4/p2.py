import copy


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


p1 = Poly([1, -2, 1])
p2 = Poly((0, 1))
