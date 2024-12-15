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

for ins in instruct:
    target = [sum(x) for x in zip(robot,ins)]
    skip_move = False
    if not target in boxes:
        if target not in walls:
            robot = target
    else:
        box_target = [sum(x) for x in zip(target,ins)]
        next_box_target = [sum(x) for x in zip(box_target,ins)]
        if box_target in walls:
            skip_move = True
        while (box_target in boxes and not skip_move):
            if next_box_target in walls:
                skip_move = True
                break
            elif next_box_target in boxes:
                box_target = next_box_target
                next_box_target = [sum(x) for x in zip(box_target,ins)]
            else:
                box_target = next_box_target
                break
            
        if not skip_move:
            boxes.remove(target)
            boxes.append(box_target)
            robot = target
            
print(100*sum([x[0] for x in boxes])+sum([x[1] for x in boxes]))
