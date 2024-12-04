import re
import numpy as np

g = []
with open('4/input.txt') as f:
    for line in f.readlines():
        g.append(list(line.strip()))
grid = np.array(g)

#split into 3x3 grids
def get_grids(grid):
    grids = []
    for i in range(len(grid)-2):
        for j in range(len(grid[0])-2):
            grids.append(grid[i:i+3,j:j+3])
    return grids

def check_row(row):
    if (row == ['M','A','S']).all() or (row == ['S','A','M']).all():
        return True

#checks a 3x3 grid
def check_minigrid(grid):
    if check_row(np.diagonal(grid)) and check_row(np.diagonal(np.fliplr(grid))):
        return True
    return False

x = 0
#diagonal
for minigrid in get_grids(grid):
    x += check_minigrid(minigrid)

print(x)