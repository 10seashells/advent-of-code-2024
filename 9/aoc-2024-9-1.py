map_compressed = []
with open('9/input.txt') as f:
    for line in f.readlines():
        vals = list(line.strip())
        int_vals = []
        for val in vals:
            int_vals.append(int(val))
    map_compressed = int_vals

map = []
file = True
file_counter = 0
for e in map_compressed:
    if file:
        for i in range(e):
            map.append(file_counter)
        file_counter += 1
        file = False
    else:
        for i in range(e):
            map.append('.')
        file = True

earliest = 0
def get_first_empty():
    global earliest
    for i in range(earliest, len(map)):
      earliest +=1
      if map[i] == '.':
          return i
    return -1

#move files
for i in reversed(range(len(map))):
    if not map[i] == '.':
        j = get_first_empty()
        if j > i:
            break
        map[j] = map[i]
        map[i] = '.'
    
#calculate checksum
checksum = 0
for i in range(len(map)):
    if not map[i] == '.':
        checksum += i*map[i]
print(checksum)
