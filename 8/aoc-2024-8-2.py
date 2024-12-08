import re
map = []
with open('8/input.txt') as f:
    for line in f.readlines():
        map.append(list(line.strip()))

#get antenna positions
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
def check_node_pair_line(loc1, loc2):
    print('loc1:',loc1)
    print('loc2:',loc2)
    ans = []
    #find the whole int points on line defined by locs
    for y in range(len(map)):
        x = ((loc2[1]-loc1[1])/(loc2[0]-loc1[0]))*(y-loc1[0])+loc1[1]
        if x in range(len(map[0])) and x.is_integer():
            ans.append([y,int(x)])
    return ans

#get antinodes for one antenna type
def check_antinodes(antenna_list):
    antinodes = []
    for i,ant1 in enumerate(antenna_list):
        for j in range(i+1,len(antenna_list)):
            ant2 = antenna_list[j]
            antinodes += check_node_pair_line(ant1,ant2)
    return antinodes

antinodes = []
for name, antenna_list in antennas.items():
   ans = check_antinodes(antenna_list)
   for an in ans:
       if an not in antinodes:
           antinodes.append(an)
print(len(antinodes))
