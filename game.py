"""
Script for playing the game
"""

from utils.logger import logger
from configs.constants import Constants
from configs.configs import Configs
import random


DIFFICULTY = Configs.DIFFICULTY
GUESS_AVAILABLE = Configs.GUESSES_AVAILABLE

NUMBER_RANGE = Constants.Difficulty.NUMBER_RANGE.get(DIFFICULTY)
LOWER_NUMBER = NUMBER_RANGE[0]
HIGHER_NUMBER = NUMBER_RANGE[1]

logger.info("Let's play the game!")
logger.info("I'm thinking of a number between %s and %s.", LOWER_NUMBER, HIGHER_NUMBER)

secret_number = random.randint(LOWER_NUMBER, HIGHER_NUMBER)
logger.info("Can you guess it?")

guess_count = 0
while GUESS_AVAILABLE > 0:
    guess = int(input("Enter your guess: "))
    guess_count += 1
    GUESS_AVAILABLE -= 1

    if guess == secret_number:
        logger.info(
            "Congratulations! You guessed the number in %s guesses.", guess_count
        )
        break
    elif guess < secret_number:
        logger.info("Too low! You have %s guess remaining.", GUESS_AVAILABLE)
    else:
        logger.info("Too high! You have %s guess remaining.", GUESS_AVAILABLE)

