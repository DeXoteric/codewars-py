def friend(x):
    new_list = []
    for i in x:
        if len(i) == 4:
            new_list.append(i)
    return new_list
