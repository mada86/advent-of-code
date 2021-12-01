def get_num_increments(lis):
    num_increments = 0
    for i, num in enumerate(lis):
        if i == 0:
            continue
        if num > lis[i - 1]:
            num_increments += 1
    return num_increments

with open("input.txt", "r") as file:
    depths = [int(row) for row in file]

# Part 1
num_depth_increments = get_num_increments(depths)
print(f"The number of times a depth measurement increases is {num_depth_increments}!")

# Part 2
sliding_window_sums = []
for i in range(len(depths)):
    window = depths[i:i + 3]
    if len(window) < 3:
        break
    sliding_window_sums.append(sum(window))

num_sliding_window_sum_increments = get_num_increments(sliding_window_sums)
print(f"The number of times a sliding window sum increases is {num_sliding_window_sum_increments}!")
