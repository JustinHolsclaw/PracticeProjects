import random

class Tile():
    def __init__(self, value, isMine):
        self.value = value
        self.isMine = isMine

def createTileObject():
    value = getRandomValue()
    if(value == "mine"):
        return Tile(0, True)
    else:
        return Tile(value, False)

def getRandomValue():
    possibleValues = [1, 2, 3, 4, 5, "mine"]
    return random.choice(possibleValues)
