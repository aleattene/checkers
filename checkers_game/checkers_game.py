from checkers_game.chessboard import Chessboard
from checkers_game.move import Move
from checkers_game.player import Player


class CheckersGame:
    """ Business Logic"""

    # Chessboard Initialization
    chessboard = Chessboard()   # copy?

    # Players Initialization
    player_01 = Player("player_01", "W")
    player_02 = Player("player_02", "B")

    # Display Chessboard and Player
    chessboard.print_chessboard()
    print(player_01)
    print(player_02)

    while True:
        # Move Player 01
        # Insert move
        move = Move(chessboard, player_01)
        if move.move:
            break
        # Check move
        while True:
            legal_move = move.check_move(chessboard, player_01, move)
            if legal_move:
                print("Mossa Consentita")
                chessboard.update_chessboard(move, player_01)
                chessboard.print_chessboard()
                print(player_01)
                print(player_02)
                break
            else:
                print("Mossa NON Consentita")
                move = Move(chessboard, player_01)
                if move.move:
                    break
                # Fix double blank line

        # Player 02
        # Insert move
        move = Move(chessboard, player_02)
        if move.move:
            break
        # Check move
        while True:
            if move.check_move(chessboard, player_02, move):
                print("Mossa Consentita")
                chessboard.update_chessboard(move, player_02)
                chessboard.print_chessboard()
                print(player_01)
                print(player_02)
                break
            else:
                print("Mossa NON Consentita")
                move = Move(chessboard, player_02)
                if move.move:
                    break

    # print(move.move_from_row)
    # print(move.move_from_col)
    # print(initial_chessboard[move_from_row][move_from_col])
    # print(move.move_to_row)
    # print(move.move_to_col)
    # print(initial_chessboard[move_to_row][move_to_col])

