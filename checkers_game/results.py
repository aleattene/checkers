# import random


class Result:

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


"""
# ONLY FOR TEST
player_01 = 12
player_02 = 12

while True:
    x = round(random.random())

    if x == 0:
        player_01 -= 1
    elif x == 1:
        player_02 -= 1

    print(player_01,player_02)

    if check_result(player_01,player_02):
       break
"""

