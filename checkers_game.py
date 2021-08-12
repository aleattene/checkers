# Entrypoint file

def main():
    # Static Chessboard
    initial_chessboard = [
        [0, "W", 0, "W", 0, "W", 0, "W"],   # line 0 - first line from the bottom
        ["W", 0, "W", 0, "W", 0, "W", 0],   # line 1
        [0, "W", 0, "W", 0, "W", 0, "W"],   # line 2
        ["F", 0, "F", 0, "F", 0, "F", 0],   # line 3
        [0, "F", 0, "F", 0, "F", 0, "F"],   # line 4
        ["B", 0, "B", 0, "B", 0, "B", 0],   # line 5
        [0, "B", 0, "B", 0, "B", 0, "B"],   # line 6
        ["B", 0, "B", 0, "B", 0, "B", 0],   # line 7
    ]

    cols_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 5, "H": 7}

    chessboard = initial_chessboard.copy()

    print("╔{:^53}╗".format("═" * 53))  # ASCII code (201,205,187)
    row = 1
    for line in reversed(chessboard):
        print("║▓ {} ▓".format(row), end="")
        row += 1
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

    """
    while True:
        move = input("Enter the move (for example A3-B4): ")
        if len(move) == 5 and \
                move[2] == "-" and \
                "A" <= move[0].upper() <= "H" and \
                "1" <= move[1] <= "8" and \
                "A" <= move[3].upper() <= "H" and \
                "1" <= move[4].upper() <= "8":
            break
        print("Insert Error. Retry.")

    move_from_col = cols_map[move[0].upper()]
    move_from_row = (int(move[1]))-1
    move_to_col = cols_map[move[3].upper()]
    move_to_row = (int(move[4])) - 1

    # print(move_from_row)
    # print(move_from_col)
    # print(initial_chessboard[move_from_row][move_from_col])

    move_from = False
    move_to = False

    if chessboard[move_from_row][move_from_col] == "W":
        move_from = True

    # print(move_to_row)
    # print(move_to_col)
    # print(initial_chessboard[move_to_row][move_to_col])

    if chessboard[move_to_row][move_to_col] == "F":
        move_to = True

    if move_from and move_to:
        print("Mossa Consentita")
    else:
        print("Mossa NON Consentita")

    print(move_from)
    print(move_to)
    """


if __name__ == "__main__":
    main()

