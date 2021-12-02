with open("input.txt", "r") as file:
    steps = [row.rstrip() for row in file]

# Part 1
pos_x = 0
pos_y = 0
for step in steps:
    direction, magnitude = step.split()
    magnitude = int(magnitude)
    if direction == "forward":
        pos_x += magnitude
    elif direction == "up":
        pos_y -= magnitude
    elif direction == "down":
        pos_y += magnitude
    else:
        print(f"{direction} is an unknown direction!")

print("Part 1")
print(f"Final horizontal position * Final depth = {pos_x * pos_y}")
print()

# Part 2
pos_x = 0
pos_y = 0
aim = 0
for step in steps:
    direction, magnitude = step.split()
    magnitude = int(magnitude)
    if direction == "forward":
        pos_x += magnitude
        pos_y += aim * magnitude
    elif direction == "up":
        aim -= magnitude
    elif direction == "down":
        aim += magnitude
    else:
        print(f"{direction} is an unknown direction!")

print("Part 2")
print(f"Final horizontal position * Final depth = {pos_x * pos_y}")
