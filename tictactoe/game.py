from board import Board
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    board = Board()

    while not board.is_game_over():
        clear_console()
        board.display_board()
        while True:
            try:
                player_choice = int(input("Enter a number from 1-9: ")) -1
            except ValueError:
                continue
            if player_choice <= 9 and board.is_empty(player_choice):
                board.make_move(player_choice, "x")
                break
        clear_console()
        board.display_board()


if __name__ == "__main__":
    main()
