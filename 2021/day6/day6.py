with open("input.txt", "r") as file:
    content = file.read()
    school = [int(num) for num in content.split(",")]

def get_num_fish_after_simulation(school, num_days):
    fish_interval_freq = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    for fish in school:
        fish_interval_freq[fish] += 1
    for _ in range(num_days):
        num_new_fish = fish_interval_freq[0]
        for interval, freq in fish_interval_freq.copy().items():
            fish_interval_freq[interval] = 0
            if interval > 0:
                fish_interval_freq[interval - 1] = freq
        fish_interval_freq[8] += num_new_fish
        fish_interval_freq[6] += num_new_fish
    num_fish = sum(fish_interval_freq.values())
    return num_fish

# Part 1
num_fish = get_num_fish_after_simulation(school, 80)
print("After 80 days, there would be", num_fish, "lanternfish")

# Part 2
num_fish = get_num_fish_after_simulation(school, 256)
print("After 256 days, there would be", num_fish, "lanternfish")
