import math
map = []
with open('9/input.txt') as f:
    for line in f.readlines():
        vals = list(line.strip())
        file = True
        file_counter = 0
        for val in vals:
            if file:
               map.append({'id':file_counter,'size':int(val)})
               file_counter+=1
            else:
                map.append({'id':-1,'size':int(val)})
            file = not file

def print_map():
    for e in map:
        c = ''
        if e['id'] == -1:
            c = '.'
        else:
            c = e['id']
        for i in range(e['size']):
            print(c,end='')
    print('')


#returns index in compressed map of first block large enough
def get_first_empty_block(size):
    for i,e in enumerate(map):
        if e['id'] == -1 and e['size'] >= size:
            return i
    return -1

for e in reversed(map):
    if not e['id'] == -1:
        j = get_first_empty_block(e['size'])
        if j >= 0 and map.index(e)>j:
            if e['size'] < map[j]['size']:
                map.insert(j+1,{'id':-1,'size':map[j]['size']-e['size']})
            map[j]['id'] = e['id']
            map[j]['size'] = e['size']
            e['id'] = -1

#calculate checksum
checksum = 0
pos = 0
for e in map:
    if not e['id'] == -1:
        checksum += e['id'] * ( (e['size']*pos)+(e['size']-1) * (((e['size']-1)+1)/2) )
    pos += e['size']
print(int(checksum))

        
'''
(i+0*id)+(i+1*id)+(i+2*id)
id((i+0)+(i+1)+(i+2))
id(3i+2!)
id((size*i)+(size-1)!)

'''
