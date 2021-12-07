with open("input.txt", "r") as file:
    content = file.read()
    positions = [int(num) for num in content.split(",")]

# Part 1
closest_pos = min(positions)
farthest_pos = max(positions)
pos_fuel_required_pairs = []
for pos in range(closest_pos, farthest_pos + 1):
    total_fuel = 0
    for crab_pos in positions:
        total_fuel += abs(crab_pos - pos)
    pos_fuel_required_pairs.append((pos, total_fuel))
pos_fuel_required_pairs.sort(key=lambda p: p[1])
print("Part 1")
print("The least fuel required is", pos_fuel_required_pairs[0][1])

print()

# Part 2
pos_fuel_required_pairs = []
for pos in range(closest_pos, farthest_pos + 1):
    total_fuel = 0
    for crab_pos in positions:
        for i in range(1, abs(crab_pos - pos) + 1):
            total_fuel += i
    pos_fuel_required_pairs.append((pos, total_fuel))
pos_fuel_required_pairs.sort(key=lambda p: p[1])
print("Part 2")
print("The least fuel required is", pos_fuel_required_pairs[0][1])
