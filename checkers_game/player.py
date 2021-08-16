# Player


class Player:

    MOVES_WINNER = ['H3G4', 'E6D5', 'F3E4', 'D5C4', 'E4D5', 'D7E6',
                    'D3B5D7', 'E6F5', 'E2D3', 'C8E6C4E2', 'D1F3E4', 'G6H5', 'G4E6D7', 'H5G4',
                    'E6D7', 'G4E2', 'G2H3B7C6', 'H3G4', 'G4F5', 'A6B5', 'F1D3', 'B5C4', 'B3D5B7C8',
                    'A8C6', 'C2B3', 'G6E4C2D1', 'H1G2', 'G8F7', 'C4D5', 'G6F5', 'G2F3', 'C6E4G2H1',
                    'B1D3E4', 'F7E6D5', 'A2B3', 'F5E4C2']

    def __init__(self, username, pieces_color):
        self.username = username
        self.pieces_color = pieces_color
        self.pieces_quantity = 12

    def __str__(self):
        return f"{self.username}: \"{self.pieces_color}\" - {self.pieces_quantity}"


