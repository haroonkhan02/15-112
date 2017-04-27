import random

def invalidInput(player1):
    print("Invalid input.")
    if player1==True:
        playerInput= input("'r' is roll. 'h' is hold.\nPlayer 1 Turn:")
    elif player1==False:
        playerInput= input("'r' is roll. 'h' is hold.\nPlayer 2 Turn:")
    return playerInput

def playPig():
    p1Score=0
    p2Score=0
    playerScore=0
    randomRoll=0
    player1=True
    print("Welcome to PlayPig!")
    playerInput= input("'r' is roll. 'h' is hold.\nPlayer 1 Turn:")
    while True:
        if (playerInput != "r") and (playerInput != "h"):
            playerInput= invalidInput(player1)
        if playerInput == "h":
            if player1==True:
                p1Score+=playerScore
                player1=not player1
                print("Player 1 Score:", p1Score)
                if p1Score>=100:
                    print ("Congrats Player 1! You won! Try again, Player 2.")
                    return
                playerInput= input("Player 2 Turn:")
            elif player1==False:
                p2Score+=playerScore
                player1=True
                print("Player 2 Score:", p2Score)
                if p2Score>=100:
                    print ("Congrats Player 2! You won! Try again, Player 1.")
                    return
                playerInput= input("Player 1 Turn:")
            playerScore=0
        elif playerInput == "r":
            randomRoll= random.randint(1,6)
            if randomRoll==1:
                playerScore=0
                if player1==True:
                    player1= not player1
                    print("You rolled a 1.\nPlayer 1 Score:", p1Score)
                    playerInput= (input("Player 2 Turn:"))
                elif player1==False:
                    print("You rolled a 1.\nPlayer 2 Score:", p2Score)
                    playerInput= (input("Player 1 Turn:"))
                    player1= True
            elif randomRoll !=1:
                playerScore+=randomRoll
                print("You Rolled a:", randomRoll)
                playerInput= input("Roll Agian.\nTurn:")
        
playPig()