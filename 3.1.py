def div(num1, num2):
    print(f'Результат деления {num1 / num2}')


a = float(input('Print number 1'))
b = float(input('Print number 2 (not 0)'))
if b != 0:
    div(a, b)
else:
    print('Number 2 cannot be 0')
