YES_ANSWERS = ["y", "yes"]

board = []
app_is_running = True
game_is_running = True
turn = 'X'


def print_board():
    for row_index, row in enumerate(board):
        row_string = ""
        for cell_index, cell in enumerate(row):
            if row_index == 2:
                row_string = row_string + f"  {cell}  "
            else:
                row_string = row_string + f"__{cell}__"

            if cell_index != 2:
                row_string = row_string + "|"

        print(row_string)


def switch_turn():
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"


def get_player_selection():
        space_selected = int(input("Where do you want to go? (1-9)\n").strip()) - 1
        row_number = int(space_selected / 3)
        column_number = space_selected % 3
        
        return (row_number, column_number)


def play_game():
    global game_is_running
    while game_is_running:
        print_board()
        print(f"It's {turn}'s turn.\n")
        row_number, column_number = get_player_selection()
        board[row_number][column_number] = turn
        if someone_won(row_number, column_number) or tie_occurred():
            game_is_running = False

        switch_turn()
    

def create_blank_board():
    global board
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        [" ", " ", " "]
    ]


def someone_won_horizontally(row_number):
    row = board[row_number]
    return row[0] == row[1] == row[2]


def southeast_diagonal_win(row_number, column_number):
    return board[0][0] == board[1][1] == board[2][2]


def northeast_diagonal_win(row_number, column_number):
    return board[2][0] == board[1][1] == board[0][2]

def someone_won_vertically(column_number):
    return board[0][column_number] == board[1][column_number] == board[2][column_number]


def someone_won_diagonally(row_number, column_number):
    return southeast_diagonal_win(row_number, column_number) or northeast_diagonal_win(row_number, column_number)


def someone_won(row_number, column_number):
    won = someone_won_horizontally(row_number) or someone_won_vertically(column_number) or someone_won_diagonally(row_number, column_number)
    if won:
        print_board()
        print(f"{turn} won!")

    return won


def tie_occurred():
    tied = not "_" in board[0] and not "_" in board[1] and not " " in board[2]
    if tied:
        print_board()
        print("It's a tie!")
    
    return tied


while(app_is_running):
    create_blank_board()
    play_game()
    
    play_again = input("Shall we play again? (y/n)\n").lower().strip()
    app_is_running = play_again in YES_ANSWERS
