class Board:
    def __init__(self, players: list = None):
        self.state = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.players = players if players is not None else ["x", "o"]
