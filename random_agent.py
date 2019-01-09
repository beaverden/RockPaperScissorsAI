import random
from helpers import opposite
from agent import Agent


class RandomAgent(Agent):
    def __init__(self):
        Agent.__init__(self)

    def move(self):
        return random.choice(['r', 'p', 's'])

    def train(self, opponent_move, agent_move, result):
        pass
