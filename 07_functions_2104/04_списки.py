a = [5, 12, 7, 8, 4, 9, 0, 13, 1, 6]


def sum_list(array: list) -> int:
    s = 0
    for i in range(len(array)):
        s += array[i]
    return s


print(sum_list(a))
