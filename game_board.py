class Board:

    def __init__(self, symbol):
        self.symbol = symbol
        self.top_row = [f" {self.symbol} ", "|", f" {self.symbol} ", "|", f" {self.symbol} "]
        self.middle_row = [f" {self.symbol} ", "|", f" {self.symbol} ", "|", f" {self.symbol} "]
        self.bottom_row = [f" {self.symbol} ", "|", f" {self.symbol} ", "|", f" {self.symbol} "]
        self.separator = "-----------"
        self.turn = 1
        self.score = [0, 0]
        self.winning_combos = []

    def print_board(self):
        """Prints the current board"""
        print(f"{''.join(self.top_row)}\n{self.separator}\n{''.join(self.middle_row)}\n{self.separator}\n{''.join(self.bottom_row)}\n")

    def check_square(self, row, index):
        """Check if square is already taken"""
        active_square = row[index]
        if active_square == "   ":
            result = True
        else:
            result = False
        return result

    def place_square(self, square, row, index):
        """Puts the current player's symbol on the board"""
        row[index] = square

    def get_row(self):
        """Ask player which row they want to play in"""
        row_choice = input(
            "In which row do you want to place your symbol? T for top, M for middle, B for bottom\n").lower()
        if row_choice == "t":
            row = self.top_row
        elif row_choice == "m":
            row = self.middle_row
        elif row_choice == "b":
            row = self.bottom_row
        else:
            row = "invalid"
        return row

    def get_column(self):
        """Ask player which column they want to play in"""
        column_choice = input(
            "In which column do you want to place your symbol? L for left, M for middle, R for right\n").lower()
        if column_choice == "l":
            index = 0
        elif column_choice == "m":
            index = 2
        elif column_choice == "r":
            index = 4
        else:
            index = "invalid"
        return index

    def check_win(self):
        """Checks if either player has won"""
        self.winning_combos = [[self.top_row[0], self.top_row[2], self.top_row[4]],
                               [self.middle_row[0], self.middle_row[2], self.middle_row[4]],
                               [self.bottom_row[0], self.bottom_row[2], self.bottom_row[4]],
                               [self.top_row[0], self.middle_row[0], self.bottom_row[0]],
                               [self.top_row[2], self.middle_row[2], self.bottom_row[2]],
                               [self.top_row[4], self.middle_row[4], self.bottom_row[4]],
                               [self.top_row[0], self.middle_row[2], self.bottom_row[4]],
                               [self.bottom_row[0], self.middle_row[2], self.top_row[4]]]
        for combo in self.winning_combos:
            is_combo = self.check_combo(combo)
            if is_combo:
                not_blank = self.check_for_blanks(combo)
                if not_blank:
                    return True
                else:
                    continue
        return False

    def check_combo(self, combo):
        """Checks line for winning combo"""
        if combo[0] == combo[1] == combo[2]:
            return True
        else:
            return False

    def check_for_blanks(self, combo):
        """Checks line for blank squares"""
        for square in combo:
            if square == "   ":
                return False
        return True

    def reset(self):
        """Resets board for a new game"""
        self.top_row = [f" {self.symbol} ", "|", f" {self.symbol} ", "|", f" {self.symbol} "]
        self.middle_row = [f" {self.symbol} ", "|", f" {self.symbol} ", "|", f" {self.symbol} "]
        self.bottom_row = [f" {self.symbol} ", "|", f" {self.symbol} ", "|", f" {self.symbol} "]
