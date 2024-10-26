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

    DIFFICULTY = os.environ.get("DIFFICULTY", "medium")
