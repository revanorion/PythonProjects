def input_tuple(a, b, c):
    try:
        user_input = str(input(a)).split(c)
        tuple_result = list()
        for x in range(0, len(b)):
            tuple_result.append(b[x](user_input[x]))
        return tuple(tuple_result)
    except:
        return ()


def input_tuple_lc(a, b, c):
    try:
        user_input = str(input(a)).split(c)
        return tuple([b[x](user_input[x]) for x in range(0, len(b))])
    except:
        return ()


def read_tuple(file_obj, types, sep):
    line = file_obj.readline().split(sep)
    return [types[x](line[x]) for x in range(0, len(types))]


def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing.
    param b: boolean, normally a tested condition: true if test passed, false otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True  ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)
    return b


try:
    print("Result: ", input_tuple("Enter first name, last name, age(float), ID(int), fulltime(bool): ",
                                  (str, str, float, int, bool), ","))
    print("Result: ", input_tuple("Enter first name, last name, age(float), ID(int), fulltime(bool): ",
                                  (str, str, float, int, bool), ","))
    f = open("cars.csv", "r")

    mycar = (make, model, mpg_float, modelYr_int, newcar_bool) = read_tuple(f, (str, str, float, int, bool), ",")
    print(mycar)
    f.close()
except:
    print("Error")
