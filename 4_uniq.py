import random


def uniq_list(old_list):
    new_list = []
    for n in range(len(old_list)):
        if old_list[n] not in new_list:
            new_list.append(old_list[n])
    return new_list


old_list = list(random.randint(0, 5) for el in range(0, random.randint(20, 30)))
print(old_list)
print(uniq_list(old_list))



