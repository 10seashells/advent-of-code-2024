stones = []
with open('11/input.txt') as f:
    for line in f.readlines():
        stones = [int(x) for x in line.split(' ')]

def blink(): 
    i = 0
    while i<len(stones):
        val = str(stones[i])
        if stones[i] == 0:
            stones[i] = 1
        elif len(val) % 2 == 0:
            stones[i] = int(val[:int(len(val)/2)])
            stones.insert(i+1,int(val[int(len(val)/2):]))
            i +=1
        else:
            stones[i] *= 2024
        i +=1

for i in range(25):
    blink()
print(len(stones))