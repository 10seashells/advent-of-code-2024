import copy

map = []
with open('12/input_tiny.txt') as f:
    for line in f.readlines():
        map.append(line.strip())

def is_valid_loc_bool(loc):
    if (loc[0] in range(len(map)) and 
        loc[1] in range(len(map[0]))):
        return True
    return False

def is_valid_loc(loc):
    if (loc[0] in range(len(map)) and 
        loc[1] in range(len(map[0]))):
        return loc
    return []

def get_dir_value(plot, dir):
    pos = [sum(x) for x in zip(plot.loc, dir)]
    if (pos[0] in range(len(plot_map)) and 
        pos[1] in range(len(plot_map[0]))):
        return plot_map[pos[0]][pos[1]]
    return False

class Plot:
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc

    def __str__(self):
        return f"{self.name}({self.loc})"
    
    def get_sides(self):
        sides = [x for x in [self.up,self.down,self.left,self.right] if x]
        return sides
    
class Region:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.plots = []
    def __str__(self):
        return f"{self.plots}"
    



plot_map = []
def create_plots():
    global plot_map
    plot_map = [[Plot(map[i][j],[i,j]) for i in range(len(map))] for j in range(len(map[0]))]
    for i,e in enumerate(plot_map):
        for j,plot in enumerate(e):
            plot.up = get_dir_value(plot,[-1,0])
            plot.down = get_dir_value(plot,[1,0])
            plot.left = get_dir_value(plot,[0,-1])
            plot.right = get_dir_value(plot,[0,1])
    print(plot_map)
            

groups = {}
def create_groups():
    global plot_map
    print(plot_map)
    for i,e in enumerate(plot_map):
        print('creating groups')
        for j,plot in enumerate(e):
            names = [x for x in groups.keys() if x[0]==plot.name[0]]
            print('names:',names)
            if len(names)==0: 
                print('new group created')
                groups[plot.name+'-'+str(i)+'-'+str(j)] = create_groups_inner([],plot.name[0],plot)
            else:
                is_counted = False
                for name in names:
                    if plot in groups[name]:
                        is_counted = True
                        break
                if not is_counted:
                    print('added to group')
                    groups[plot.name+'-'+str(i)+'-'+str(j)] = create_groups_inner([],plot.name[0],plot)
   
def create_groups_inner(visited,name,plot):
    if not plot.name==name:
        return []
    group = [plot]
    for side in plot.get_sides():
        if side.name==name:
            if side not in group: 
                if not (visited and side in visited):
                    vis = copy.deepcopy(visited)
                    vis.append(plot)
                    group += create_groups_inner(vis,name,side)
    print('group:',group)
    return group

def get_num_perim_sides(plot,locs):
    num = 4
    for side in plot.get_sides():   
        if side in locs:
            num -=1
    return num

create_plots()
create_groups()
price = 0
for group, plots in groups.items():
    perim = 0
    area = len(plots)
    for plot in plots:
        perim += get_num_perim_sides(plot,plots)
    price += area*perim
    print(group,' price = area ',area,' * perim ',perim)
print(price)


'''
AAAA
BBCD
BBCC
EEEC

.x.x.x.x.
xA.A.A.Ax
.x.x.x.x.
xB.BxC.D.
.........
xB.BxC.D.
.x.x.....
.E.E.E.C.
.........

make graphs of each region
area = total num in group
perimeter = sum of sides of all in group that do not border same type

'''