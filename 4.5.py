from functools import reduce

big_list = [el for el in range(100, 1001) if el % 2 == 0]


def mult(el, next_el):
    return el * next_el


print(reduce(mult, big_list))
