# Link: https://www.codewars.com/kata/55b42574ff091733d900002f


def friend(x):
    new_list = []
    for i in x:
        if len(i) == 4:
            new_list.append(i)
    return new_list
