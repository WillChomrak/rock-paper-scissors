# want to make a simple app that randomly chooses rock, paper, or scissors to battle me
# later functionalities to add could be: score tracker

# so what do we need here?
# a func to take an input
# a func to randomly choose a r/p/s
# a func to compare both and return the winner
# an engine function

import random

fighters = ['rock', 'paper', 'scissors']
score = [0, 0]

# func to take request and take input from user 
# and to check if user has input one of 3 options
def playerChoice():
    # takes input and converts to all lowercase for simplicity
    selection = input("Please enter 'rock', 'paper', or 'scissors': ").lower()
    
    # check user input an appropriate choice
    if selection in fighters:
        return selection
    else:
        print('Input not recognized. Please enter one of the options exactly.')
        return playerChoice()

# func to randomly select computer fighter
def compChoice():
    # generate random number between 0 and 2 INCLUSIVE
    randNum = random.randint(0, 2)
    # pick fighter using randNum
    selection = fighters[randNum]
    return selection

# ok now is the tricky part. How do I get this to compare the two choices and determine the winner?
# This could be a boolean ... maybe ... how would I record a draw?
def fight(playerChoice, compChoice):
    if playerChoice == compChoice:
        return "draw"
    # if player chooses rock
    if playerChoice == "rock":
        # rock beats scissors
        if compChoice == "scissors":
            return "winner"
        # rock doesn't beat paper
        else:
            return "loser"
    # if player chooses paper
    elif playerChoice == "paper":
        # paper beats rock
        if compChoice == "rock":
            return "winner"
        # paper doesn't beat scissors
        else:
            return "loser"
    # if player chosses scissors
    else:
        # scissors beats paper
        if compChoice == "paper":
            return "winner"
        # scissors doesn't beat rock
        else:
            return "loser"

def playAgain():
    # retrieve input from user: play again y/n
    again = input("Would you like to play againg (y/n)").lower()
    # if yes run game engine
    if again == "y" or again == "yes":
        gameEngine()
    # if no do nothing (later change this to print final score)
    elif again == "n" or again == "no":
        return
    # if incorrect input print message and re-run playAgain()
    else:
        print("Input not recognized. Please enter 'y' or 'n' exactly")
        playAgain()

def incrementScore(result):
    # if user wins add a point to their score
    if result == "winner":
        score[0] += 1
    # if comp wins add a point to it's score
    elif result == "loser":
        score[1] += 1

# This engine runs all the other functions
def gameEngine():
    # get player choice
    pChoice = playerChoice()
    print("You chose: ", pChoice)
    # get comp choice
    cChoice = compChoice()
    print("The computer chose: ", cChoice)
    # compare choices for winner
    result = fight(pChoice, cChoice)
    print(result)
    # change score based on results
    incrementScore(result)
    # print current score to screen
    print("Score: You - {}, Computer - {}".format(score[0], score[1]))
    # ask user to play again
    playAgain()

gameEngine()

