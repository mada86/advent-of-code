with open("input.txt", "r") as file:
    numbers = [row.rstrip() for row in file]

# Part 1
gamma_rate_binary = ""
binary_columns = zip(*numbers)
for column in binary_columns:
    if column.count("1") > column.count("0"):
        gamma_rate_binary += "1"
    else:
        gamma_rate_binary += "0"
gamma_rate = int(gamma_rate_binary, 2)

num_bits = int(len(numbers[0]))
max_rate = 2 ** num_bits
epsilon_rate = max_rate - gamma_rate - 1
power_consumption = gamma_rate * epsilon_rate
print(f"Power consumption: {power_consumption}")

# Part 2
def get_binary_rating(is_reversed=False):
    remaining_numbers = numbers.copy()
    num_bits = int(len(numbers[0]))
    for i in range(num_bits):
        if len(remaining_numbers) == 1:
            break
        binary_columns = list(zip(*remaining_numbers))
        first_column = binary_columns[i]
        key_number = "0"
        if is_reversed:
            if first_column.count("0") > first_column.count("1"):
                key_number = "1"
        else:
            if first_column.count("1") >= first_column.count("0"):
                key_number = "1"
        new_remaining_numbers = []
        for number in remaining_numbers:
            if number[i] == key_number:
                new_remaining_numbers.append(number)
        remaining_numbers = new_remaining_numbers
    return remaining_numbers[0]

oxygen_gen_rating_binary = get_binary_rating()
co2_scubber_rating_binary = get_binary_rating(is_reversed=True)
oxygen_gen_rating = int(oxygen_gen_rating_binary, 2)
co2_scrubber_rating = int(co2_scubber_rating_binary, 2)
life_support_rating = oxygen_gen_rating * co2_scrubber_rating
print(f"Life support rating: {life_support_rating}")
