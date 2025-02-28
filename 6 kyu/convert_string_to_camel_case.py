# Link: https://www.codewars.com/kata/517abf86da9663f1d2000003

import re


def to_camel_case(text):
    words = re.split("_|-", text)
    new_string = words.pop(0)
    for i in words:
        new_string += i.capitalize()
    return new_string


# Cleaner solution:
# def to_camel_case(text):
#     words = re.split("_|-", text)
#     words[1:] = list(map(str.capitalize, words[1:]))
#     return "".join(words)
