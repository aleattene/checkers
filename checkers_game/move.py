

class Move:

    def __init__(self, chessboard):
        self.move_from_row = 0     # int
        self.move_from_col = 0     # int
        self.move_to_row = 0       # int
        self.move_to_col = 0       # int
        self.make_move(chessboard)

    def make_move(self, chessboard):
        while True:
            move = input("Enter the move (for example A3-B4): ")
            if Move.check_syntax_move(move):
                break
            print("Insert Error. Retry.")
        self.move_from_row = (int(move[1])) - 1
        self.move_from_col = chessboard.cols_map[move[0].upper()]
        self.move_to_row = (int(move[4])) - 1
        self.move_to_col = chessboard.cols_map[move[3].upper()]

    @staticmethod
    def check_syntax_move(move):
        if len(move) == 5 and \
                move[2] == "-" and \
                "A" <= move[0].upper() <= "H" and \
                "1" <= move[1] <= "8" and \
                "A" <= move[3].upper() <= "H" and \
                "1" <= move[4].upper() <= "8":
            return True

    def check_move(self, chessboard):
        move_from = False
        move_to = False
        if chessboard.disposition[self.move_from_row][self.move_from_col] == "W":
            move_from = True
        if chessboard.disposition[self.move_to_row][self.move_to_col] == "F":
            move_to = True
        # print(move_from)
        # print(move_to)
        if move_from and move_to:
            print("Mossa Consentita")
            chessboard.update_chessboard(self)
            chessboard.print_chessboard()
        else:
            print("Mossa NON Consentita")