import re
import copy

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
                    boxes.append([[height,width*2],[height,(width*2)+1]])
                elif line[width]=='@':
                    robot = [height,width*2]
                elif line[width]=='#':
                    walls.append([height,width*2])
                    walls.append([height,width*2+1])
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
    height +=1
    width = (width-1)*2
print('walls:',walls)
print('boxes:',boxes)
print('robot:',robot)

def can_move(box, ins):
    boxes_copy = copy.deepcopy(boxes)
    box_target = [[sum(x) for x in zip(box[0],ins)],[sum(x) for x in zip(box[1],ins)]]
    if box_target[0] in walls or box_target[1] in walls:
        return False
    elif box_target in boxes:
        if not can_move(box_target,ins):
            return False

def move(box, ins, boxes):
    box_target = [[sum(x) for x in zip(box[0],ins)],[sum(x) for x in zip(box[1],ins)]]
    if box_target[0] in walls or box_target[1] in walls:
        return False
    elif box_target in boxes:
        if not move(box_target,ins,boxes):
            return False
    else:
        to_move = [False,False]
        box0 = get_box(box_target[0])
        if box0 == box:
            box0 = False
        box1 = get_box(box_target[1])
        if box1 == box:
            box1 = False
        if box0 and move(box0,ins,copy.deepcopy(boxes)):
            to_move[0] = True
        if box1 and move(box1,ins,copy.deepcopy(boxes)):
            to_move[1] = True
        if box0 and box1 and to_move==[True,True]:
            move(box0,ins,boxes)
            move(box1,ins,boxes)
        elif box0 and not box1: 
            if to_move[0]==True:
                move(box0,ins,boxes)
            else: return False
        elif box1 and not box0:
            if to_move[1]==True:
                move(box1,ins,boxes)
            else: return False
        elif box0 and box1 and False in to_move:
            return False

    print('moving box from ',box,' to ',box_target)
    boxes.remove(box)
    boxes.append(box_target)
    print('moved box from ',box,' to ',box_target)
    return True

def get_box(pos):
    for box in boxes:
        if pos == box[0] or pos == box[1]:
            return box
    return False

def print_map():
    for i in range(height):
        for j in range(width):
            if [i,j] == robot:
                print('@',end='')
            elif get_box([i,j]):
                print('O',end='')
            elif [i,j] in walls:
                print('#',end='')
            else:
                print('.',end='')
        print('')
print_map()
i = 0
for ins in instruct:
    target = [sum(x) for x in zip(robot,ins)]
    box = get_box(target)
    if box:
        if move(box,ins,boxes):
            robot = target
    elif target not in walls:
        robot = target
    if i>3710:
        print(ins)
        print_map()
    i +=1
    print('i:',i)

print(robot)
print(boxes)
print(100*sum([x[0][0] for x in boxes])+sum([x[0][1] for x in boxes]))
print_map()
'''
1314658 too low
'''