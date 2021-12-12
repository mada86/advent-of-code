from copy import deepcopy

with open("input.txt", "r") as file:
    original_grid = [[int(energy) for energy in row.rstrip()] for row in file]

# Part 1
grid = deepcopy(original_grid)

grid_height = len(grid)
grid_width = len(grid[0])

def increment_adj_points(y, x):
    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            if y_offset == x_offset == 0:
                continue
            adj_y = y + y_offset
            adj_x = x + x_offset
            if adj_y < 0 or adj_x < 0:
                continue
            if adj_y > grid_height - 1 or adj_x > grid_width - 1:
                continue
            grid[adj_y][adj_x] += 1
    return grid

def step():
    num_flashes = 0
    for y, row in enumerate(grid):
        for x in range(len(row)):
            grid[y][x] += 1

    flashed_points = []
    while True:
        new_flashed_points = []
        for y, row in enumerate(grid):
            for x, energy in enumerate(row):
                if energy <= 9 or (y, x) in flashed_points:
                    continue
                increment_adj_points(y, x)
                new_flashed_points.append((y, x))
        if len(new_flashed_points) == 0:
            break
        flashed_points += new_flashed_points

    for y, row in enumerate(grid):
        for x, energy in enumerate(row):
            if energy <= 9:
                continue
            grid[y][x] = 0
            num_flashes += 1
    return num_flashes

num_flashes = 0
for i in range(100):
    num_flashes += step()

print("Num flashes:", num_flashes)

# Part 2
grid = deepcopy(original_grid)

def are_all_energies_equal():
    top_left_energy = grid[0][0]
    for row in grid:
        for energy in row:
            if energy != top_left_energy:
                return False
    return True

step_number = 1
while True:
    step()
    if are_all_energies_equal():
        print("All energies are equal at step:", step_number)
        break
    step_number += 1
