import re
map = []
with open('8/input.txt') as f:
    for line in f.readlines():
        map.append(list(line.strip()))
print(map)

antennas = {}
for i,row in enumerate(map):
    for j,loc in enumerate(row):
        if not loc == '.':
            if loc in antennas:
                antennas[loc].append([i,j])
            else:
                antennas[map[i][j]] = [[i,j]]
print(antennas)

#get antinodes for a pair of antennas
def check_node_pair(loc1, loc2):
    ans = []
    miny = min(loc1[0],loc2[0])
    maxy = max(loc1[0],loc2[0])
    diffy = maxy-miny
    minx = min(loc1[1],loc2[1])
    maxx = max(loc1[1],loc2[1])
    diffx = maxx-minx
    #\ diagonal
    if (loc1[0]<loc2[0] and loc1[1]<loc2[1]) or (loc2[0]<loc1[0] and loc2[1]<loc1[1]):
        an1 = [miny-diffy,minx-diffx]
        if (an1[0]>=0 and an1[1]>=0):
            ans.append(an1)
        an2 = [maxy+diffy,maxx+diffx]
        if (an2[0]<len(map) and an2[1]<len(map[0])):
            ans.append(an2)
    #/ diagonal
    else:
        an3 = [miny-diffy,maxx+diffx]
        if (an3[0]>=0 and an3[1]<len(map[0])):
            ans.append(an3)
        an4 = [maxy+diffy,minx-diffx]
        if (an4[0]<len(map) and an4[1]>=0):
            ans.append(an4)
    return ans

#get antinodes for one antenna type
def check_antinodes(antenna_list):
    antinodes = []
    for i,ant1 in enumerate(antenna_list):
        for j in range(i+1,len(antenna_list)):
            ant2 = antenna_list[j]
            antinodes += check_node_pair(ant1,ant2)
    return antinodes

antinodes = []
for name, antenna_list in antennas.items():
   ans = check_antinodes(antenna_list)
   for an in ans:
       if an not in antinodes:
           antinodes.append(an)


print(antinodes)
print(len(antinodes))
