

class Move:

    def __init__(self, chessboard, player):
        self.move_from = ""         # int
        self.move_to = ""       # int
        self.move = self.make_move(chessboard, player)

    def make_move(self, chessboard, player):
        while True:
            move = input(player.username + " - Enter the move (for example A3-B4 / blank line to quit): ")
            check = Move.check_syntax_move(move)
            if check[0]:
                break
            print("Insert Error. Retry.")
        if check[1]:
            return check[1]
        else:
            self.move_from = move[0].upper() + move[1]
            self.move_to = move[3].upper() + move[4]
            self.move = False

    @staticmethod
    def check_syntax_move(move):
        if move == "":
            return True, True
        elif len(move) == 5 and \
                move[2] == "-" and \
                "A" <= move[0].upper() <= "H" and \
                "1" <= move[1] <= "8" and \
                "A" <= move[3].upper() <= "H" and \
                "1" <= move[4].upper() <= "8":
            return True, False
        else:
            return False, False

    def check_move(self, chessboard, player, move):
        if move.move_from in chessboard.square_not_allowed \
                or move.move_to in chessboard.square_not_allowed:
            return False
        else:
            if player.pieces_color == "W":
                if chessboard.disposition[move.move_from] == "W":
                    if chessboard.disposition[move.move_to] == "F":
                        return True
            elif player.pieces_color == "B":
                if chessboard.disposition[move.move_from] == "B":
                    if chessboard.disposition[move.move_to] == "F":
                        return True
            else:
                return False
        """
        move_from = False
        move_to = False
        remove = False
        # Simple Move
        if player.pieces_color == "W":
            if chessboard.disposition[self.move_from_row][self.move_from_col] == "W":
                move_from = True
                if self.move_to_col in [self.move_from_col + 1, self.move_from_col - 1]:
                    if self.move_to_row == self.move_from_row + 1:
                        if chessboard.disposition[self.move_to_row][self.move_to_col] == "F":
                            move_to = True
                elif self.move_to_col in [self.move_from_col + 2, self.move_from_col - 2]:
                    if self.move_to_row == self.move_from_row + 2:
                        if chessboard.disposition[self.move_to_row][self.move_to_col] == "F":
                            if chessboard.disposition[self.move_to_row - 1][self.move_to_col - 1] == "B" \
                                    or chessboard.disposition[self.move_to_row - 1][self.move_to_col + 1] == "B":
                                move_to = True
                                remove = True
                                # Rimuovere B dalla chessboard
                                # Decrementare B dal player
                                # Chiedere se proseguire
        elif player.pieces_color == "B":
            if chessboard.disposition[self.move_from_row][self.move_from_col] == "B":
                move_from = True
                if self.move_to_col in [self.move_from_col + 1, self.move_from_col - 1]:
                    if self.move_to_row == self.move_from_row - 1:
                        if chessboard.disposition[self.move_to_row][self.move_to_col] == "F":
                            move_to = True
                elif self.move_to_col in [self.move_from_col + 2, self.move_from_col - 2]:
                    if self.move_to_row == self.move_from_row - 2:
                        if chessboard.disposition[self.move_to_row][self.move_to_col] == "F":
                            if chessboard.disposition[self.move_to_row + 1][self.move_to_col + 1] == "W" \
                                    or chessboard.disposition[self.move_to_row + 1][self.move_to_col + 1] == "W":
                                move_to = True
                                remove = True
                                # Rimuovere W dalla chessboard
                                # Decrementare W dal player
                                # Chiedere se proseguire
        # print(move_from)
        # print(move_to)
        if move_from and move_to:
            return True, remove
        """