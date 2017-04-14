import os


def ed_read(filename: str, from_index: int = 0, to: int = -1):
    """
    returns as a string the content of the file named filename, with
    file positions in the half-open range [from, to). If to == -1, the content between from and the end of
    the file will be returned. If parameter to exceeds the file length, then the function raises exception
    ValueError with a corresponding error message.
    :param filename: file to be read
    :param from_index: min index to start reading from
    :param to: max index to stop reading at
    :return: None
    """
    try:
        with open(filename, mode='r', encoding="utf8") as file:
            validate_file_read(file, from_index, to)
            if to == -1:
                print(file.read()[from_index:])
            else:
                print(file.read()[from_index:to])

    except OSError:
        return
    except (RuntimeError, TypeError, NameError):
        return
    return


def validate_file_read(file, from_index, to):
    """
    This will check that from_index and to are valid indexes in the file otherwise raise ValueError
    :param file: file to check
    :param from_index: min index
    :param to: max index
    :return: None
    """
    f_length = len(file.read())
    if from_index > f_length or from_index < 0 or to > f_length:
        raise ValueError
    if to != -1 and from_index > to:
        raise ValueError
    file.seek(0)


def ed_find(filename, search_str):
    """
    finds string search_str in the file named by filename and returns a
    list with index positions in the file text where the string search_str is located. E.g. it returns [4, 100]
    if the string was found at positions 4 and 100. It returns [] if the string was not found.
    :type filename: str
    :param filename: file to be searched
    :param search_str: string to search
    :return: list of indexes found
    """
    try:
        search_indexes = []
        with open(filename, mode='r', encoding="utf8") as file:
            contents = file.read()
            f_length = len(contents)
            search_len = len(search_str)
            current_index = 0
            while current_index + search_len < f_length:
                result = contents.find(search_str, current_index)
                if result != -1:
                    search_indexes.append(result)
                    current_index = result + search_len
                else:
                    break
        return search_indexes
    except OSError:
        return


def ed_replace(filename, search_str, replace_with, occurrence=-1):
    """
    replaces search_str in the file
    named by filename with string replace_with. If occurrence==-1, then it replaces ALL occurrences.
    If occurrence>=0, then it replaces only the occurrence with index occurrence, where 0 means the
    first, 1 means the second, etc. If the occurrence argument exceeds the actual occurrence index in
    the file of that string, the function does not do the replacement. The function returns the number of
    times the string was replaced.
    :param filename: file to be manipulated
    :param search_str: string to be searched and replaced
    :param replace_with: string that is used to replace search_str
    :param occurrence: the exact occurrence in the file or all for occurrence = -1
    :return: number of strings replaced
    """
    try:
        search_indexes = ed_find(filename, search_str)
        if len(search_indexes) == 0 or len(search_indexes) - 1 < occurrence or occurrence < -1:
            return 0
        with open(filename, mode='r+', encoding="utf8") as file:
            replace_count = 0
            contents = file.read()
            file.seek(0)
            file.truncate()
            search_len = len(search_str)
            if occurrence == -1:
                replaced = contents
                index = replaced.find(search_str)
                while index != -1:
                    replace_count += 1
                    replaced = replaced[:index] + replace_with + replaced[index + search_len:]
                    index = replaced.find(search_str)
                file.write(replaced)
                return replace_count
            replace_count = 1
            index = search_indexes[occurrence]
            replaced = contents[:index] + replace_with + contents[index + search_len:]
            file.write(replaced)
            return replace_count
    except OSError:
        return 0


def ed_append(filename, string):
    """
    appends string to the end of the file. If the file does not exist, a new
    file is created with the given file name. The function returns the number of characters written to the
    file.
    :param filename: file to be manipulated
    :param string: string to be appended
    :return: number of characters written
    """
    try:
        from pathlib import Path
        if Path(filename).is_file():
            with open(filename, mode='r+', encoding="utf8") as file:
                file.read()
                file.write(string)
                return len(string)
        else:
            with open(filename, mode='w', encoding="utf8") as file:
                file.write(string)
                return len(string)
    except IOError:
        return 0


def validate_file_tuple(filename, pos_str_col: list):
    """
    this will validate each item in the pos_str_col collection and make sure that the first value in the
    tuple is not < 0 and that it is not > max length of the original file otherwise raise ValueError
    :param filename:
    :param pos_str_col:
    :return:
    """
    with open(filename, mode='r', encoding="utf8") as file:
        max_length = len(file.read())
        for str_col in pos_str_col:
            if str_col[0] < 0 or str_col[0] > max_length:
                raise ValueError("invalid position ", str_col[0])


def ed_write(filename, pos_str_col):
    """
    for each tuple (position, s) in collection pos_str_col (e.g. a list)
    this function writes to the file at position pos the string s. This function overwrites some of the
    existing file content. If any position parameter is invalid (< 0) or greater than the file contents size,
    the function does not change the file and raises ValueError with a proper error message. In case of
    no errors, the function returns the number of strings written to the file. Assume the strings to be
    written do not overlap.
    :param filename: file to be manipulated
    :param pos_str_col: collection of tuples
    :return: number of strings added
    """
    validate_file_tuple(filename, pos_str_col)
    with open(filename, mode='r+', encoding="utf8") as file:
        for str_col in pos_str_col:
            file.seek(str_col[0])
            file.write(str_col[1])
        return len(pos_str_col)


def ed_insert(filename, pos_str_col):
    """
    for each tuple (position, s) in collection pos_str_col (e.g. a list)
    this function inserts into to the file content the string s at position pos. This function does not
    overwrite the existing file content, as seen in the examples below. If any position parameters is
    invalid (< 0) or greater than the original file content length, the function does not change the file at
    all and raises ValueError with a proper error message. In case of no errors, the function returns the
    number of strings inserted to the file.
    :param filename: file to be manipulated
    :param pos_str_col: collection of tuples
    :return: number of strings added
    """
    validate_file_tuple(filename, pos_str_col)
    with open(filename, mode='r+', encoding="utf8") as file:
        for str_col in pos_str_col:
            file.seek(0)
            contents = file.read()
            file.seek(0)
            contents = contents[:str_col[0]] + str_col[1] + contents[str_col[0]:]
            file.truncate()
            file.write(contents)
        return len(pos_str_col)


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


def test_ed_write():
    test_name = "test write"
    test_fn = "test.txt"
    from pathlib import Path
    if Path(test_fn).is_file():
        os.remove(test_fn)
    initial_text = "abcdefg"
    with open(test_fn, mode='w', encoding="utf8") as test_f:
        test_f.write(initial_text)
    try:
        new_text = [(0, "0123")]
        ret = ed_write(test_fn, new_text)
        expected_text = "0123efg"
        current_text = ""
        with open(test_fn, mode="r", encoding="utf8") as test_f:
            current_text = str(test_f.read())
        cond = (ret == len(new_text) and (current_text == expected_text))
        return testif(cond, test_name)
    except Exception as exc:
        print("Test {} failed due to exception: {}\n".format(test_name, str(exc)))
        return False


def test_ed_replace():
    test_name = "test write"
    test_fn = "test.txt"
    from pathlib import Path
    if Path(test_fn).is_file():
        os.remove(test_fn)
    initial_text = "abcdefg"
    with open(test_fn, mode='w', encoding="utf8") as test_f:
        test_f.write(initial_text)
    try:
        replace_text = "0123"
        search_text = "cde"
        ret = ed_replace(test_fn, search_text, replace_text)
        expected_text = "ab0123fg"
        current_text = ""
        with open(test_fn, mode="r", encoding="utf8") as test_f:
            current_text = str(test_f.read())
        cond = (ret == 1 and (current_text == expected_text))
        return testif(cond, test_name)
    except Exception as exc:
        print("Test {} failed due to exception: {}\n".format(test_name, str(exc)))
        return False
