from board import Board
import math


class Minimax:
    def __init__(self, board: Board, player: str):
        if not board.player_exists(player):
            raise ValueError(f"Invalid player: {player}")
        self.player = player
        self.board = board

    def static_eval(self) -> int:
        empty = self.board.count_empty()
        if self.board.get_winner() is None:
            return 0
        elif self.board.get_winner() == self.player:
            return empty + 1
        else:
            return -empty - 1
