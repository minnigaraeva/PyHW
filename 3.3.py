def my_func(num1, num2, num3):
    res = num1 + num2 + num3 - min(num1, num2, num3)
    print(f'The sum of two largest numbers is {res}')


my_func(float(input('Enter a number a')), float(input('Enter a number b')), float(input('Enter a number c')))
