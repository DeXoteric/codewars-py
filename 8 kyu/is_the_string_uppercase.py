# Link: https://www.codewars.com/kata/56cd44e1aa4ac7879200010b


def is_uppercase(inp):
    for i in inp:
        if i.islower():
            return False
    return True
