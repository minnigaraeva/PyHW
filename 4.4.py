import random

my_list = [random.randint(1, 9) for el in range(1, 15)]
print(my_list)
unrepeated = []
for elem in my_list:
    if my_list.count(elem) == 1:
        unrepeated.append(elem)
print(unrepeated)
