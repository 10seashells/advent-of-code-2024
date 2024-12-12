import copy

map = []
with open('12/input_tiny_6.txt') as f:
    for line in f.readlines():
        map.append(line.strip())
print(map)
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

def get_group(loc):
    for group,locs in groups:
        if map[loc[0]][loc[1]] in locs:
            return group
        
def is_diag_in_shape(side1, side2, loc, locs):
    diag = [0,0]
    diag[0] = (loc[0]-(side2[0]-loc[0]) if side1[0]==loc[0] else loc[0]-(side1[0]-loc[0]))
    diag[1] = (loc[1]-(side2[1]-loc[1]) if side1[1]==loc[1] else loc[1]-(side1[1]-loc[1]))
    if diag in locs:
        return True
    return False
def is_diag_adjacent(side1,side2):
    if side1[0]==side2[0] or side1[1]==side2[1]:
        return False
    return True
'''def is_triag_in_shape(side1, loc, locs):
    sides = get_sides(loc)
    adj_sides = [side for side in sides if not is_diag_adjacent(side, side1)]
'''



def get_outside_corners(loc,locs):
    sides = get_sides(loc)
    sides = [side for side in sides if side in locs]
    corners = -1
    if len(sides) == 0:
        corners = 4
    elif len(sides) == 1:
        corners = 2
    elif len(sides) == 2:
        # if 2 sides across from each other other about loc
        if is_diag_adjacent(sides[0],sides[1]):
            corners = 0
        # if 2 sides next to each other about loc
        else:
            # if the opposite corner is part of shape
            if is_diag_in_shape(sides[0],sides[1],loc,locs):
                corners = 0
            else:
                corners = 1
            #corners = 1
    elif len(sides) == 3:
        corners = 0
    elif len(sides) == 4:
        corners = 0
    print('outside corners:',corners)
    return corners

def get_inside_corners(loc,locs):
    sides = get_sides(loc)
    sides = [side for side in sides if side in locs]
    corners = -1
    if len(sides) == 0:
        print('oops')
    elif len(sides) == 1:
        corners = 0
    elif len(sides) == 2:
        if is_diag_adjacent(sides[0],sides[1]):
            corners = 0
        else:
            #print('diagonal corner')

            corners = 1
    elif len(sides) == 3:
        #print('tri corner')
        corners = 2
    elif len(sides) == 4:
        #print(loc)
        #print('four corner')
        corners = 4
    return corners

def get_num_inside_corners(locs):
    outside_edge = []
    for loc in locs:
        for side in get_sides(loc):
            if (side[0] in range(len(map)) and 
                side[1] in range(len(map[0])) and 
                side not in locs and 
                side not in outside_edge):
                outside_edge.append(side)

    corners = 0
    for loc in outside_edge:
        corners+= get_inside_corners(loc,locs)
    print('inside corners:',corners)
    return corners

create_groups()

price = 0
for group, locs in groups.items():
    corners = 0
    area = len(locs)
    for loc in locs:
        corners += get_outside_corners(loc,locs)
    corners += get_num_inside_corners(locs)
    price += area*corners
    print(group,' price = area ',area,' * sides ',corners)
print(price)

'''


AAAA
BBCD
BBCC
EEEC

A
area=4
perim=10
outside corners=4
sides=4

B
area=4
perim=8
outside corners=4
sides=4

C
area=4
perim=10
outside corners=6
sides=8

D
area=1
perim=10
outside corners=4
sides=4

E
area=3
perim=8
outside corners=4
sides=4

4 outside corners

845887 too high

'''