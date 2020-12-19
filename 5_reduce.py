from functools import reduce


def multi_list(el1, el2):
    return el1 * el2


old_list = list(el for el in range(100, 1001) if el % 2 == 0)
print(old_list)
print(reduce(multi_list, old_list))