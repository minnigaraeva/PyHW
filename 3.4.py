def deg(x, y):
    res = x
    for i in range(1, abs(y)):
        res = res * x
    res = 1 / res
    print(f'x ** y = {res:.10f}')


deg(float(input('Enter a valid positive number')), int(input(f'Enter a negative integer')))
