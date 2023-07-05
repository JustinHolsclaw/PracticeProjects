##Start game
##create board
##click the board
##react to click
##add to score or explode bomb
from Player import Player

def addPlayers():
    players = []
    print("How many players are there?")
    playerNumber = int(input()) ##input Validation needs to be more robust
    while playerNumber < 1 or playerNumber > 5:
        print("Please select a number between 1 and 4.")
        playerNumber = input()
    while playerNumber > 0:
        print("Please enter player name")
        playerName = input()
        player = Player.__new__(Player)
        player.__init__(playerName)
        players.append(player)
        playerNumber -= 1
    return players

def playGame():
    #createBoard
    pass
    

def main():
    addPlayers()
    playGame()
    

if __name__ == "__main__":
    main()

def startGame():
    pass

