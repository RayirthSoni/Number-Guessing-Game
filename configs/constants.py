"""
Constants
"""


class Constants:
    """
    Constants configurations
    """

    class Difficulty:
        """
        Difficulty configurations
        """

        possible_difficulties = ["easy", "medium", "hard"]
        default_difficulty = "medium"
        number_range = {"easy": (1, 10), "medium": (1, 100), "hard": (1, 1000)}
