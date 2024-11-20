"""
Link: https://www.codewars.com/kata/576b93db1129fcf2200001e6

Description:

Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

Example:

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6

Input validation:

If an empty value ( null, None, Nothing, nil etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.
"""


def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0

    new_arr = arr
    new_arr.sort()
    new_arr.pop(0)
    new_arr.pop(len(new_arr) - 1)

    return sum(new_arr)
