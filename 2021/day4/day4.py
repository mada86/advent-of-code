with open("input.txt", "r") as file:
    contents = file.read()
    sections = contents.split("\n\n")
    numbers = [int(num) for num in sections[0].split(",")]
    boards_raw = sections[1:]
    boards = []
    for board_raw in boards_raw:
        rows_raw = board_raw.split("\n")
        board = []
        for row_raw in rows_raw:
            row = [int(num) for num in row_raw.split()]
            board.append(row)
        boards.append(board)

def simulate_bingo(numbers, boards):
    num_rows = len(boards[0])
    num_columns = len(boards[0][0])

    all_num_marked = []
    for board in boards:
        num_marked = [
            [0] * num_rows,
            [0] * num_columns
        ]
        all_num_marked.append(num_marked)

    # Note that this assumes all numbers are positive
    # A marked out number is signified by a "-1"
    winning_board_indexes = []
    winning_numbers = []
    for number in numbers:
        for i, board in enumerate(boards):
            if i in winning_board_indexes:
                continue
            num_marked = all_num_marked[i]
            for j, row in enumerate(board):
                try:
                    k = row.index(number)
                except ValueError:
                    continue
                board[j][k] = -1
                num_marked[0][j] += 1
                num_marked[1][k] += 1
            if num_rows in num_marked[0] or num_columns in num_marked[1]:
                winning_board_indexes.append(i)
                winning_numbers.append(number)
    return (winning_board_indexes, winning_numbers)

def calculate_unmarked_numbers_sum(board):
    unmarked_numbers_sum = 0
    for row in board:
        for num in row:
            if num > -1:
                unmarked_numbers_sum += num
    return unmarked_numbers_sum

# Part 1
winning_board_indexes, winning_numbers = simulate_bingo(numbers, boards)
first_winning_board_index = winning_board_indexes[0]
winning_board = boards[first_winning_board_index]
unmarked_numbers_sum = calculate_unmarked_numbers_sum(winning_board)
score = unmarked_numbers_sum * winning_numbers[0]
print("Winning score:", score)

# Part 2
last_winning_board_index = winning_board_indexes[-1]
winning_board = boards[last_winning_board_index]
unmarked_numbers_sum = calculate_unmarked_numbers_sum(winning_board)
score = unmarked_numbers_sum * winning_numbers[-1]
print("Last winning score:", score)
