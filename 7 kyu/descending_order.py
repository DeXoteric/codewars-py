# Link: https://www.codewars.com/kata/5467e4d82edf8bbf40000155


def descending_order(num):
    num = list(str(num))
    num.sort(reverse=True)
    num = "".join(num)
    return int(num)


# Best one-liner from Codewars:
# def Descending_Order(num):
#     return int("".join(sorted(str(num), reverse=True)))
