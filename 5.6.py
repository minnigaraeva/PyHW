with open('lesson5HW6.txt') as f:
    info = f.read().splitlines()
dic = {}
for inf in info:
    scores = inf.replace("(", " ").split()
    value = 0
    for score in scores:
        if score.isdigit():
            value += int(score)
    dic[inf.split(':')[0]] = value
print(dic)
