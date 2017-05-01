import turtle

import math


# tree scope
def tree(length, depth):
    # noinspection PyUnresolvedReferences

    def binary_tree(length, depth):
        """
        draws a binary tree of length and depth
        :param length:
        :param depth:
        :return:
        """
        if depth == 0:
            return  # base case
        posx = turtle.xcor()
        posy = turtle.ycor()
        left(length, depth)
        turtle.up()
        turtle.goto(posx, posy)
        #turtle.dot()
        turtle.down()
        right(length, depth)

    # noinspection PyUnresolvedReferences

    def left(length, depth):
        """
        Left Side of the tree
        :param length:
        :param depth:
        :return:
        """
        turtle.setheading(240)
        turtle.forward(length)
        binary_tree(length / 2, depth - 1)

    # noinspection PyUnresolvedReferences

    def right(length, depth):
        """
        Right side of the tree
        :param length:
        :param depth:
        :return:
        """
        turtle.setheading(300)
        turtle.forward(length)
        binary_tree(length / 2, depth - 1)

    binary_tree(length, depth)


# noinspection PyUnresolvedReferences
def treemain():
    turtle.up()
    turtle.sety(200)
    turtle.down()
    turtle.delay(20)
    tree(160, 6)
treemain()

def power(x, n):
    """
    calculates the value of x to the power of n recursively
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    result = power(x, math.floor(n / 2))
    if n % 2 > 0:
        return x * result * result
    else:
        return result * result


def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing.
    :param b: boolean, normaly a tested conditionL true if passed, false otherwise
    :param testname: the test name
    :param msgOK: string to be printed if param b==True ( test condition true )
    :param msgFailed: string to be printed if param b==False ( tes condition false)
    :return: b
    """
    if b:
        print("Success: ", testname, "; ", msgOK)
    else:
        print("Failed: ", testname, "; ", msgFailed)
    return b


def test_power():
    test_name = "test power"

    try:
        cond = (2 ** 28 == power(2, 28))
        return testif(cond, test_name)
    except Exception as exc:
        print("Test {} failed due to exception: {}\n".format(test_name, str(exc)))
        return False


def slice_sum(lst, begin, end):
    """
    This takes am iterable object and does recursive sum between begin and end.
    :param lst: iterable object
    :param begin: beginning index
    :param end: ending index
    :return: begin index for list + recursive call
    """
    if begin > end or begin > len(lst) - 1 or end > len(lst) - 1:
        raise IndexError
    if begin < end:
        return lst.index(begin) + slice_sum(lst, begin + 1, end)
    return 0


def slice_sum_m(lst, begin, end):
    """
    This takes am iterable object and does recursive sum between begin and end. It caches results for sums of begin
     and end in a global list of tuples
    :param lst: iterable object
    :param begin: beginning index
    :param end: ending index
    :return: begin index for list + recursive call
    """
    if begin > end or begin > len(lst) - 1 or end > len(lst) - 1:
        raise IndexError
    if (begin, end) not in lst_dict:
        if begin < end:
            lst_dict[(begin, end)] = lst.index(begin) + slice_sum_m(lst, begin + 1, end)
        else:
            return 0
    return lst_dict[(begin, end)]


def test_slice_sum():
    test_name = "test slice sum"

    try:
        lst = (0, 1, 2, 3, 4, 5)
        cond = (sum(lst[2:5]) == slice_sum(lst, 2, 5))
        testif(cond, test_name)
    except Exception as exc:
        print("Test {} failed due to exception: {}\n".format(test_name, str(exc)))
        return False


def test_slice_sum_m():
    test_name = "test slice sum m"

    try:
        lst = (0, 1, 2, 3, 4, 5)
        cond = (sum(lst[2:5]) == slice_sum_m(lst, 2, 5))
        testif(cond, test_name)
        cond = (sum(lst[3:5]) == slice_sum_m(lst, 3, 5))
        testif(cond, test_name)
        cond = (sum(lst[0:5]) == slice_sum_m(lst, 0, 5))
        testif(cond, test_name)
    except Exception as exc:
        print("Test {} failed due to exception: {}\n".format(test_name, str(exc)))
        return False


lst_dict = {}
test_slice_sum_m()
input()