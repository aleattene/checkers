from checkers_game.chessboard import Chessboard
from checkers_game.move import Move


class CheckersGame:
    """ Business Logic"""

    # Chessboard Initialization
    chessboard = Chessboard()   # copy?

    # Display Chessboard
    chessboard.print_chessboard()

    # Insert move
    move = Move(chessboard)

    # Check move
    move.check_move(chessboard)

    # print(move.move_from_row)
    # print(move.move_from_col)
    # print(initial_chessboard[move_from_row][move_from_col])
    # print(move.move_to_row)
    # print(move.move_to_col)
    # print(initial_chessboard[move_to_row][move_to_col])

