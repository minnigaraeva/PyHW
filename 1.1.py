name = input('Как Вас зовут? ')
a = 9
b = 7
print("а + b = ", a + b)
c = int(input("Введите целое число с "))
print(f"c + a = {c + a:.2f}")
e = int(input('чему равно b? '))
if e == b:
    print(f'Поздравляю {name:>10}')
else:
    print(f"Ну {name}, это же простая арифметика")


