months = [12, ]
n = 0
while n < 11:
    months.append(n + 1)
    n += 1
print(months)
m = int(input('Введите номер месяца'))
a = months.index(m)
if a < 3:
    print('winter')
elif 2 < a < 6:
    print('spring')
elif 5 < a < 9:
    print('summer')
elif a > 8:
    print('autumn')


