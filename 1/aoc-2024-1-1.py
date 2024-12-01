
list1 = []
list2 = []

with open('input.txt') as f:
    for line in f.readlines():
        l = line.split()
        list1.append(int(l[0]))
        list2.append(int(l[1]))

list1.sort()
list2.sort()

total = 0
for i in range (len(list1)):
    total = total + abs(list1[i]-list2[i])

print(total)
