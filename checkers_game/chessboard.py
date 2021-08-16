

class Chessboard:

    square_not_allowed = ["A1", "C1", "E1", "G1",
                          "B2", "D2", "F2", "H2",
                          "A3", "C3", "E3", "G3",
                          "B4", "D4", "F4", "H4",
                          "A5", "C5", "E5", "G5",
                          "B6", "D6", "F6", "H6",
                          "A7", "C7", "E7", "G7",
                          "B8", "D8", "F8", "H8"]

    def __init__(self):
        self.disposition = self.generate_chessboard()

    @staticmethod
    def generate_chessboard():
        # Static Chessboard
        square_allowed_map = {
            "A8": "B", "C8": "B", "E8": "B", "G8": "B",
            "B7": "B", "D7": "B", "F7": "B", "H7": "B",
            "A6": "B", "C6": "B", "E6": "B", "G6": "B",
            "B5": "F", "D5": "F", "F5": "F", "H5": "F",
            "A4": "F", "C4": "F", "E4": "F", "G4": "F",
            "B3": "W", "D3": "W", "F3": "W", "H3": "W",
            "A2": "W", "C2": "W", "E2": "W", "G2": "W",
            "B1": "W", "D1": "W", "F1": "W", "H1": "W",
        }
        return square_allowed_map

    def print_chessboard(self):
        print("╔{:^53}╗".format("═" * 53))  # ASCII code (201,205,187)
        rows, cols, i = 8, 8, 0                    # constants
        pieces = list(self.disposition.values())    # from dict to list
        for row in range(rows, 0, -1):
            print("║▓ {} ▓".format(row), end="")
            if row % 2 == 0:
                for col in range(1, cols, 2):
                    if pieces[i][0] != "F":
                        print(f"║  {pieces[i][0]}  ", end="")
                        print("║░░░░░", end="")
                    else:
                        print("║     ", end="")
                        print("║░░░░░", end="")
                    i += 1
                print("║")
            else:
                for col in range(1, cols, 2):
                    print("║░░░░░", end="")
                    if pieces[i][0] != "F":
                        print(f"║  {pieces[i][0]}  ", end="")
                    else:
                        print("║     ", end="")
                    i += 1
                print("║")
            print("╠{:^53}╣".format("═" * 53))  # ASCII code (204,185,205)
        print("║▓▓▓▓▓║▓ A ▓║▓ B ▓║▓ C ▓║▓ D ▓║▓ E ▓║▓ F ▓║▓ G ▓║▓ H ▓║")
        print("╚{:^53}╝".format("═" * 53))  # ASCII code (200,188,205)
        # print(self.disposition)



