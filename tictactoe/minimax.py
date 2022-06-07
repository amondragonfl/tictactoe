from board import Board


class Minimax:
    def __int__(self, board: Board, player: str):
        if player not in board.players:
            raise ValueError(f"Invalid player: {player}")
        self.player = player
        self.board = board

    def best_move(self):
        pass

    def static_eval(self):
        pass
