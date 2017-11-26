import random
import math
#import os


def draw_board(spots):
    index = 0
    for i in range(1, 4):
        for j in range(1, 4):
            print("  {}  |".format(spots[index]), end="")
            index += 1
        print("")


def determine_first_player():
    first_player = math.floor(random.randint(1, 2))
    return first_player


def player_move(player_number, available_squares):
    print("Player ", player_number, "'s turn", sep="")
    move = 0
    while True:
        if move not in available_squares:
            try:
                move = int(input("Please select a valid square number on the board: "))
            except ValueError:
                print("You selected an invalid option. Please select a valid square number between 1-9")
        else:
            return move


def player_switch(player):
    return 1 if player == 2 else 2


def check_win_status():
    return True

if __name__ == "__main__":
    board_layout = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    available_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    current_player = determine_first_player()
    print("player", current_player, "is the first player")
    draw_board(board_layout)
    game_over = False

    while not game_over:
        valid_move = player_move(current_player, available_spots)
        available_spots.pop(available_spots.index(valid_move))
        board_layout[valid_move-1] = "X" if current_player == 1 else "O"
        current_player = player_switch(current_player)
        # os.system('cls' if os.name=='nt' else 'clear')   #to clear the screen
        draw_board(board_layout)
        if check_win_status():
            game_over = True


