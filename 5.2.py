with open('lesson5HW2.txt', 'r', encoding='utf-8') as f:
    letter = f.read()
strings = letter.splitlines()
print(f'Number of lines: {len(strings)}\n\nNumber of words:')
for i in strings:
    print(f'{i} - {len(i.split())}')
