class Board:
    def __init__(self, players: list = None):
        self.state = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.players = players if players is not None else ["x", "o"]

    def make_move(self, index: int, player: str) -> None:
        if player not in self.players:
            raise ValueError(f"Invalid player : {player}")
        if self.state[index] not in self.players:
            self.state[index] = player
