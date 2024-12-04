import re
import numpy as np

g = []
with open('4/input.txt') as f:
    for line in f.readlines():
        g.append(list(line.strip()))
grid = np.array(g)

def get_diags(grid):
    diags = []
    #split into subgrids of size 4
    for i in range(len(grid)-3):
        for j in range(len(grid[0])-3):
            diags.append(np.diagonal(grid[i:i+4,j:j+4]))
            diags.append(np.diagonal(np.fliplr(grid[i:i+4,j:j+4])))
    return diags

#checks a single row forward only
def check_row(row):
    x = 0
    for i in range(len(row)-3):
        if (row[i:i+4] == ['X','M','A','S']).all():
            x +=1
    return x

x = 0
#horizontal
for row in grid:
    x += check_row(row)
    x += check_row(np.flip(row))
#vertical
for col in grid.T:
    x += check_row(col)
    x += check_row(np.flip(col))

#diagonal
for diag in get_diags(grid):
    x += check_row(diag)
    x += check_row(np.flip(diag))

print(x)