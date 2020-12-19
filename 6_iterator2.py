from itertools import cycle
import random


def iter_list(old_list):
    exit = 0
    for n in cycle(old_list):
        if exit == 100:
            break
        exit += 1
        print(n)


old_list = list(random.randint(0, 1000) for el in range(0, random.randint(0, 20)))
print(old_list)
iter_list(old_list)