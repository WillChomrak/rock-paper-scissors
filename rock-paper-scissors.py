# want to make a simple app that randomly chooses rock, paper, or scissors to battle me
# later functionalities to add could be: score tracker

# so what do we need here?
# a func to take an input
# a func to randomly choose a r/p/s
# a func to compare both and return the winner

import random

fighters = ['rock', 'paper', 'scissors']

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



     