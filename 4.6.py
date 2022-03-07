import itertools

"Итератор для целых чисел, начиная с указанного"
start = int(input('Enter a start number'))
for num in range(start, start + 10):
    print(num)

"Циклический итератор"
a = 0
input('Press Enter to start the second part')
for el in itertools.cycle('cycle'):
    if a > 10:
        break
    print(el)
    a += 1
