# Link: https://www.codewars.com/kata/57cc975ed542d3148f00015b


def check(seq, elem):
    return elem in seq


# Notes:
# Initially, this was my solution:
# def check(seq, elem):
#     return True if elem in seq else False
# However, thanks to a pylint warning, I learned that the solution could be simplified.
