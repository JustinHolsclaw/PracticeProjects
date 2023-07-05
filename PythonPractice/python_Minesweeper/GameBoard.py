import random
from Tile import createTileObject
def create2dArray(Height, Width):
    heightIncrementor = 0
    widthIncrementor = 0
    array = [[]]
    while(heightIncrementor != Height):
        if(widthIncrementor != Width):
            array[heightIncrementor].append(random.randint(1,10))
            widthIncrementor = widthIncrementor+1
        elif(heightIncrementor == Height-1):
            heightIncrementor = heightIncrementor+1
        else:
            heightIncrementor = heightIncrementor+1
            array.append([])
            widthIncrementor = 0
    return array

#print(create2dArray(5,5))

def createGameBoardArray(Height, Width):
    heightIncrementor = 0
    widthIncrementor = 0
    array = [[]]
    while(heightIncrementor != Height):
        if(widthIncrementor != Width):
            array[heightIncrementor].append(createTileObject())
            widthIncrementor = widthIncrementor+1
        elif(heightIncrementor == Height-1):
            heightIncrementor = heightIncrementor+1
        else:
            heightIncrementor = heightIncrementor+1
            array.append([])
            widthIncrementor = 0
    return array