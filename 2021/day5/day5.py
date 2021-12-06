with open("input.txt", "r") as file:
    rows = [row.rstrip() for row in file]
    lines = [
        [
            [int(num) for num in coord.split(",")]
            for coord in row.split(" -> ")
        ] for row in rows
    ]

def count_overlapping_points(vent_positions):
    num_overlapping_points = 0
    for num_points in vent_positions.values():
        if num_points > 1:
            num_overlapping_points += 1
    return num_overlapping_points

# Part 1
vent_positions = {}
for line in lines:
    [x1, y1], [x2, y2] = line
    if x1 == x2:
        small_y = min(y1, y2)
        big_y = max(y1, y2)
        for y in range(small_y, big_y + 1):
            pos = (x1, y)
            if pos in vent_positions:
                vent_positions[pos] += 1
            else:
                vent_positions[pos] = 1
    elif y1 == y2:
        small_x = min(x1, x2)
        big_x = max(x1, x2)
        for x in range(small_x, big_x + 1):
            pos = (x, y1)
            if pos in vent_positions:
                vent_positions[pos] += 1
            else:
                vent_positions[pos] = 1

num_overlapping_points = count_overlapping_points(vent_positions)
print("Part 1")
print("There are", num_overlapping_points, "points where at least two lines overlap")

print()

# Part 2
vent_positions = {}
for line in lines:
    [x1, y1], [x2, y2] = line
    small_x = min(x1, x2)
    big_x = max(x1, x2)
    small_y = min(y1, y2)
    big_y = max(y1, y2)
    x_delta = big_x - small_x
    y_delta = big_y - small_y
    if x1 == x2:
        for y in range(small_y, big_y + 1):
            pos = (x1, y)
            if pos in vent_positions:
                vent_positions[pos] += 1
            else:
                vent_positions[pos] = 1
    elif y1 == y2:
        for x in range(small_x, big_x + 1):
            pos = (x, y1)
            if pos in vent_positions:
                vent_positions[pos] += 1
            else:
                vent_positions[pos] = 1
    elif x_delta == y_delta:
        x_dir_coeff = 1 if x2 > x1 else -1
        y_dir_coeff = 1 if y2 > y1 else -1
        for i in range(x_delta + 1):
            pos = (x1 + i * x_dir_coeff, y1 + i * y_dir_coeff)
            if pos in vent_positions:
                vent_positions[pos] += 1
            else:
                vent_positions[pos] = 1

num_overlapping_points = count_overlapping_points(vent_positions)
print("Part 2")
print("There are", num_overlapping_points, "points where at least two lines overlap")
