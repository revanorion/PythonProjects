def ed_read(filename: str, from_index: int = 0, to: int = -1):
    """
    returns as a string the content of the file named filename, with
    file positions in the half-open range [from, to). If to == -1, the content between from and the end of
    the file will be returned. If parameter to exceeds the file length, then the function raises exception
    ValueError with a corresponding error message.
    :param filename:
    :param from_index:
    :param to:
    :return:
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
    :param filename:
    :param search_str:
    :return:
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
    :param filename:
    :param search_str:
    :param replace_with:
    :param occurrence:
    :return:
    """
    try:
        search_indexes = ed_find(filename, search_str)
        if len(search_indexes) == 0 or len(search_indexes) - 1 < occurrence or occurrence < -1:
            return
        with open(filename, mode='r+', encoding="utf8") as file:
            contents = file.read()
            file.seek(0)
            file.truncate()
            search_len = len(search_str)
            if occurrence == -1:
                replaced = contents
                index = replaced.find(search_str)
                while index != -1:
                    replaced = replaced[:index] + replace_with + replaced[index + search_len:]
                    index = replaced.find(search_str)
                file.write(replaced)
                return
            index = search_indexes[occurrence]
            replaced = contents[:index] + replace_with + contents[index + search_len:]
            file.write(replaced)
    except OSError:
        return


def ed_append(filename, string):
    """
    appends string to the end of the file. If the file does not exist, a new
    file is created with the given file name. The function returns the number of characters written to the
    file.
    :param filename:
    :param string:
    :return:
    """
    return


def ed_write(filename, pos_str_col):
    """
    for each tuple (position, s) in collection pos_str_col (e.g. a list)
    this function writes to the file at position pos the string s. This function overwrites some of the
    existing file content. If any position parameter is invalid (< 0) or greater than the file contents size,
    the function does not change the file and raises ValueError with a proper error message. In case of
    no errors, the function returns the number of strings written to the file. Assume the strings to be
    written do not overlap.
    :param filename:
    :param pos_str_col:
    :return:
    """
    return


def ed_insert(filename, pos_str_col):
    """
    for each tuple (position, s) in collection pos_str_col (e.g. a list)
    this function inserts into to the file content the string s at position pos. This function does not
    overwrite the existing file content, as seen in the examples below. If any position parameters is
    invalid (< 0) or greater than the original file content length, the function does not change the file at
    all and raises ValueError with a proper error message. In case of no errors, the function returns the
    number of strings inserted to the file.
    :param filename:
    :param pos_str_col:
    :return:
    """
    return


ed_read("file.txt")
print('*' * 10)
ed_replace("file.txt", "hello", "test")
print('*' * 10)
ed_read("file.txt")
# print(ed_find("file.txt", "tests"))
