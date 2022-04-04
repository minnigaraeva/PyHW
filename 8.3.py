class CharacterError(Exception):
    pass


el = 0
the_list = []
while el != 'stop':
    el = input('Enter a number for list (to stop enter "stop")')
    try:
        if not el.isdigit():
            raise CharacterError('Need a number')
    except CharacterError as err:
        print(err)
    else:
        the_list.append(el)
print(the_list)

