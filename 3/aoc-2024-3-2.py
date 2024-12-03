import re

text = []   
sum = 0     

with open('3/input.txt') as f:
    text = ''.join(f.readlines())

txt = "mul(1,1)"
muls = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", text)

do = True
for mul in muls:
    if (mul=="do()"):
        do = True
    elif (mul=="don't()"):
        do = False
    elif(do):
        nums = re.findall("\d+", mul)
        sum = sum + int(nums[0])*int(nums[1])

print(sum)