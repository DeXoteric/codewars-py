def better_than_average(class_points, your_points):
    total_class_points = 0
    for points in class_points:
        total_class_points += points
    average = total_class_points / len(class_points)
    return your_points > average
