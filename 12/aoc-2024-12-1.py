import copy

map = []
with open('12/input.txt') as f:
    for line in f.readlines():
        map.append(line.strip())

groups = {}
def create_groups():
    for i,e in enumerate(map):
        for j,f in enumerate(e):
            loc = [i,j]
            names = [x for x in groups.keys() if x[0]==f]
            if len(names)==0: 
                groups[f+'-'+str(i)+'-'+str(j)] = create_groups_inner([],f,loc)
            else:
                is_counted = False
                for name in names:
                    if loc in groups[name]:
                        is_counted = True
                        break
                if not is_counted:
                    groups[f+'-'+str(i)+'-'+str(j)] = create_groups_inner([],f,loc)
   
def create_groups_inner(visited,name,loc):
    if not map[loc[0]][loc[1]]==name:
        return []
    group = [loc]
    sides = get_sides(loc)
    for side in sides:
        if map[side[0]][side[1]]==name:
            if side not in group: 
                if not (visited and side in visited):
                    vis = copy.deepcopy(visited)
                    vis.append(loc)
                    g = create_groups_inner(vis,name,side)
                    group += g
            
    return group

def get_sides(loc):
    sides = []
    for dir in [[0,1],[0,-1],[1,0],[-1,0]]:
        side = [sum(x) for x in zip(loc, dir)]
        if (side[0] in range(len(map)) and 
            side[1] in range(len(map[0]))):
            sides.append(side)
    return sides

def get_num_perim_sides(loc,locs):
    num = 4
    sides = get_sides(loc)
    for side in sides:   
        if side in locs:
            num -=1
    return num

def get_num_perim_sides_old(loc,locs):
    num = 0
    for dir in [[0,1],[0,-1],[1,0],[-1,0]]:
        side = [sum(x) for x in zip(loc, dir)]
        if (side[0] in range(len(map)) and 
            side[1] in range(len(map[0]))):
            if not side in locs:
                num +=1
        elif (not side[0] in range(len(map)) or 
            not side[1] in range(len(map[0]))):
                num +=1
    return num

create_groups()

price = 0
for group, locs in groups.items():
    perim = 0
    area = len(locs)
    for loc in locs:
        perim += get_num_perim_sides(loc,locs)
    price += area*perim
    print(group,' price = area ',area,' * perim ',perim)
print(price)
