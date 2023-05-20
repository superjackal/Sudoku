import numpy as np
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


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

def full(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False
    return True

def check(grid):
    grid = np.array(grid)
    nums = {i for i in range(1, 10)}
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

def solve(grid):
    while not full(grid):
        possible_numbers = [[ list() for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if grid[i][j] > 0:
                    continue
                possibilities = []
                for n in range(1, 10):
                    if possible(grid, i, j, n):
                        possibilities.append(n)
                possible_numbers[i][j] = possibilities
                if len(possible_numbers[i][j]) == 1:
                    grid[i][j] = possible_numbers[i][j][0]
        print_grid(grid)
print_grid(grid)
solve(grid)
print(check(grid))