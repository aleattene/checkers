# Entrypoint file
from checkers_game.chessboard import Chessboard
from checkers_game.move import Move


def main():

    # Generate Initial Chessboard
    chessboard = Chessboard()   # copy?

    # Display Chessboard
    chessboard.print_chessboard()

    # Make move
    move = Move(chessboard)

    # print(move.move_from_row)
    # print(move.move_from_col)
    # print(initial_chessboard[move_from_row][move_from_col])

    move_from = False
    move_to = False

    if chessboard.disposition[move.move_from_row][move.move_from_col] == "W":
        move_from = True

    # print(move.move_to_row)
    # print(move.move_to_col)
    # print(initial_chessboard[move_to_row][move_to_col])

    if chessboard.disposition[move.move_to_row][move.move_to_col] == "F":
        move_to = True

    # print(move_from)
    # print(move_to)

    if move_from and move_to:
        print("Mossa Consentita")
        chessboard.update_chessboard(move)
        chessboard.print_chessboard()
    else:
        print("Mossa NON Consentita")


if __name__ == "__main__":
    main()

