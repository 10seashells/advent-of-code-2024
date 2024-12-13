import re

machines = []
with open('13/input_small.txt') as f:
    
    count = 0
    instructions = {}
    for line in f.readlines():
        nums = [int(x) for x in re.findall('\d+',line)]
        if count == 0 and re.match('Button A:',line):
            instructions['a'] = nums
            count +=1
        elif count == 1 and re.match('Button B:',line):
            instructions['b'] = nums
            count +=1
        elif count == 2 and re.match('Prize:',line):
            instructions['prize'] = nums
            machines.append(instructions)
            instructions = {}
            count = 0

max_presses=100
def get_cost(machine):
    best = []
    for a in range(max_presses):
        b = (machine['prize'][0] - machine['a'][0]*a) / machine['b'][0]
        if b.is_integer() and b>=0 and b == (machine['prize'][1] - machine['a'][1]*a) / machine['b'][1]:
            if best == [] or ((not best == []) and 3*a+b < 3*best[0]+best[1]):
                best = [a,b]
    cost = (0 if best == [] else 3*best[0]+best[1])
    return int(cost)

total = 0
for machine in machines:
    cost = get_cost(machine)
    total += cost
print(total)



'''
x = Ax*a + Bx*b = prizex
y = Ay*a + By*b = prizey
minimize a*3 + b

b = (18641 - 69*80) / 27
b = (prizex - Ax*a) / Bx

c = (prizex - bx*d) / ax
c = (prizey - by*d) / ay
d = (prizex - ax*c) / bx
d = (prizey - ax*c) / bx


'''
'''for machine in machines:
    get_winnable(machine)'''