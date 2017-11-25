import random
import math
#import os


def draw_board(spots):
    print("print board")
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
    print("moving player ", player_number)
    move = 0
    while True:
        if move not in available_squares:
            try:
                move = int(input("Please select a valid square number on the board: "))
            except ValueError:
                print("You selected an invalid option. Please select a valid square number between 1-9")
        else:
            return move


if __name__ == "__main__":
    board_layout = [1,2,3,4,5,6,7,8,9]
    available_spots = [1,2,3,4,5,6,7,8,9]
    draw_board(board_layout)
    player = determine_first_player()
    print("player", player, "is the first player")
    game_over = False
    while not game_over:
        player_move(player, available_spots)
        player += 1
        available_spots.pop(1)
        board_layout[1]="X"
        draw_board(board_layout)
        player_move(player, available_spots)

    # os.system('cls' if os.name=='nt' else 'clear')   #to clear the screen
        game_over = True


