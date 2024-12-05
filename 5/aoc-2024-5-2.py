rules = []
updates = []
with open('5/input.txt') as f:
    for line in f.readlines():
        if '|' in line:
            rules.append(line.strip().split('|'))
        elif ',' in line:
            updates.append(line.strip().split(','))

def is_correct(update):
    for rule in rules:
        if set(rule).issubset(update) and update.index(rule[0]) > update.index(rule[1]):
            return False
    return True

def fix_update(update):
    while(not is_correct(update)):
        for rule in rules:
            if set(rule).issubset(update) and update.index(rule[0]) > update.index(rule[1]):
                a = update.index(rule[0])
                b = update.index(rule[1])
                temp = update[a]
                update[a] = update[b]
                update[b] = temp
    return update
    
total = 0
for update in updates:
    if not is_correct(update):
        fixed = fix_update(update)
        middle = int(fixed[len(fixed)//2])
        total += middle
print(total)
