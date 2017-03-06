import math
import locale
locale.setlocale(locale.LC_ALL, '')


def get_change(x, y):
    return {"change": math.floor(x / y),
            "left_over": (math.ceil((x - math.floor(x / y) * y) * 100) / 100)}


while 1:
    cash = float(input("Enter amount: "))
    if cash < 0:
        print("Invalid input.")
        continue
    change = get_change(cash, .25)
    quarters = change["change"]
    change = get_change(change["left_over"], .10)
    dimes = change["change"]
    pennies = math.ceil(change["left_over"]*100)
    print(locale.currency(cash, grouping=True),
          "makes ", quarters, " quarters, ", dimes, " dimes, and ", pennies,
          " pennies (", quarters + dimes + pennies, " coins), total amount in coins: ",
          locale.currency(cash, grouping=True), ".")
