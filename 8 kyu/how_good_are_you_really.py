# Link: https://www.codewars.com/kata/5601409514fc93442500010b


def better_than_average(class_points, your_points):
    total_class_points = 0
    for points in class_points:
        total_class_points += points
    average = total_class_points / len(class_points)
    return your_points > average
