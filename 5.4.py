with open('lesson5HW4.txt') as f, open('lesson5HW41.txt', 'w', encoding='utf-8') as f2:
    numbers = f.readlines()
    dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for number in numbers:
        eng = number.split()
        print(f'{dic[eng[0]]} - {eng[2]}', file=f2)
