import json

with open('lesson5HW7.txt') as f:
    info = f.readlines()
firms = {}
su = 0
num = 0
for inf in info:
    name, form, rev, costs = inf.split()
    prof = int(rev) - int(costs)
    firms[name] = prof
    if prof >= 0:
        su += prof
        num += 1
cons = [firms, {'average_profit': su / num}]
print(cons)

with open('lesson5.json', 'w', encoding='utf-8') as f:
    json.dump(cons, f)

