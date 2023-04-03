from random import randint
from game_board import Board
from players import Player, Computer


# Create game board and one player

board = Board(" ")
player1 = Player("X", 0)


def get_num_players():
    """Ask if there are 1 or 2 players"""
    num_players = 0
    while num_players == 0:
        num_players = input("How many players? 1 or 2? ")
        if num_players == "1":
            print("Alright, you can play against the computer.")
            player2 = Computer("O", 1)
            return player2
        elif num_players == "2":
            print("Great! Two players selected.")
            player2 = Player("O", 1)
            return player2
        else:
            print("I'm sorry, that selection is not valid. Please try again.")
            num_players = 0


def computer_turn():
    """Computer places symbol in a randomly generated position"""
    possible_positions = [["t", 0], ["t", 2], ["t", 4],
                          ["m", 0], ["m", 2], ["m", 4],
                          ["b", 0], ["b", 2], ["b", 4]]
    i = randint(0, 8)
    position = possible_positions[i]
    row = position[0]
    index = position[1]
    return row, index


def play_game(player2):
    """Runs the tic tac toe game"""
    while board.turn < 10:

        # Determine active player

        if board.turn % 2 != 0:
            active_player = player1
        else:
            active_player = player2

        board.print_board()
        print(f"{active_player.name}'s turn. Where would you like to place your symbol?")

        position = "invalid"
        while position == "invalid":

            if active_player.type == "human":

                # Ask player where they want to place their symbol

                row = "invalid"
                while row == "invalid":
                    row = board.get_row()
                    if row == "invalid":
                        print("That choice is invalid. Please try again.")

                index = "invalid"
                while index == "invalid":
                    index = board.get_column()
                    if index == "invalid":
                        print("That choice is invalid. Please try again.")

            else:
                
                # Computer player chooses where to place their symbol
                
                row_choice, index = computer_turn()
                if row_choice == "t":
                    row = board.top_row
                elif row_choice == "m":
                    row = board.middle_row
                elif row_choice == "b":
                    row = board.bottom_row

            # Check if position is already taken

            position_available = board.check_square(row, index)
            if position_available:
                board.place_square(active_player.square, row, index)
                position = "valid"
                board.turn += 1
            else:
                if active_player.type == "human":
                    print("That position is already taken. Please try again.")

        # Beginning in fifth turn, check for win

        if board.turn <= 5:
            continue
        else:
            win = board.check_win()
            if win:
                board.print_board()
                print(f"{active_player.name} wins. Game over!")
                board.score[active_player.index] += 1
                board.turn = 11

    # Message if tie game

    if board.turn == 10:
        board.print_board()
        print("It's a tie! Better luck next time.")

    # Print score if win or tie

    if board.turn >= 10:
        print(f"Score: {player1.name}: {board.score[player1.index]}, {player2.name}: {board.score[player2.index]}")


def play_again():
    """Ask if player(s) want(s) to play again"""
    another_round = 0
    while another_round == 0:
        another_round = input("Would you like to play again? (Y / N) ").lower()
        if another_round == "n":
            print("Thanks for playing. Goodbye!")
            return False
        elif another_round == "y":
            print("Great! Let's play again!")
            board.turn = 1
            board.reset()
            return True
        else:
            print("That is not a valid response! Please enter Y or N.")
            another_round = 0


# Run the game

playing = True

print("Welcome to Tic Tac Toe!")
while playing:
    player2 = get_num_players()
    play_game(player2)
    playing = play_again()
