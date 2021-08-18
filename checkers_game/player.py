

class Player:

    def __init__(self, username, pieces_color):
        self.username = username
        self.pieces_color = pieces_color
        self.pieces_quantity = 12

    def __str__(self):
        return f"{self.username}: \"{self.pieces_color}\" - {self.pieces_quantity}"



