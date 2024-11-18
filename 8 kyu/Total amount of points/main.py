def points(games):
    total_points = 0
    for i in games:
        if int(i[0]) > int(i[2]):
            total_points += 3
        if int(i[0]) == int(i[2]):
            total_points += 1
    return total_points


# Notes:
# - int() wasn't necessary
