rules = []
updates = []
with open('5/input.txt') as f:
    for line in f.readlines():
        if '|' in line:
            rules.append(line.strip().split('|'))
        elif ',' in line:
            updates.append(line.strip().split(','))  
            
total = 0
correct = True
for update in updates:
    for rule in rules:
        if set(rule).issubset(update) and update.index(rule[0]) > update.index(rule[1]):
            correct = False
    if correct:
        total += int(update[len(update)//2])
    correct = True
print(total)
