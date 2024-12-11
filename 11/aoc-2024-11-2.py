stones = []
with open('11/input.txt') as f:
    for line in f.readlines():
        stones = [int(x) for x in line.split(' ')]

caches = []

def blink(stone): 
    result = []
    val = str(stone)
    i = 0
    if stone == 0:
        result.append(1)
    elif len(val) % 2 == 0:
        result.append(int(val[:int(len(val)/2)]))
        result.append(int(val[int(len(val)/2):]))
        i +=1
    else:
        result.append(stone*2024)
        i +=1
    return result

def calculate_num_stones(blinks,depth,stones):
    result = 0
    for stone in stones:
        res_num = 0
        if stone in caches[depth]:
            result += caches[depth][stone]
        else:
            res_values = blink(stone)
            if depth+1 < blinks:
                res_num += calculate_num_stones(blinks,depth+1,res_values)
                result += res_num
                caches[depth][stone] = res_num
            elif depth+1 == blinks:
                result += len(res_values)
    return result

def calculate_blinks(blinks, stones):
    global caches
    caches = [{} for i in range(blinks)]
    result = calculate_num_stones(blinks,0,stones)
    return result
    
result = calculate_blinks(75,stones)
print(result)
