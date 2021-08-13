

class Chessboard:

    cols_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

    def __init__(self):
        self.disposition = self.generate_chessboard()

    @staticmethod
    def generate_chessboard():
        # Static Chessboard
        initial_chessboard = [
            [0, "W", 0, "W", 0, "W", 0, "W"],  # line 0 - first line from the bottom
            ["W", 0, "W", 0, "W", 0, "W", 0],  # line 1
            [0, "W", 0, "W", 0, "W", 0, "W"],  # line 2
            ["F", 0, "F", 0, "F", 0, "F", 0],  # line 3
            [0, "F", 0, "F", 0, "F", 0, "F"],  # line 4
            ["B", 0, "B", 0, "B", 0, "B", 0],  # line 5
            [0, "B", 0, "B", 0, "B", 0, "B"],  # line 6
            ["B", 0, "B", 0, "B", 0, "B", 0],  # line 7
        ]
        return initial_chessboard

    def print_chessboard(self):
        print("╔{:^53}╗".format("═" * 53))  # ASCII code (201,205,187)
        row = 8
        for line in reversed(self.disposition):
            print("║▓ {} ▓".format(row), end="")
            row += -1
            for col in line:
                if col == 0:
                    print("║░░░░░", end="")
                elif col == "F":
                    print("║     ", end="")
                else:
                    print(f"║  {col}  ", end="")
            print("║")
            print("╠{:^53}╣".format("═" * 53))  # ASCII code (204,185,205)
        print("║▓▓▓▓▓║▓ A ▓║▓ B ▓║▓ C ▓║▓ D ▓║▓ E ▓║▓ F ▓║▓ G ▓║▓ H ▓║")
        print("╚{:^53}╝".format("═" * 53))  # ASCII code (200,188,205)

    def update_chessboard(self, move):
        self.disposition[move.move_from_row][move.move_from_col] = "F"
        self.disposition[move.move_to_row][move.move_to_col] = "W"
