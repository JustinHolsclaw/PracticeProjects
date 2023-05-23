##Start game
##create board
##click the board
##react to click
##add to score or explode bomb
from mine import Player

def addPlayers():
    players = []
    print("How many players are there?")
    playerNumber = input()
    while playerNumber < 0 or playerNumber > 5:
        print("Please select a number greater than 0 but less than 5.")
        playerNumber = input()
    while playerNumber > 0:
        print("Please enter player name")
        playerName = input()
        players.__add__(Player(playerNumber, playerName))

def main():
    addPlayers()

if __name__ == "__main__":
    main()

def startGame():
    pass
main()