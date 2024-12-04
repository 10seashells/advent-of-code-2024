import re

text = []   
sum = 0     

with open('3/input.txt') as f:
    text = ''.join(f.readlines())

muls = re.findall("mul\(\d+,\d+\)", text)

for mul in muls:
    nums = re.findall("\d+", mul)
    sum = sum + int(nums[0])*int(nums[1])

print(sum)