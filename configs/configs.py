'''
Script contains configs
'''

import os


class Configs:
    """
    Game configs
    """
    difficulty = os.environ.get('DIFFICULTY', 'medium')