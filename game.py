'''
Script for playing the game
'''

from utils.logger import logger
import os
from configs.constants import Constants
from configs.configs import Configs
import random

def play_game():
    '''
    Function to play the game
    '''
    print(Configs.difficulty)

    logger.info("Let's play the game!")
    logger.info("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    logger.info("Can you guess it?")

    # Initialize the guess count
    guess_count = 0

    # Loop until the user guesses the correct number
    while True:
        # Get the user's guess
        guess = int(input("Enter your guess: "))

        # Increment the guess count
        guess_count += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {guess_count} guesses.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

play_game()