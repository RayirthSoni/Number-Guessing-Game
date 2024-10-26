"""
Script contains configs
"""

# Ignore pylint warnings
# pylint: disable=line-too-long

import os


class Configs:
    """
    Game configs
    """

    difficulty = os.environ.get("DIFFICULTY", "medium")
