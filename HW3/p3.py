import pylab


def get_csv_data(f, string_pos_lst, sep=","):
    bb_lst = list()
    line = f.readline()
    bb_lst.append(line.strip('\n').split(sep))

    while True:
        try:
            line = f.readline()
            if line == "":
                break

            line_lst = [x.strip('\n') for x in line.split(sep)]
            for x in range(0, len(line_lst)):
                if x not in string_pos_lst:
                    line_lst[x] = float(line_lst[x])
            bb_lst.append(line_lst)
        except:
            continue

    return bb_lst


def get_columns(data_lst, cols_lst):
    if not cols_lst:
        return []
    cols_result = list()
    try:
        cols_index = [x for x in range(0, len(data_lst[0])) if data_lst[0][x] in cols_lst]
        for y in cols_index:
            col = [data_lst[x][y] for x in range(1, len(data_lst))]
            cols_result.append(col)

        return cols_result
    except:
        return []


bb_file = open("lb-james.csv", "r")
bb_lst = get_csv_data(bb_file, [0, 2, 3, 4], ",")
print(bb_lst)
selected_cols_lst = get_columns(bb_lst, ["Age", "3P%", "2P%", "FT%"])
season = [x for x in get_columns(bb_lst, ["Season"])]
season = [int(x[:4]) for x in season[0]]
print(selected_cols_lst)
pylab.plot(season, selected_cols_lst[1], 'ro-', label="3P%")
pylab.plot(season, selected_cols_lst[2], 'go-', label="2P%")
pylab.plot(season, selected_cols_lst[3], 'bo-', label="FT%")
pylab.xlabel("Age")
pylab.ylabel("Percentage")
pylab.legend()
pylab.title("LeBron James shots on percentage")
pylab.show()
