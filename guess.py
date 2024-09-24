#!/usr/bin/python3

"""
Program:   guess.py
Version:   1.0
Date:      24 September 2024
Author:    David Cleary
Licencing: Copyright 2024 SuniTAFE. All rights reserved.
Platforms: AWS-Linux
"""

# imports
import random

# globals
SCOREFILE = "guess.sc"

# functions
def loadScore():
    """
    Load score information from a text file.
    
    Returns:
        Score information (dictionary).
    """
    file = open(SCOREFILE, "r")
    scoreText = file.readline()
    score = {}
    score['g'] = int(scoreText.split()[0])
    score['a'] = float(scoreText.split()[1])
    file.close()
    return score
    
def saveScore(score):
    """
    Save score information to a text file.
    
    Parameters:
        score (dictionary): Score information.
    """
    file = open(SCOREFILE, "w")
    file.write(f"{score['g']} {score['a']}\n")
    file.close()

def main():
    """
    Main function
    Play the number guessing game.
    The number of games played and the average guesses are displayed.
    The user repeatedly guesses a number betwen 1 and 100 until they guess
    correctly.
    """
    # load and display previous score information, the number of games played 
    # and the average number of guesses
    score = loadScore()
    print(f"Games played: {score['g']}, average guesses: {score['a']}")

    # set the guess count to 0 and the secret number to a random integer
    # between 1 and 100
    count = 0
    secret = random.randint(1, 100)
    
    # main game loop
    while True:
        
        # increment the guess count and get the next guess from the user
        count += 1
        guess = int(input("Guess a number between 1 and 100: "))

        # compare user's guess and the secret number
        # display the comparison result
        # exit the loop if the user's guess matches the secret number
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the secret number in {count} guesses! Goodbye.")
            break
    
    # increment the number of games played, update the average number of
    # guesses and save the updated previous score information
    score['g'] += 1
    score['a'] = ((score['g'] - 1) * score['a'] + count) / score['g']
    saveScore(score)    
        
# call main function
if __name__ == '__main__':
    main()