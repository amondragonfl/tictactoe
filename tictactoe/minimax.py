from board import Board
import math


class Minimax:
    def __init__(self, board: Board, player: str):
        if not board.player_exists(player):
            raise ValueError(f"Invalid player: {player}")
        self.player = player
        self.board = board

    def best_move(self, maximizing_player):
        if self.board.is_game_over():
            return self.static_eval(), None
        if maximizing_player:
            max_eval = (-math.inf, None)
            for index in self.board.empty_indices():
                self.board.make_move(index, "o")
                current_eval = self.best_move(False)
                max_eval = (current_eval[0], index) if current_eval[0] > max_eval[0] else max_eval
                self.board.state[index] = str(index + 1)
            return max_eval
        else:
            min_eval = (math.inf, None)
            for index in self.board.empty_indices():
                self.board.make_move(index, "x")
                current_eval = self.best_move(True)
                min_eval = (current_eval[0], index) if current_eval[0] < min_eval[0] else min_eval
                self.board.state[index] = str(index + 1)
            return min_eval

    def static_eval(self) -> int:
        empty = self.board.count_empty()
        if self.board.get_winner() is None:
            return 0
        elif self.board.get_winner() == self.player:
            return empty + 1
        else:
            return -(empty + 1)
