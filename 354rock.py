# Program #5 – Rock Program
# Programmer:  345Fritz
# Class:  CS 1010, Spring 2019
# Due Date: May. 1, 2019
# Purpose of program: Rock, paper, scissors game

import random

def main():

    # call to function
    userChoice = getUserChoice()

    # loop through functions
    while not (userChoice >= 4 or userChoice == 0):
        computerChoice = getComputerChoice()
        winner = determineWinner(userChoice, computerChoice)
        strUserChoice = convertChoice(userChoice)
        strCompChoice = convertCompChoice(computerChoice)
        win = convertWin(winner)

        # output
        print("="*30)
        print("Your choice =", strUserChoice)
        print("Computer Choice =", strCompChoice)
        print("Who won?:", win)
        print("="*30)

        # restart game
        getUserChoice()


# allow the user to make a choice, if its greater or equal to 4 exit the game
def getUserChoice():

    # input
    choice = int(input("Game Menu\n----------\n1)Rock\n2)Paper\n3)Scissors\n4)Quit\nEnter your choice here: "))
    if choice == 4:
        exit()
    else:
        choice = int(input("Enter a valid choice: "))
    return choice

# generate random number
def getComputerChoice():

    choice = random.randint(1, 3)
    return choice

# determine the winner
def determineWinner(userChoice, computerChoice):

    if userChoice == 1 and computerChoice == 2:
        winner = 2
    elif userChoice == 2 and computerChoice == 3:
        winner = 2
    elif userChoice == 3 and computerChoice == 1:
        winner = 2
    elif userChoice == computerChoice:
        winner = 0
    else:
        winner = 1
    return winner

# convert the numeric choice into a string for output
def convertChoice(userChoice):

    if userChoice == 1:
        strUserChoice = "Rock"
    elif userChoice == 2:
        strUserChoice = "Paper"
    elif userChoice == 3:
        strUserChoice = "Scissors"
    else:
        return
    return strUserChoice

# convert the numeric value that the computer generated into a string for output
def convertCompChoice(computerChoice):

    if computerChoice == 1:
        strCompChoice = "Rock"
    elif computerChoice == 2:
        strCompChoice = "Paper"
    elif computerChoice == 3:
        strCompChoice = "Scissors"
    else:
        return
    return strCompChoice

# convert the numeric number assigned to the winner into a string for output
def convertWin(winner):

    if winner == 1:
       winnerCode = "User"
    elif winner == 2:
        winnerCode = "Computer"
    else:
        winnerCode = "Draw!"
    return winnerCode

# end
main()
