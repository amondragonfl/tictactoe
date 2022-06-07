from board import Board


class Minimax:
    def __init__(self, board: Board, player: str):
        if not board.player_exists(player):
            raise ValueError(f"Invalid player: {player}")
        self.player = player
        self.board = board

    def best_move(self):
        pass

    def static_eval(self) -> int:
        empty = self.board.count_empty()
        if self.board.get_winner() is None:
            return 0
        elif self.board.get_winner() == self.player:
            return empty
        else:
            return -empty
