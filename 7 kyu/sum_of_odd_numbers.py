# Link: https://www.codewars.com/kata/55fd2d567d94ac3bc9000064


def row_sum_odd_numbers(n):
    first_number = 1 + (n - 1) * n
    sum_of_numbers = n * first_number + n * (n - 1)
    return sum_of_numbers


# Simpler solution found on Codewars:
# def not_my_solution(n):
#     return n**3


# For future reference:
# Centered Cubic Numbers
# Pyramidal Numbers
