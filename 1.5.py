revenue = int(input('Введите знчение выручки '))
costs = int(input('Введите сумму издержек '))
if revenue > costs:
    print('Поздравляю! Вы работаете с прибылью!')
elif revenue < costs:
    print('Осторожно! Вы несете убытки!')
elif revenue == costs:
    print('Присмотритесь, вы работаете в ноль.')