def printer_error(s):
    colors = list(map(chr, range(ord("a"), ord("m") + 1)))
    errors = 0
    input_length = len(s)
    s = list(s)
    for i in s:
        if i not in colors:
            errors += 1

    return f"{errors}/{input_length}"


# Notes:
# - variable "colors" was not necessary, if statement can be replaced by if i > "m"
# - converting "s" to list was also not necessary

# Best one-liner from Codewars:
# def printer_error(s):
#     return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
