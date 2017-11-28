import random
import math
# import os  # enable if you want to clear the console screen after every move (line 111.
# I used IntelliJ while developing and it doesn't support the screen clearing command so I have left it commented out


def draw_board(spots):

    """Prints out the board. Takes the list of the board layout as an argument and iterates through a 3x3 matrix to print
    the board in the correct layout"""

    index = 0
    for i in range(1, 4):
        for j in range(1, 4):
            print("  {}  |".format(spots[index]), end="")
            index += 1
        if i < 3:
            print("\n-----|-----|-----|")


def player_move(player_number, available_squares):

    """Lets the players know whose move it is. Then takes in a number from 1-9 as input and checks it against the
    list of available squares. If the input is invalid string or number OR the number is not is the available squares
    then it prints out a message and asks the player again"""

    print("\nPlayer ", player_number, "'s turn", sep="")
    move = 0
    while True:
        if move not in available_squares:
            try:
                move = int(input("Please select a valid square number on the board: "))
            except ValueError:
                print("You selected an invalid option. Please select a valid square number between 1-9")
        else:
            return move


def vertical_check(layout, index):

    """Receives the board layout and the column to check as arguments. It then checks if the squares in that column all
    have the same value and if so, return True as well as the index to let the caller know which column has the winner's
    moves"""

    if layout[index] == layout[index+3] and layout[index+3] == layout[index+6]:
        return True, index
    else:
        return False, index


def horizontal_check(layout, index):

    """Receives the board layout and the row to check as arguments. It then checks if the squares in that row all
    have the same value and if so, return True as well as the index to let the caller know which row has the winner's
    moves"""

    if layout[index] == layout[index+1] and layout[index+1] == layout[index+2]:
        return True, index
    else:
        return False, index


def diagonal_check(layout):

    """Receives the board layout as argument and checks if either diagonal is a winning combination. If so, it will
    return True"""

    if (layout[0] == layout[4] and layout[4] == layout[8]) or (layout[2] == layout[4] and layout[4] == layout[6]):
        return True
    else:
        return False


def check_win_status(layout):

    """Performs check if the current board layout has any winning combinations horizontally, vertically or diagonally.
    If so, it will check whether the symbol in that combination is an X or O and depending on that return 1 or 2 for
    the winning player number"""

    for i in [0, 3, 6]:
        horizontal_results, index = horizontal_check(layout, i)
        if horizontal_results:
            return 1 if layout[index] == 'X' else 2

    if diagonal_check(layout):
        return 1 if layout[4] == 'X' else 2

    for i in [0, 1, 2]:
        vertical_results, index = vertical_check(layout, i)
        if vertical_results:
            return 1 if layout[index] == 'X' else 2


if __name__ == "__main__":

    board_layout = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # setup empty board
    available_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list holding the squares available to make a move in
    current_player = math.floor(random.randint(1, 2))
    print("player", current_player, "is the first player")
    draw_board(board_layout)
    game_over = False  # sets up the game over flag that will be used later to determine whether to leave the game loop
    result = None  # variable that will hold either the player number if one wins or the number 3 to signify a draw

    while not game_over:
        valid_move = player_move(current_player, available_spots)
        available_spots.pop(available_spots.index(valid_move))  # removes the spot from the list of available spots
        board_layout[valid_move-1] = "X" if current_player == 1 else "O"   # adds the symbol (X for P1 and O for P2)
        # to the board layout

        current_player = 1 if current_player == 2 else 2
        # os.system('cls' if os.name == 'nt' else 'clear')   # to clear the screen
        draw_board(board_layout)
        winner = check_win_status(board_layout)  # checks if there is a winning combination
        if winner:
            game_over = True
            result = winner
        if not available_spots:  # if there are no available spots and there was no winner then the game is a tie
            game_over = True
            result = 3

    if result == 3:
        print("\nThis game was a draw. Better luck next time")
    elif result == 1 or result == 2:
        print("\nPlayer {} wins the game. Well Done!".format(result))
