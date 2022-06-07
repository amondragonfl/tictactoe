from board import Board
from minimax import Minimax
from colorama import Fore
import colorama
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    o, x = f"{Fore.LIGHTRED_EX}o{Fore.RESET}", f"{Fore.LIGHTGREEN_EX}x{Fore.RESET}"
    board = Board([o, x])
    ai_player = Minimax(board, o)

    while not board.is_game_over():
        clear_console()
        board.display_board()
        print(f"Playing as {x}")
        while True:
            try:
                player_choice = int(input("Enter a number from 1-9: ")) - 1
            except ValueError:
                continue
            if player_choice <= 9 and board.is_empty(player_choice):
                board.make_move(player_choice, x)
                break
        if not board.is_game_over():
            print("Computer is thinking...")
            board.make_move(ai_player.best_move(True)[1], o)

    clear_console()
    board.display_board()
    if board.count_empty() == 0:
        print(f"Tie!")
    else:
        print(f"HE HE HE HA, you lost!")
    input("Press [ENTER] to play again or [CTRL + C] to exit")
    main()


if __name__ == "__main__":
    colorama.init(autoreset=True)
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit
