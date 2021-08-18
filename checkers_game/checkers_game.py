from .chessboard import Chessboard
from .move import Move
from .player import Player
# from .result import Result


class Result:  # Export subsequently to the file result.py

    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def check_result(player_01, player_02):
        print(player_01)
        print(player_02)
        min_pieces = 1  # in production 2 or 3
        if player_01.pieces_quantity <= min_pieces and player_02.pieces_quantity <= min_pieces and \
                (player_01.pieces_quantity == player_02.pieces_quantity):
            print("GAME ENDED in a DRAW.")
            next_move = True
        elif player_01.pieces_quantity == 0:  # or (player_01.pieces_quantity == 1 and player_02.pieces_quantity == 3):
            print("GAME OVER - PLAYER 02 is the WINNER.")
            next_move = True
        elif player_02.pieces_quantity == 0:  # or (player_02.pieces_quantity == 1 and player_01.pieces_quantity == 3):
            print("GAME OVER - PLAYER 01 is the WINNER.")
            next_move = True
        else:
            next_move = False
        return next_move


class CheckersGame:
    """ Business Logic"""

    # Chessboard Initialization
    chessboard = Chessboard()   # copy?

    # Players Initialization
    player_01 = Player("Player_01", "W")
    player_02 = Player("Player_02", "B")

    """
    # Player_01 WINNER
    MOVES = ['H3G4', 'E6D5', 'F3E4', 'D5C4', 'E4D5', 'D7E6',
             'D3B5D7', 'E6F5', 'E2D3', 'C8E6C4E2', 'D1F3E4', 'G6H5', 'G4E6D7', 'H5G4',
             'E6D7', 'G4E2', 'G2H3', 'B7C6', 'H3G4', 'H7G6', 'G4F5', 'A6B5', 'F1D3', 'B5C4',
             'B3D5B7C8', 'A8C6', 'C2B3', 'G6E4C2D1', 'H1G2', 'G8H7', 'B3C4', 'H7G6',
             'C4D5', 'G6F5', 'G2F3', 'C6E4G2H1', 'B1D3E4', 'F7E6D5', 'A2B3', 'F5E4C2',
             'D3F5G7', 'G2F1', 'D7C8', 'E8D7', 'B3C4', 'D7C6', 'F5D7', 'E8C6', 'C4B5', 'C6A4',
             'C6B5', 'D7E8', 'B5D3', 'E8D7C6', 'B3C4', 'D3C2', 'C8B7', 'C2D1', 'B7C6', 'D1C2',
             'D7E8', 'F1E2', 'C6D5', 'E2F3', 'D5E4', 'C2D1C2', 'E8F7B5', 'D1E2D3', 'F7E6F5',
             'F3G4H5', 'E4F3D1', 'G4F5D7', 'F3G2', 'E2F3', 'E6G4E2F1']
    """

    """
    # Player_02 WINNER 
    MOVES = ['H3G4', 'E6D5', 'F3E4', 'D5C4', 'E4D5', 'D7E6',
             'D3B5D7', 'E6F5', 'E2D3', 'C8E6C4E2', 'D1F3E4', 'G6H5', 'G4E6D7', 'H5G4',
             'E6D7', 'G4E2', 'G2H3', 'B7C6', 'H3G4', 'H7G6', 'G4F5', 'A6B5', 'F1D3', 'B5C4',
             'B3D5B7C8', 'A8C6', 'C2B3', 'G6E4C2D1', 'H1G2', 'G8H7', 'B3C4', 'H7G6',
             'C4D5', 'G6F5', 'G2F3', 'C6E4G2H1', 'B1D3E4', 'F7E6D5', 'A2B3', 'F5E4C2',
             'D3F5G7', 'G2F1', 'D7C8', 'E8D7', 'B3C4', 'D7C6', 'F5D7', 'E8C6', 'C4B5', 'C6A4',
             'C6B5', 'D7E8', 'B5D3', 'E8D7C6', 'B3C4', 'D3C2', 'C8B7', 'C2D1', 'B7C6', 'D1C2',
             'D7E8', 'F1E2', 'C6D5', 'E2F3', 'D5E4', 'C2D1C2', 'E8F7B5', 'D1E2D3', 'F7E6F5', 'F3D5F7E8']

    """

    # """
    # Both WINNERS
    MOVES = ['H3G4', 'E6D5', 'F3E4', 'D5C4', 'E4D5', 'D7E6',
             'D3B5D7', 'E6F5', 'E2D3', 'C8E6C4E2', 'D1F3E4', 'G6H5', 'G4E6D7', 'H5G4',
             'E6D7', 'G4E2', 'G2H3', 'B7C6', 'H3G4', 'H7G6', 'G4F5', 'A6B5', 'F1D3', 'B5C4',
             'B3D5B7C8', 'A8C6', 'C2B3', 'G6E4C2D1', 'H1G2', 'G8H7', 'B3C4', 'H7G6',
             'C4D5', 'G6F5', 'G2F3', 'C6E4G2H1', 'B1D3E4', 'F7E6D5', 'A2B3', 'F5E4C2',
             'D3F5G7', 'G2F1', 'D7C8', 'E8D7', 'B3C4', 'D7C6', 'F5D7', 'E8C6', 'C4B5', 'C6A4',
             'C6B5', 'D7E8', 'B5D3', 'E8D7C6', 'B3C4', 'D3C2', 'C8B7', 'C2D1', 'B7C6', 'D1C2',
             'D7E8', 'F1E2', 'C6D5', 'E2F3', 'D5E4', 'C2D1C2', 'E8F7B5', 'D1E2D3', 'F7E6F5',
             'F3D5C6', 'E6C4B3']
    # """

    # Display Chessboard and Players
    chessboard.print_chessboard()
    print(player_01)
    print(player_02)

    # Moves List (Winner: player_01, player_02 or both)
    moves_list = MOVES.copy()
    # moves_list = []
    while True:
        # Player 01 - Insert move(s)
        move = Move(player_01, moves_list)
        # Blank line entered
        if move.move:
            break
        # Check Move(s)
        while True:
            if move.check_simple_move(chessboard, player_01):
                print("Mossa Consentita: " + move.move_from_to[:4])
                if len(move.move_from_to) > 4:
                    print("Altre Mosse NON Consentite")
                break
            elif move.check_complex_move(chessboard, player_01, player_02):
                print("Mossa Consentita: " + move.move_from_to[:4])
                move.move_from_to = move.move_from_to[2:]
                while True:
                    if len(move.move_from_to) < 4:
                        break
                    else:
                        if move.check_complex_move(chessboard, player_01, player_02):
                            print("Mossa Consentita: " + move.move_from_to[:4])
                            move.move_from_to = move.move_from_to[2:]
                        else:
                            print("Mossa NON Consentita: " + move.move_from_to[:4])
                            break
                break
            else:
                print("Mossa NON Consentita: " + move.move_from_to[:4])
                move = Move(player_01, moves_list)
                if move.move:
                    break

        # Update Chessboard
        chessboard.check_checkers()
        # Display Chessboard
        chessboard.print_chessboard()
        # Check Result
        if Result.check_result(player_01, player_02):
            break

        # Player 02 - Insert move(s)
        move = Move(player_02, moves_list)
        # Blank line entered
        if move.move:
            break
        # Check move(s)
        while True:
            if move.check_simple_move(chessboard, player_02):
                print("Mossa Consentita: " + move.move_from_to[:4])
                if len(move.move_from_to) > 4:
                    print("Altre Mosse NON Consentite")
                break
            elif move.check_complex_move(chessboard, player_02, player_01):
                print("Mossa Consentita: " + move.move_from_to[:4])
                move.move_from_to = move.move_from_to[2:]
                while True:
                    if len(move.move_from_to) < 4:
                        break
                    else:
                        if move.check_complex_move(chessboard, player_02, player_01):
                            print("Mossa Consentita: " + move.move_from_to[:4])
                            move.move_from_to = move.move_from_to[2:]
                        else:
                            print("Mossa NON Consentita: " + move.move_from_to[:4])
                            break
                break
            else:
                print("Mossa NON Consentita: " + move.move_from_to[:4])
                move = Move(player_02, moves_list)
                if move.move:
                    break

        # Update Chessboard
        chessboard.check_checkers()
        # Display Chessboard
        chessboard.print_chessboard()
        # Check Result
        if Result.check_result(player_01, player_02):
            break


