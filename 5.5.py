with open('lesson5HW5.txt', 'w', encoding='utf=8') as f:
    print(input('Введите числа через пробел'), file=f)
with open('lesson5HW5.txt', 'r', encoding='utf=8') as f:
    nums = f.read().split()
su = 0
for num in nums:
    su += float(num)
print(su)
