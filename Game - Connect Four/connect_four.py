from collections import deque


class InvalidColSize(Exception):
    pass


class FullColumn(Exception):
    pass


board_rows, board_columns = (6, 7)
board = [[0 for _ in range(board_columns)] for _ in range(board_rows)]

connections_to_win = 4
winning_conditions = {
    "horizontal":
        {"left": (0, -1),
         "right": (0, 1)},

    "vertical":
        {"top": (-1, 0),
         "down": (1, 0)},

    "diagonal-top-left-down-right":
        {"top-left": (-1, -1),
         "down-right": (1, 1)},

    "diagonal-top-right-down-left":
        {"top-right": (-1, 1),
         "down-left": (1, -1)},
}

current_players = deque()

while True:
    try:
        current_players = deque([int(x) for x in input("Provide the names "
                                                       "of all players, separated by a space: ").split()])
        break
    except ValueError:
        print("Names have to be integers - 1, 2, 3, etc.")
        continue

player_victory = False
total_turns = 0

while True:
    player = current_players.popleft()
    current_players.append(player)
    chosen_col = 0

    while True:
        try:
            print()
            chosen_col = int(input(f"Player {player}, please choose a column: "))
            if not (1 <= chosen_col <= board_columns):
                raise InvalidColSize()
            elif not len([0 for i in range(board_rows) if board[i][chosen_col - 1] == 0]):
                raise FullColumn()
            break
        except ValueError:
            print("Column number has to be an integer - 1, 2, 3 etc.")
            continue
        except InvalidColSize:
            print(f"Column has to be bigger than/equal to 1 and lower than/equal to {board_columns}!")
            continue
        except FullColumn:
            print(f"Column {chosen_col} is full! Choose another column!")
            continue

    total_turns += 1
    chosen_col -= 1
    current_placement = []

    for row in range(board_rows - 1, -1, -1):
        if board[row][chosen_col] == 0:
            board[row][chosen_col] = player
            current_placement = [row, chosen_col]
            break

    print()
    [print(row) for row in board]

    if total_turns >= board_rows * board_columns:
        print("Game over! The board is full!")
        break

    for (connection, possible_directions) in winning_conditions.items():
        current_connection = [current_placement]

        for (direction, coordinates) in possible_directions.items():
            current_row, current_col = current_placement
            check_row, check_col = coordinates

            for _ in range(connections_to_win):
                current_row += check_row
                current_col += check_col

                if (0 <= current_row < board_rows) and (0 <= current_col < board_columns):
                    if board[current_row][current_col] == player:
                        current_connection.append([current_row, current_col])

                        if len(current_connection) >= 4:
                            print(f"The winner is player {player}!")
                            player_victory = True   # exit() could be used if we want the game to stop immediately
                            break
                    else:
                        break
                else:
                    break

            if player_victory:
                break
        if player_victory:
            break
    if player_victory:
        break
