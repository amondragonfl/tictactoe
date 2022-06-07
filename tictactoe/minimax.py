from board import Board


class Minimax:
    def __int__(self, board: Board, player: str):
        if not board.player_exists(player):
            raise ValueError(f"Invalid player: {player}")
        self.player = player
        self.board = board

    def best_move(self):
        pass

    def static_eval(self):
        pass
