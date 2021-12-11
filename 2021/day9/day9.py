with open("input.txt", "r") as file:
    grid = [[int(height) for height in row.rstrip()] for row in file]

grid_height = len(grid)
grid_width = len(grid[0])

low_points = []

def get_adj_points(x, y):
    adj_points = []
    if x > 0:
        adj_points.append((x - 1, y))
    if x < grid_width - 1:
        adj_points.append((x + 1, y))
    if y > 0:
        adj_points.append((x, y - 1))
    if y < grid_height - 1:
        adj_points.append((x, y + 1))
    return adj_points

# Part 1
def is_low_point(x, y):
    height = grid[y][x]
    adj_points = get_adj_points(x, y)
    for point in adj_points:
        x, y = point
        if height >= grid[y][x]:
            return False
    return True

total_risk_level = 0
for y, row in enumerate(grid):
    for x, height in enumerate(row):
        if is_low_point(x, y):
            low_points.append((x, y))
            risk_level = height + 1
            total_risk_level += risk_level

print("Total risk level:", total_risk_level)

# Part 2
def get_adj_basin_points(x, y):
    adj_basin_points = []
    adj_points = get_adj_points(x, y)
    for adj_point in adj_points:
        adj_x, adj_y = adj_point
        height = grid[adj_y][adj_x]
        if height < 9:
            adj_basin_points.append(adj_point)
    return adj_basin_points

def get_basin_points(point, basin_points=[]):
    basin_points = basin_points.copy()
    basin_points.append(point)
    x, y = point
    adj_basin_points = get_adj_basin_points(x, y)
    for adj_bp in adj_basin_points:
        if adj_bp not in basin_points:
            basin_points = get_basin_points(adj_bp, basin_points)
    return basin_points

basin_sizes = []
for lp in low_points:
    basin_points = get_basin_points(lp)
    size = len(basin_points)
    basin_sizes.append(size)

basin_sizes.sort(reverse=True)
three_largest_basin_sizes = basin_sizes[:3]
product = 1
for size in three_largest_basin_sizes:
    product *= size
print("Product of the three largest basin sizes:", product)
