"""
Link: https://www.codewars.com/kata/55fd2d567d94ac3bc9000064

Description:

Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
"""


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
