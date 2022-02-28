def from_string(*args):
    string = '0'
    su = 0
    while string.count('br') == 0:
        string = input('Enter numbers separated by a space')
        for e in string.split():
            if e != 'br':
                a = float(e)
                su += a
            else:
                break
        print(su)
    print(f'Final sum is {su}')


from_string()





