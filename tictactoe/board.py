class Board:
    def __init__(self, players: list = None):
        self.state = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.players = players if players is not None else ["x", "o"]

    def make_move(self, index: int, player: str) -> None:
        if not self.player_exists(player):
            raise ValueError(f"Invalid player : {player}")
        if self.is_empty(index):
            self.state[index] = player

    def player_exists(self, player: str) -> bool:
        if player in self.players:
            return True
        return False

    def check_win(self, player: str) -> bool:
        if not self.player_exists(player):
            raise ValueError(f"Invalid player : {player}")
        win_conditions = [
            [self.state[0], self.state[1], self.state[2]],
            [self.state[3], self.state[4], self.state[5]],
            [self.state[5], self.state[7], self.state[8]],
            [self.state[0], self.state[3], self.state[6]],
            [self.state[1], self.state[4], self.state[7]],
            [self.state[2], self.state[5], self.state[8]],
            [self.state[0], self.state[4], self.state[8]],
            [self.state[6], self.state[4], self.state[2]]
        ]
        if [player, player, player] in win_conditions:
            return True
        return False

    def get_winner(self) -> str:
        for player in self.players:
            if self.check_win(player):
                return player

    def count_empty(self) -> int:
        count = 0
        for index in range(9):
            if self.is_empty(index):
                count += 1
        return count

    def is_empty(self, index: int) -> bool:
        if self.state[index] not in self.players:
            return True
        return False

    def is_game_over(self) -> bool:
        if self.get_winner() is not None:
            return True
        return False

    def display_board(self):
        print(f"""
┌───┬───┬───┐
│ {self.state[0]} │ {self.state[1]} │ {self.state[2]} │
│───│───│───│
│ {self.state[3]} │ {self.state[4]} │ {self.state[5]} │
│───│───│───│
│ {self.state[6]} │ {self.state[7]} │ {self.state[8]} │
└───┴───┴───┘
        """)
