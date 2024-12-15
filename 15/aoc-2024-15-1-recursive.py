import re

boxes = []
robot = []
instruct = []
walls = []
height = -1
width = 0
with open('15/input.txt') as f:
    for line in f.readlines():
        if(line[0]=='#'):
            height +=1
            width = 0
            while width < len(line):
                if line[width]=='O':
                    boxes.append([height,width])
                elif line[width]=='@':
                    robot = [height,width]
                elif line[width]=='#':
                    walls.append([height,width])
                width +=1
        elif(not line[0]=='\n'):
            for char in line:
                if char=='<':
                    instruct.append([0,-1])
                elif char=='>':
                    instruct.append([0,1])
                elif char=='^':
                    instruct.append([-1,0])  
                elif char=='v':
                    instruct.append([1,0])

def move(box, ins):
    box_target = [sum(x) for x in zip(box,ins)]
    if box_target in walls:
        return False
    elif box_target in boxes:
        success = move(box_target,ins)
        if not success:
            return False
    boxes.remove(box)
    boxes.append(box_target)
    return True
        

for ins in instruct:
    target = [sum(x) for x in zip(robot,ins)]
    if target in boxes:
        success = move(target,ins)
        if success:
            robot = target
    elif target not in walls:
        robot = target

print(robot)
print(boxes)
print(100*sum([x[0] for x in boxes])+sum([x[1] for x in boxes]))
