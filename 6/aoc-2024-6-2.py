import copy

original_map = []
with open('6/input.txt') as f:
    for line in f.readlines():
        original_map.append(list(line))
map = copy.deepcopy(original_map)

x = -1
y = -1
#find the guard
for i in range(len(map)-1):
    for j in range(len(map[0])-1):
        if map[i][j] in ['^','>','v','<']:
            x = j
            y = i


#enter first position into moves
first_move = [x,y]
moves = [first_move]
original_guards = ['^']

def move():
    global x
    global y
    global map
    guard = map[y][x]
    guard90 = ''
    x_rel = 0
    y_rel = 0
    if guard == '^':
        y_rel = -1
        guard90 = '>'
    elif guard == '>':
        x_rel = 1
        guard90 = 'v'
    elif guard == 'v':
        y_rel = 1
        guard90 = '<'
    elif guard == '<':
        x_rel = -1 
        guard90 = '^'   

    # if target move is out of bounds
    if x+x_rel < 0 or x+x_rel >= len(map[0]) or y+y_rel < 0 or y+y_rel >= len(map):
        return False
    # if target move is blocked
    elif map[y+y_rel][x+x_rel] == '#':
        map[y][x] = guard90
        return move()
    # move normally
    map[y+y_rel][x+x_rel] = guard
    map[y][x] = '.'
    x += x_rel
    y += y_rel
    moves.append([x,y])
    original_guards.append(guard)
    return True

still_moves = True
while (still_moves):
    still_moves = move()

unique_moves = []
for pos in moves:
    if pos not in unique_moves:
        unique_moves.append(pos)

print('unique_moves:',len(unique_moves))

original_moves = copy.copy(moves)

def check_loop_moves():
    if len(moves)<5:
        return False
    second_last = moves[len(moves)-2]
    last = moves[len(moves)-1]
    for i in range(len(moves)-4):
        if moves[i] == second_last and moves[i+1] == last:
            return True
    return False

obstacles = []


k = 0
prev_pos=[-1,-1]
map = copy.deepcopy(original_map)
for i in range(len(original_moves)-1):
    
    #reset previous placed obstacle
    if not (prev_pos[0]==-1 and prev_pos[1]):
        map[prev_pos[1]][prev_pos[0]]='.'
    #reset previous guard
    map[y][x]='.'

    pos = original_moves[i+1]
    x = original_moves[i][0]
    y = original_moves[i][1]
    moves = [[x,y]]
    map[y][x] = original_guards[i]
    map[pos[1]][pos[0]] = '#'
    if pos in obstacles:
        prev_pos=pos
        continue
    m = 0
    while True:
        still_moves = move()
        if not still_moves:
            break
        #check for looping less frequently to run faster
        if m%1000 == 0:
            if check_loop_moves():
                obstacles.append([pos[0],pos[1]])
                break
        m +=1
    k +=1
    if k%100 == 0:
        print(k)
    prev_pos=pos

print('obstacles:',obstacles)
print(len(obstacles))

unique_obstacles = []
for pos in obstacles:
    if pos not in unique_obstacles:
        unique_obstacles.append(pos)

print('unique_obstacles:',unique_obstacles)
print(len(unique_obstacles))

print(first_move in obstacles)
'''
3,6
6,7
7,7
1,8
3,8
7,9


1685 too high
1684 too high
'''
