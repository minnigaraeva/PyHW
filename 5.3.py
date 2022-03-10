with open('lesson5HW3.txt', 'r', encoding='utf-8') as f:
    workers = f.read().splitlines()
low_pay = []
payment = 0
num = 0
for worker in workers:
    base = worker.split()
    payment += float(base[1])
    num += 1
    if float(base[1]) < 20000:
        low_pay.append(base[0])
print(f'Average salary is: {payment / num:.2f}')
print(f'Low-paid workers are: \n{low_pay}')
