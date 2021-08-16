from checkers_game.chessboard import Chessboard
from checkers_game.move import Move
from checkers_game.player import Player
import time


class CheckersGame:
    """ Business Logic"""

    TIME = 0

    # Chessboard Initialization
    chessboard = Chessboard()   # copy?

    # Players Initialization
    player_01 = Player("player_01", "W")
    player_02 = Player("player_02", "B")

    # Both WINNER
    MOVES = ['H3G4', 'E6D5', 'F3E4', 'D5C4', 'E4D5', 'D7E6',
             'D3B5D7', 'E6F5', 'E2D3', 'C8E6C4E2', 'D1F3E4', 'G6H5', 'G4E6D7', 'H5G4',
             'E6D7', 'G4E2', 'G2H3', 'B7C6', 'H3G4', 'H7G6', 'G4F5', 'A6B5', 'F1D3', 'B5C4',
             'B3D5B7C8', 'A8C6', 'C2B3', 'G6E4C2D1', 'H1G2', 'G8H7', 'B3C4', 'H7G6',
             'C4D5', 'G6F5', 'G2F3', 'C6E4G2H1', 'B1D3E4', 'F7E6D5', 'A2B3', 'F5E4C2',
             'D3F5G7', 'E8C6', 'F5D7']

    """
    # PLAYER 01 - WINNER
    MOVES = ['H3G4', 'E6D5', 'F3E4', 'D5C4', 'E4D5', 'D7E6',
             'D3B5D7', 'E6F5', 'E2D3', 'C8E6C4E2', 'D1F3E4', 'G6H5', 'G4E6D7', 'H5G4',
             'E6D7', 'G4E2', 'G2H3', 'B7C6', 'H3G4', 'H7G6', 'G4F5', 'A6B5', 'F1D3', 'B5C4',
             'B3D5B7C8', 'A8C6', 'C2B3', 'G6E4C2D1', 'H1G2', 'G8H7', 'B3C4', 'H7G6',
             'C4D5', 'G6F5', 'G2F3', 'C6E4G2H1', 'B1D3E4', 'F7E6D5', 'A2B3', 'F5E4C2',
             'B3C4', 'E8F7', 'C4D5F7', 'F7G6', 'D3F5H7', 'G2F1', 'D5F7']
    """

    """
    # PLAYER 02 - WINNER
    MOVES = ['H3G4', 'E6D5', 'F3E4', 'D5C4', 'E4D5', 'D7E6',
             'D3B5D7', 'E6F5', 'E2D3', 'C8E6C4E2', 'D1F3E4', 'G6H5', 'G4E6D7', 'H5G4',
             'E6D7', 'G4E2', 'G2H3', 'B7C6', 'H3G4', 'H7G6', 'G4F5', 'A6B5', 'F1D3', 'B5C4',
             'B3D5B7C8', 'A8C6', 'C2B3', 'G6E4C2D1', 'H1G2', 'G8H7', 'B3C4', 'H7G6',
             'C4D5', 'G6F5', 'G2F3', 'C6E4G2H1', 'B1D3E4', 'F7E6D5', 'A2B3', 'F5E4C2',
             'B3C4D5', 'E4C2B1', 'C4B5A6', 'E8C6A4B3']
    """

    # Display Chessboard and Player
    chessboard.print_chessboard()
    print(player_01)
    print(player_02)

    # Game
    moves_list = MOVES.copy()

    while True:
        # Player 01
        move = Move(chessboard, player_01, moves_list)  # Insert move
        if move.move:
            break
        # Check move
        while True:
            if move.check_simple_move(chessboard, player_01, player_02):
                print("Mossa Consentita1")
                if len(move.move_from_to) > 4:
                    print("Altre Mosse NON Consentite")
                chessboard.print_chessboard()
                print(player_01)
                print(player_02)
                break
            elif move.check_complex_move(chessboard, player_01, player_02):
                print("Mossa Consentita2")
                move.move_from_to = move.move_from_to[2:]
                while True:
                    if len(move.move_from_to) < 4:
                        break
                    else:
                        if move.check_complex_move(chessboard, player_01, player_02):
                            print("Mossa Consentita3")
                            move.move_from_to = move.move_from_to[2:]
                        else:
                            print("Mossa NON Consentita4")
                            break
                chessboard.print_chessboard()
                print(player_01)
                print(player_02)
                break
            else:
                print("Mossa NON Consentita5")
                move = Move(chessboard, player_01, moves_list)
                if move.move:
                    break
                # Fix double blank line

        time.sleep(TIME)
        # Player 02
        # Insert move
        move = Move(chessboard, player_02, moves_list)
        if move.move:
            break
        # Check move
        while True:
            if move.check_simple_move(chessboard, player_02, player_01):
                print("Mossa Consentita1")
                if len(move.move_from_to) > 4:
                    print("Altre Mosse NON Consentite")
                chessboard.print_chessboard()
                print(player_01)
                print(player_02)
                break
            elif move.check_complex_move(chessboard, player_02, player_01):
                print("Mossa Consentita2")
                move.move_from_to = move.move_from_to[2:]
                while True:
                    if len(move.move_from_to) < 4:
                        break
                    else:
                        if move.check_complex_move(chessboard, player_02, player_01):
                            print("Mossa Consentita3")
                            move.move_from_to = move.move_from_to[2:]
                        else:
                            print("Mossa NON Consentita4")
                            break
                chessboard.print_chessboard()
                print(player_01)
                print(player_02)
                break
            else:
                print("Mossa NON Consentita5")
                move = Move(chessboard, player_02, moves_list)
                if move.move:
                    break
        time.sleep(TIME)
    # print(move.move_from_row)
    # print(move.move_from_col)
    # print(initial_chessboard[move_from_row][move_from_col])
    # print(move.move_to_row)
    # print(move.move_to_col)
    # print(initial_chessboard[move_to_row][move_to_col])

