from board import Board
import math


class Minimax:
    def __init__(self, board: Board, player: str):
        if not board.player_exists(player):
            raise ValueError(f"Invalid player: {player}")
        self.player = player
        self.board = board
        self.other_player = self.board.players[0] if self.board.players[0] is not self.player else self.board.players[1]

    def best_move(self, maximizing_player: bool = True):
        if self.board.is_game_over():
            return self.static_eval(), None
        if maximizing_player:
            max_eval = -math.inf, None
            for index in self.board.empty_indices():
                self.board.make_move(index, self.player)
                move_eval = self.best_move(False)
                if move_eval[0] > max_eval[0]:
                    max_eval = (move_eval[0], index)
                self.board.state[index] = str(index + 1)
            return max_eval
        else:
            min_eval = math.inf, None
            for index in self.board.empty_indices():
                self.board.make_move(index, self.other_player)
                move_eval = self.best_move(True)
                if move_eval[0] < min_eval[0]:
                    min_eval = (move_eval[0], index)
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
