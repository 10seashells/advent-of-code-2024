
import re
eqs = []
with open('7/input.txt') as f:
    for line in f.readlines():
        values = re.split(':\s|\s', line.strip())
        int_values = []
        for value in values:
            int_values.append(int(value))
        eqs.append(int_values)

def calc(result, vals):
    if vals[0]>result:
        return False
    add = vals[0]+vals[1]
    mult = vals[0]*vals[1]
    concat = int(str(vals[0])+str(vals[1]))
    if len(vals) == 2:
        return add == result or mult == result or concat == result
    elif len(vals) == 3:
        return calc(result, [mult]+[vals[2]]) or calc(result, [add]+[vals[2]]) or calc(result, [concat]+[vals[2]])
    else:
        return calc(result, [mult]+vals[2:]) or calc(result, [add]+vals[2:]) or calc(result, [concat]+vals[2:])

total_valid = 0
for eq in eqs:
    if calc(eq[0],eq[1:]):
        total_valid += eq[0]
print(total_valid)