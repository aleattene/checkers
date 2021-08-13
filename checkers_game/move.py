

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
            if Move.check_move(move):
                break
            print("Insert Error. Retry.")
        self.move_from_row = (int(move[1])) - 1
        self.move_from_col = chessboard.cols_map[move[0].upper()]
        self.move_to_row = (int(move[4])) - 1
        self.move_to_col = chessboard.cols_map[move[3].upper()]

    @staticmethod
    def check_move(move):
        if len(move) == 5 and \
                move[2] == "-" and \
                "A" <= move[0].upper() <= "H" and \
                "1" <= move[1] <= "8" and \
                "A" <= move[3].upper() <= "H" and \
                "1" <= move[4].upper() <= "8":
            return True
