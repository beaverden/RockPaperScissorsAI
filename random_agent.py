import random
from helpers import opposite


class RandomAgent:
    def __init__(self):
        pass

    def move(self):
        return random.choice(['r', 'p', 's'])

    def train(self, opponent_move, agent_move, result):
        pass
