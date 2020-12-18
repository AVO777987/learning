import random


# def rand_list(lenght):
#     my_list = []
#     for n in range(lenght):
#         my_list.append(random.randint(0, 1000))
#     return my_list


def max_list(old_list):
    new_list = []
    for n in range(len(old_list)):
        if n == 0:
            continue
        if old_list[n] > old_list[n-1]:
            new_list.append(old_list[n])
    return new_list


# old_list = rand_list(random.randint(10, 20))
old_list = list(random.randint(0, 1000) for el in range(0, random.randint(10, 20)))
print(old_list)
print(max_list(old_list))



