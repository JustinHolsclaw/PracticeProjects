class Player:
    def __new__(cls, *args):
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        self.score = 0
    