def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0

    new_arr = arr
    new_arr.sort()
    new_arr.pop(0)
    new_arr.pop(len(new_arr) - 1)

    return sum(new_arr)
