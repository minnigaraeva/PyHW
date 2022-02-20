n = int(input('Введите целое число '))
a = 1
while n // a > 0:
    a = a * 10
b = n + (n * a + n) + ((n * a + n) * a + n)
print(f'{n} + {n}{n} + {n}{n}{n} = {b}')


