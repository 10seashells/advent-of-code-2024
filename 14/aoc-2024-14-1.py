import re
robots = []

def half(len):
    return [[0,int(len/2-1)],[int(len/2+1),len-1]]

#map_size = {'x':11,'y':7}
map_size = {'x':101,'y':103}
top_left = [half(map_size['x'])[0],half(map_size['y'])[0]]
top_right = [half(map_size['x'])[1],half(map_size['y'])[0]]
bottom_left = [half(map_size['x'])[0],half(map_size['y'])[1]]
bottom_right = [half(map_size['x'])[1],half(map_size['y'])[1]]

print(top_left)
with open('14/input.txt') as f:
    for line in f.readlines():
        robot = {}
        nums = [int(x) for x in re.findall('-?\d+',line)]
        robot['pos'] = [nums[0],nums[1]]
        robot['velocity'] = [nums[2],nums[3]]
        robots.append(robot)
print(robots)

def is_in_area(robot, quad):
    if quad[0][0]<=robot['pos'][0]<= quad[0][1] and quad[1][0]<=robot['pos'][1]<= quad[1][1]:
        return True
    return False

def get_total_safety():
    total = [0,0,0,0]
    for robot in robots:
        if is_in_area(robot,top_left):
            total[0]+=1
        elif is_in_area(robot,top_right):
            total[1]+=1
        elif is_in_area(robot,bottom_left):
            total[2]+=1
        elif is_in_area(robot,bottom_right):
            total[3]+=1
    return total[0]*total[1]*total[2]*total[3]

def move(robot,secs):
    movement = [x*secs for x in robot['velocity']]
    newpos = [sum(x) for x in zip(robot['pos'],movement)]

    if newpos[0]<0:
        print(newpos[0] % (map_size['x']-1) + map_size['x'])
        newpos[0] = newpos[0] % map_size['x'] + map_size['x']
    if newpos[0]> map_size['x']-1:
        newpos[0] %= map_size['x']

    if newpos[1]<0:
        newpos[1] = newpos[1] % map_size['y'] + map_size['y']
    if newpos[1]> map_size['y']-1:
        newpos[1] %= map_size['y']
    robot['pos']=newpos

def print_map():
    map = [[0]*(map_size['x']) for i in range(map_size['y'])]
    for robot in robots:
        map[robot['pos'][1]][robot['pos'][0]] +=1
    for line in map:
        print(line)


secs = 100
for robot in robots:
    move(robot, secs)

#print_map()
print(get_total_safety())
