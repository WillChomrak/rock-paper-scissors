# want to make a simple app that randomly chooses rock, paper, or scissors to battle me
# later functionalities to add could be: score tracker

# so what do we need here?
# a func to take an input
# a func to randomly choose a r/p/s
# a func to compare both and return the winner

def playerChoice():
    selection = input("Please enter 'rock', 'paper', or 'scissors': ").lower()
    
    if selection == 'rock' or selection == 'paper' or selection == 'scissors':
        return selection
    else:
        print('Input not recognized. Please enter one of the options exactly.')
        return playerChoice()

     