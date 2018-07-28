YES_ANSWERS = ["y", "yes"]
BOARD = 'board'
APP_IS_RUNNING = 'app_is_running'
GAME_IS_RUNNING = 'game_is_running'
TURN = 'turn'
AVAILABLE_SPACES = 'available_spaces'

game_state = {
    BOARD: [],
    APP_IS_RUNNING: True,
    GAME_IS_RUNNING: True,
    TURN: "X",
    AVAILABLE_SPACES: [1, 2, 3, 4, 5, 6, 7, 8, 9]
}


def initialize_game():
    create_blank_board()
    game_state[APP_IS_RUNNING] = True
    game_state[GAME_IS_RUNNING] = True
    game_state[TURN] = 'X'
    game_state[AVAILABLE_SPACES] = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def create_blank_board():
    game_state[BOARD] = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        [" ", " ", " "]
    ]


def play_game():
    while game_state[GAME_IS_RUNNING]:
        turn = game_state[TURN]
        print_board()
        print(f"\nIt's {turn}'s turn.")
        row_number, column_number = get_player_selection()
        game_state[BOARD][row_number][column_number] = game_state[TURN]
        if someone_won(row_number, column_number) or tie_occurred():
            game_state[GAME_IS_RUNNING] = False

        switch_turn()


def print_board():
    for row_index, row in enumerate(game_state[BOARD]):
        row_string = ""
        for cell_index, cell in enumerate(row):
            if row_index == 2:
                row_string = row_string + f"  {cell}  "
            else:
                row_string = row_string + f"__{cell}__"

            if cell_index != 2:
                row_string = row_string + "|"

        print(row_string)


def get_player_selection():
    formatted_choice = ""
    available_spaces = game_state[AVAILABLE_SPACES]

    while formatted_choice not in available_spaces:

        user_choice = input("Where do you want to go? (1-9)\n")
        try:
            formatted_choice = int(user_choice.strip())
            if formatted_choice not in available_spaces:
                print("Sorry, that's not an available space!")
        except ValueError:
            print("Sorry, that's not a number!")

    game_state[AVAILABLE_SPACES].remove(formatted_choice)

    board_index = formatted_choice - 1
    row_number, column_number = divmod(board_index, 3)

    return (row_number, column_number)


def someone_won(row_number, column_number):
    won = someone_won_horizontally(row_number) or \
        someone_won_vertically(column_number) or \
        someone_won_diagonally(row_number, column_number)

    if won:
        turn = game_state[TURN]
        print_board()
        print(f"{turn} WON!!")

    return won


def someone_won_horizontally(row_number):
    row = game_state[BOARD][row_number]

    return row[0] \
        == row[1] \
        == row[2]


def someone_won_vertically(column_number):
    board = game_state[BOARD]

    return board[0][column_number] \
        == board[1][column_number] \
        == board[2][column_number]


def someone_won_diagonally(row_number, column_number):
    return southeast_diagonal_win(row_number, column_number) or \
        northeast_diagonal_win(row_number, column_number)


def southeast_diagonal_win(row_number, column_number):
    board = game_state[BOARD]

    return board[0][0] \
        == board[1][1] \
        == board[2][2]


def northeast_diagonal_win(row_number, column_number):
    board = game_state[BOARD]

    return board[2][0] == board[1][1] == board[0][2]


def tie_occurred():
    board = game_state[BOARD]
    tied = not "_" in board[0] and \
        not "_" in board[1] and \
        not " " in board[2]

    if tied:
        print_board()
        print("It's a tie!")
    
    return tied


def switch_turn():
    if game_state[TURN] == "X":
        set_turn("O")
    else:
        set_turn("X")


def set_turn(turn):
    game_state[TURN] = turn


while(game_state[APP_IS_RUNNING]):
    initialize_game()
    play_game()
    
    play_again = (
        input("Shall we play again? (y/n)\n")
            .lower()
            .strip()
    )

    game_state[APP_IS_RUNNING] = play_again in YES_ANSWERS
