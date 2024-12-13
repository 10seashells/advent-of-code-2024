import re

machines = []
with open('13/input.txt') as f:
    
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
            instructions['prize'] = [x+10000000000000 for x in nums]
            machines.append(instructions)
            instructions = {}
            count = 0


def get_cost(machine):
    a_top = (machine['b'][1]*machine['prize'][0]-machine['b'][0]*machine['prize'][1])
    a_bottom = (machine['b'][1]*machine['a'][0]-machine['b'][0]*machine['a'][1])
    if not a_top%a_bottom==0:
        return 0
    a = int(a_top/a_bottom)
    b_top = machine['prize'][0] - machine['a'][0]*a
    b_bottom = machine['b'][0]
    if not b_top%b_bottom==0:
        return 0
    b = int(b_top/b_bottom)
    return 3*a+b if (b>=0 and a>=0) else 0


total = 0
for machine in machines:
    cost = get_cost(machine)
    total += cost
print(total)

'''
Ax*a + Bx*b = prizex
Ay*a + By*b = prizey
minimize a*3 + b

c = (prizex - bx*d) / ax
c = (prizey - by*d) / ay
d = (prizex - ax*c) / bx
d = (prizey - ay*c) / by

(prizex - bx*d) = (prizey - by*d) * (ax/ay) 

'''
