import copy
map = []
with open('10/input.txt') as f:
    for line in f.readlines():
        map.append([int(x) for x in line.strip()])

def get_trails_inner(steps_taken,pos):
    trails = []
    correct_height = len(steps_taken)
    current_height = map[pos[0]][pos[1]]
    #if this is a wrong step
    if not current_height == correct_height:
        return []
    steps_taken.append(pos)
    #if at peak
    if current_height==9:
        return steps_taken
    #if not at peak yet
    else:
        for dir in [[1,0],[-1,0],[0,1],[0,-1]]:
            new_pos = [sum(x) for x in zip(pos, dir)]
            if new_pos[0] in range(len(map)) and new_pos[1] in range(len(map[0])):
                trail = get_trails_inner(copy.deepcopy(steps_taken), new_pos)
                if not trail == []:
                    trails+=trail
    return trails

#get number of peaks for 1 trailhead
def get_num_peaks(pos):
    trails = get_trails_inner([],pos)
    peaks = [x for i,x in enumerate(trails) if i>0 and (i+1)%10==0]
    unique_peaks = list(set(tuple(x) for x in peaks))
    return len(unique_peaks)

total = 0
for i,e in enumerate(map):
    for j,f in enumerate(e):
        if f==0:
            total += get_num_peaks([i,j])
print(total)