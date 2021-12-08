with open("input.txt", "r") as file:
    entries = [[value.split() for value in row.rstrip().split(" | ")] for row in file]

# Part 1
num = 0
for entry in entries:
    signal_patterns, output = entry
    for pattern in signal_patterns:
        if len(pattern) not in (2, 4, 3, 7):
            continue
        for output_pattern in output:
            if set(pattern) == set(output_pattern):
                num += 1
print("The digits 1, 4, 7, and 8 appear", num, "times")

# Part 2
from pprint import pprint

pattern_length_to_digit = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8],
}
total_output = 0
for entry in entries:
    # Segment index order:
    # 0
    #1 2
    # 3
    #4 5
    # 6
    signal_patterns, output = entry
    digit_to_possible_patterns = [[] for _ in range(10)]
    for pattern in signal_patterns:
        possible_digits = pattern_length_to_digit[len(pattern)]
        for digit in possible_digits:
            digit_to_possible_patterns[digit].append(set(pattern))

    pattern_1 = digit_to_possible_patterns[1][0]
    pattern_4 = digit_to_possible_patterns[4][0]
    pattern_7 = digit_to_possible_patterns[7][0]

    segment_0 = list(pattern_1 ^ pattern_7)[0]

    segment_1_options = pattern_1 ^ pattern_4

    possible_9_patterns = digit_to_possible_patterns[9]
    for pattern in possible_9_patterns:
        if pattern_1.issubset(pattern) and segment_1_options.issubset(pattern):
            pattern_9 = pattern
            break

    temp_for_segment_0 = pattern_4 ^ pattern_9
    temp_for_segment_0.remove(segment_0)
    segment_6 = list(temp_for_segment_0)[0]

    possible_6_patterns = digit_to_possible_patterns[6]
    for pattern in possible_6_patterns:
        if (pattern_1 & pattern and not pattern_1.issubset(pattern)) and segment_1_options.issubset(pattern):
            pattern_6 = pattern

    segment_4 = list(pattern_6 - pattern_9)[0]

    segment_2 = list(pattern_9 - pattern_6)[0]

    segment_5 = list(pattern_1 - set(segment_2))[0]

    possible_3_patterns = digit_to_possible_patterns[3]
    for pattern in possible_3_patterns:
        if pattern_1.issubset(pattern):
            pattern_3 = pattern

    temp_for_segment_3 = pattern_3 - pattern_1
    temp_for_segment_3.remove(segment_0)
    temp_for_segment_3.remove(segment_6)
    segment_3 = list(temp_for_segment_3)[0]

    temp_for_segment_1 = list(segment_1_options)
    temp_for_segment_1.remove(segment_3)
    segment_1 = temp_for_segment_1[0]

    pattern_to_digit = {
        frozenset(segment_0 + segment_1 + segment_2 + segment_4 + segment_5 + segment_6): 0,
        frozenset(pattern_1): 1,
        frozenset(segment_0 + segment_2 + segment_3 + segment_4 + segment_6): 2,
        frozenset(pattern_3): 3,
        frozenset(pattern_4): 4,
        frozenset(segment_0 + segment_1 + segment_3 + segment_5 + segment_6): 5,
        frozenset(pattern_6): 6,
        frozenset(pattern_7): 7,
        frozenset(segment_0 + segment_1 + segment_2 + segment_3 + segment_4 + segment_5 + segment_6): 8,
        frozenset(pattern_9): 9,
    }

    output_value = int("".join([str(pattern_to_digit[frozenset(pattern)]) for pattern in output]))
    total_output += output_value
print("The total output is", total_output)
