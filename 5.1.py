f = open('lesson5HW1.txt', 'w', encoding='utf-8')
mes = 'hi'
while len(mes) > 0:
    mes = input('Enter a text')
    print(mes, file=f)
f.close()
