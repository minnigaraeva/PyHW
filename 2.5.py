l = [8, 6, 5, 5, 2]
n = int(input('Введите натуральное число'))
b = l.count(n)
if b > 0:
    a = l.index(n)
    l.insert(a + b, n)
else:
    num = 0
    while n < l[num]:
        num += 1
        if num >= len(l):
            break
    l.insert(num, n)
print(l)
