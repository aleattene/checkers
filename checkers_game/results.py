#########

import random


def check_result(player_01, player_02):

    
    if player_01.pieces_quantity == 0:
        print("GAME OVER - PLAYER 02 is the WINNER.")
        return True
    elif player_02.pieces_quantity == 0:
        print("GAME OVER - PLAYER 01 is the WINNER.")
        return True
    elif player_01.pieces_quantity == 2 and player_02.pieces_quantity ==2:
        print("GAME ENDED in a DRAW.")
        return True
    
    return False


# While loop 

"""player_01=12
player_02=12

while True:
    
    x= round(random.random())

    if x==0:
        player_01 -= 1
        
    elif x==1:
        player_02 -= 1
        

    print(player_01,player_02)

    if check_result(player_01,player_02):
       break"""

