# Link: https://www.codewars.com/kata/57a083a57cb1f31db7000028


def powers_of_two(n):
    numbers = []
    for i in range(n + 1):
        numbers.append(2**i)
    return numbers
