"""
Main Script
"""

# Ignore pylint wanrings
# pylint: disable=line-too-long


import random
from flask import Flask, render_template, request, jsonify

from utils.logger import logger
from configs.constants import Constants
from configs.configs import Configs


GUESSES_AVAILABLE = Configs.GUESSES_AVAILABLE
NUMBER_RANGE = Constants.Difficulty.NUMBER_RANGE

app = Flask(__name__)

# Game state dictionary
game_state = {
    "secret_number": None,
    "guess_count": 0,
    "guesses_left": GUESSES_AVAILABLE,
    "lower_bound": None,
    "upper_bound": None,
}


def start_new_game(difficulty, guesses_available):
    lower, upper = NUMBER_RANGE.get(difficulty)
    game_state["secret_number"] = random.randint(lower, upper)
    game_state["guess_count"] = 0
    game_state["guesses_left"] = guesses_available
    game_state["lower_bound"] = lower
    game_state["upper_bound"] = upper
    logger.info(
        f"New game started. Difficulty: {difficulty.capitalize()}, Secret Number: {game_state['secret_number']}, Range: {lower}-{upper}, Guesses Available: {guesses_available}"
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start_game():
    data = request.get_json()
    difficulty = data.get("difficulty", "medium").lower()
    guesses_available = int(data.get("guesses", 100))
    start_new_game(difficulty, guesses_available)
    return jsonify(
        {
            "message": f"Game started! I'm thinking of a number between {game_state['lower_bound']} and {game_state['upper_bound']}.",
            "lower": game_state["lower_bound"],
            "upper": game_state["upper_bound"],
            "guesses_left": game_state["guesses_left"],
        }
    )


@app.route("/guess", methods=["POST"])
def guess():
    data = request.get_json()
    guess = int(data.get("guess"))
    game_state["guess_count"] += 1
    game_state["guesses_left"] -= 1
    response_message = ""

    if guess == game_state["secret_number"]:
        response_message = f"Congratulations! You guessed the number in {game_state['guess_count']} guesses."
        logger.info(response_message)
        game_state["guesses_left"] = 0
    elif guess < game_state["secret_number"]:
        response_message = (
            f"Too low! You have {game_state['guesses_left']} guesses remaining."
        )
        logger.info(response_message)
    else:
        response_message = (
            f"Too high! You have {game_state['guesses_left']} guesses remaining."
        )
        logger.info(response_message)

    if game_state["guesses_left"] <= 0 and guess != game_state["secret_number"]:
        response_message = "Game over! You've run out of guesses."
        logger.info(response_message)

    return jsonify(
        {"message": response_message, "guesses_left": game_state["guesses_left"]}
    )


if __name__ == "__main__":
    app.run(debug=True)
