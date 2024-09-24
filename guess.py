#!/usr/bin/python3

import random

SCOREFILE = "guess.sc"

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

# Main function
def main():
    score = loadScore()
    print(f"Games played: {score['g']}, average guesses: {score['a']}")

    count = 0
    secret = random.randint(1, 100)
    while True:
        count += 1
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the secret number in {count} guesses! Goodbye.")
            break
    
    score['g'] += 1
    score['a'] = ((score['g'] - 1) * score['a'] + count) / score['g']
    saveScore(score)    
        
# Call main function
if __name__ == '__main__':
    main()