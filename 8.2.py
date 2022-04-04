class MyError(Exception):
    pass


num1 = float(input('Enter a number'))
num2 = float(input('Enter another number'))
try:
    if num2 == 0:
        raise MyError('Zero is not ok for division')
except MyError as err:
    print(err)
else:
    print(f'Result of division is {num1 / num2:.2f}')
finally:
    print('The end')




