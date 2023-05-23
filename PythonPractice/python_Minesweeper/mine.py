class Mine:
        def __init__(self, pointValue, isBomb):
            self.pointValue = pointValue
            self.isBomb = isBomb

class Player:
    def __init__(self, playerNumber, name):
        self.playerNumber = playerNumber
        self.name = name
        self.score = 0