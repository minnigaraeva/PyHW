def fact(n):
    a = 1
    for num in range(1, n + 1):
        a = a * num
        yield a


for el in fact(int(input('Enter a positive integer'))):
    print(el)
