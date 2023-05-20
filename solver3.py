import numpy as np
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 0, 0, 0, 0]]

def print_grid(grid):
    print()
    for i in range(9):
        if i % 3 == 0:
            print('---------------------------')
        for j in range(9):
            if j % 3 == 0:
                print(' | ', end="")
            print(grid[i][j], end=" ")
        print()
    print('---------------------------')

def possible(grid, row, col, num):
    # Check if number is in row
    for n in range(9):
        if grid[row][n] == num:
            return False
    # Check if number is in col
    for n in range(9):
        if grid[n][col] == num:
            return False
    # Check if number is in 3x3 box
    row_offset = row - row % 3
    col_offset = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[row_offset+i][col_offset+j] == num:
                return False
    return True


def check(grid):
    grid = np.array(grid)
    nums = {i for i in range(1,10)}
    for x in range(9):
        # Rows Check
        if nums != set(grid[x, :]):
            return False
        # Columns Check
        if nums != set(grid[:, x]):
            return False
    # Boxes Check
    for x in [0, 3, 6]:
        for y in [0, 3, 6]:
            if nums != set(grid[x:x+3, y:y+3].flatten()):
                return False
    return True

def solve(grid, row, col):
    if (row == 8 and col == 9):
        return True
    
    if col == 9:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)
    
    for num in range(1, 10, 1):
        if possible(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

print_grid(grid)
if solve(grid, 0, 0):
    print_grid(grid)
    print(check(grid))