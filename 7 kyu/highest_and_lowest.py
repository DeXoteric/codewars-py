# Link: https://www.codewars.com/kata/554b4ac871d6813a03000035


def high_and_low(numbers):
    new_numbers = list(map(int, numbers.split()))

    return f"{max(new_numbers)} {min(new_numbers)}"
