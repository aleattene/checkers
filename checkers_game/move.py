

class Move:

    simple_moves_w_allowed = ["B1A2", "B1C2", "D1C2", "D1E2", "F1E2", "F1G2", "H1G2",
                              "A2B3", "C2B3", "C2D3", "E2D3", "E2F3", "G2F3", "G2H3",
                              "B3A4", "B3C4", "D3C4", "D3E4", "F3E4", "F3G4", "H3G4",
                              "A4B5", "C4B5", "C4D5", "E4D5", "E4F5", "G4F5", "G4H5",
                              "B5A6", "B5C6", "D5C6", "D5E6", "F5E6", "F5G6", "H5G6",
                              "A6B7", "C6B7", "C6D7", "E6D7", "E6F7", "G6F7", "G6H7",
                              "B7A8", "B7C8", "D7C8", "D7E8", "F7E8", "F7G8", "H7G8"]

    complex_moves_w_allowed = {
        "B1D3": "C2", "D1F3": "E2", "D1B3": "C2", "F1D3": "E2", "F1H3": "G2", "H1F3": "G2",
        "A2C4": "B3", "C2A4": "B3", "C2E4": "D3", "E2C4": "D3", "E2G4": "F3", "G2E4": "F3",
        "B3D5": "C4", "D3B5": "C4", "D3F5": "E4", "F3D5": "E4", "F3H5": "G4", "H3F5": "G4",
        "A4C6": "B5", "C4A6": "B5", "C4E6": "D5", "E4C6": "D5", "E4G6": "F5", "G4E6": "F5",
        "B5D7": "C6", "D5B7": "C6", "D5F7": "E6", "F5D7": "E6", "F5H7": "G6", "H5E7": "G6",
        "A6C8": "B7", "C6A8": "B7", "C6E8": "D7", "E6C8": "D7", "E6G8": "E7", "G6E8": "E7",
    }

    def __init__(self, player, moves_list):
        self.move_from_to = ""         # int
        self.move = self.make_move(player, moves_list)

    def __str__(self):
        pass

    def make_move(self, player, moves_list):
        while True:
            # move = input(player.username + " - Enter the move (for example A3-B4 / blank line to quit): ")
            # """
            if len(moves_list) == 0:
                check = True, True
                break
            move = moves_list[0]
            # """
            print("Move of " + player.username + ": " + move)
            moves_list.pop(0)  #
            check = Move.check_syntax_move(move)
            if check[0]:
                break
            print("Insert Error. Retry.")
        if check[1]:
            return check[1]
        else:
            self.move_from_to = move.upper()
            self.move = False

    @staticmethod
    def check_syntax_move(move):
        if move == "":
            return True, True
        elif len(move) % 2 != 0:
            return False, False
        else:
            for i in range(0, len(move), 2):
                if not("A" <= move[i].upper() <= "H") or not("1" <= move[i+1] <= "8"):
                    return False, False
        return True, False

    def check_simple_move(self, chessboard, player_one):

        if self.move_from_to[:2] in chessboard.square_not_allowed \
                or self.move_from_to[2:4] in chessboard.square_not_allowed:
            return False    # Move is not allowed
        else:
            # Move player 01
            if player_one.pieces_color == "W":
                if chessboard.disposition[self.move_from_to[:2]] == "W":
                    if chessboard.disposition[self.move_from_to[2:4]] == "F":
                        if (self.move_from_to[:4]) in Move.simple_moves_w_allowed:
                            chessboard.disposition[self.move_from_to[:2]] = "F"
                            chessboard.disposition[self.move_from_to[2:4]] = player_one.pieces_color
                            return True
                elif chessboard.disposition[self.move_from_to[:2]] == "WWW":
                    if chessboard.disposition[self.move_from_to[2:4]] == "F":
                        if (self.move_from_to[:4]) in Move.simple_moves_w_allowed:
                            chessboard.disposition[self.move_from_to[:2]] = "F"
                            chessboard.disposition[self.move_from_to[2:4]] = "WWW"
                            return True
                        elif (self.move_from_to[2:4] + self.move_from_to[:2]) in Move.simple_moves_w_allowed:
                            chessboard.disposition[self.move_from_to[:2]] = "F"
                            chessboard.disposition[self.move_from_to[2:4]] = "WWW"
                            return True
            # Move player 02
            elif player_one.pieces_color == "B":
                if chessboard.disposition[self.move_from_to[:2]] == "B":
                    if chessboard.disposition[self.move_from_to[2:4]] == "F":
                        if (self.move_from_to[2:4] + self.move_from_to[:2]) in Move.simple_moves_w_allowed:
                            chessboard.disposition[self.move_from_to[:2]] = "F"
                            chessboard.disposition[self.move_from_to[2:4]] = player_one.pieces_color
                            return True
                elif chessboard.disposition[self.move_from_to[:2]] == "BBB":
                    if chessboard.disposition[self.move_from_to[2:4]] == "F":
                        if (self.move_from_to[2:4] + self.move_from_to[:2]) in Move.simple_moves_w_allowed:
                            chessboard.disposition[self.move_from_to[:2]] = "F"
                            chessboard.disposition[self.move_from_to[2:4]] = "BBB"
                            return True
                        elif (self.move_from_to[:4]) in Move.simple_moves_w_allowed:
                            chessboard.disposition[self.move_from_to[:2]] = "F"
                            chessboard.disposition[self.move_from_to[2:4]] = "BBB"
                            return True
        return False

    def check_complex_move(self, chessboard, player_one, player_two):

        if self.move_from_to[:2] in chessboard.square_not_allowed \
                or self.move_from_to[2:4] in chessboard.square_not_allowed:
            return False  # The move is not allowed
        else:
            # Move player 01
            if player_one.pieces_color == "W":
                if chessboard.disposition[self.move_from_to[:2]] == "W":
                    if chessboard.disposition[self.move_from_to[2:4]] == "F":
                        if (self.move_from_to[:4]) in Move.complex_moves_w_allowed:
                            if chessboard.disposition[Move.complex_moves_w_allowed[self.move_from_to[:4]]] \
                                    == player_two.pieces_color:
                                chessboard.disposition[self.move_from_to[:2]] = "F"
                                chessboard.disposition[self.move_from_to[2:4]] = player_one.pieces_color
                                chessboard.disposition[Move.complex_moves_w_allowed[self.move_from_to[:4]]] = "F"
                                player_two.pieces_quantity -= 1
                                return True
                elif chessboard.disposition[self.move_from_to[:2]] == "WWW":
                    if chessboard.disposition[self.move_from_to[2:4]] == "F":
                        if (self.move_from_to[:4]) in Move.complex_moves_w_allowed:
                            if chessboard.disposition[Move.complex_moves_w_allowed[self.move_from_to[:4]]]\
                                    in ["B", "BBB"]:
                                chessboard.disposition[self.move_from_to[:2]] = "F"
                                chessboard.disposition[self.move_from_to[2:4]] = "WWW"
                                chessboard.disposition[Move.complex_moves_w_allowed[self.move_from_to[:4]]] = "F"
                                player_two.pieces_quantity -= 1
                                return True
                        elif (self.move_from_to[2:4] + self.move_from_to[:2]) in Move.complex_moves_w_allowed:
                            if chessboard.disposition[Move.complex_moves_w_allowed[self.move_from_to[2:4]
                                                                                   + self.move_from_to[:2]]]\
                                    in ["B", "BBB"]:
                                chessboard.disposition[self.move_from_to[:2]] = "F"
                                chessboard.disposition[self.move_from_to[2:4]] = "WWW"
                                chessboard.disposition[Move.complex_moves_w_allowed[(self.move_from_to[2:4] +
                                                                                     self.move_from_to[:2])]] = "F"
                                player_two.pieces_quantity -= 1
                                return True
            # Move player 02
            elif player_one.pieces_color == "B":
                if chessboard.disposition[self.move_from_to[:2]] == "B":
                    if chessboard.disposition[self.move_from_to[2:4]] == "F":
                        if (self.move_from_to[2:4] + self.move_from_to[:2]) in Move.complex_moves_w_allowed:
                            if chessboard.disposition[Move.complex_moves_w_allowed[self.move_from_to[2:4] +
                                                                                   self.move_from_to[:2]]]\
                                    == player_two.pieces_color:
                                chessboard.disposition[self.move_from_to[:2]] = "F"
                                chessboard.disposition[self.move_from_to[2:4]] = player_one.pieces_color
                                chessboard.disposition[Move.complex_moves_w_allowed[(self.move_from_to[2:4] +
                                                                                     self.move_from_to[:2])]] = "F"
                                player_two.pieces_quantity -= 1
                                return True
                elif chessboard.disposition[self.move_from_to[:2]] == "BBB":
                    if chessboard.disposition[self.move_from_to[2:4]] == "F":
                        if (self.move_from_to[2:4] + self.move_from_to[:2]) in Move.complex_moves_w_allowed:
                            if chessboard.disposition[Move.complex_moves_w_allowed[self.move_from_to[2:4]
                                                                                   + self.move_from_to[:2]]] \
                                    in ["W", "WWW"]:
                                chessboard.disposition[self.move_from_to[:2]] = "F"
                                chessboard.disposition[self.move_from_to[2:4]] = "BBB"
                                chessboard.disposition[Move.complex_moves_w_allowed[(self.move_from_to[2:4] +
                                                                                     self.move_from_to[:2])]] = "F"
                                player_two.pieces_quantity -= 1
                                return True
                        if (self.move_from_to[:4]) in Move.complex_moves_w_allowed:
                            if chessboard.disposition[Move.complex_moves_w_allowed[self.move_from_to[:4]]] \
                                    in ["W", "WWW"]:
                                chessboard.disposition[self.move_from_to[:2]] = "F"
                                chessboard.disposition[self.move_from_to[2:4]] = "BBB"
                                chessboard.disposition[Move.complex_moves_w_allowed[self.move_from_to[:4]]] = "F"
                                player_two.pieces_quantity -= 1
                                return True
        return False
