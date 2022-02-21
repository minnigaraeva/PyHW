l = [22, 3.9, 'ListPractice', True, [1, 3, 5]]
l.append(input('Напишите что-нибудь'))
print(l)
b = len(l)
n = 0
a = 0
while n < b:
    a = l[n]
    print(f'Тип {n} элемента списка - {type(a)}')
    n += 1



