import random

first_list = [random.randint(1, 600) for el in range(1, 16)]
print(first_list)
a = 601
new_list = []
for elem in first_list:
    if elem > a:
        new_list.append(elem)
    a = elem
print(new_list)

