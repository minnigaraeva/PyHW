time = int(input('Введите время в секундах '))
sec = time % 60
hrs = time // 3600
minutes = time % 3600 // 60
print(f'{hrs:02d}:{minutes:02d}:{sec:02d}')


