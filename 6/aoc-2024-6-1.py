map = []

with open('6/input_small.txt') as f:
    for line in f.readlines():
        map.append(list(line))
x = -1
y = -1
#find the guard
for i in range(len(map)-1):
    for j in range(len(map[0])-1):
        if map[i][j] in ['^','>','v','<']:
            x = j
            y = i

#enter first position into moves
moves = [[x,y]]

def move():
    global x
    global y
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
    return True

still_moves = True
while (still_moves):
    still_moves = move()
    print(map)

unique_moves = []
for pos in moves:
    if pos not in unique_moves:
        unique_moves.append(pos)

print(len(unique_moves))