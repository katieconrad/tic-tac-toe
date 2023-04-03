class Player:

    def __init__(self, symbol, i):
        self.symbol = symbol
        self.square = f" {self.symbol} "
        self.name = f"Player {self.symbol}"
        self.index = i
        self.type = "human"


class Computer(Player):

    def __init__(self, symbol, i):
        super().__init__(symbol, i)
        self.type = "computer"


