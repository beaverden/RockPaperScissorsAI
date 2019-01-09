import random
from collections import deque
from difflib import SequenceMatcher
import numpy as np
from agent import Agent
from helpers import opposite
from markov_agent import MarkovAgent


class MatchingAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.sequence = []
        self.last_sequence = deque(maxlen=10)
        self.actions = ['r', 'p', 's']
        self.values = {'r': 0, 'p': 1, 's': 2}
        self.markov = MarkovAgent()

    def move(self):
        if len(self.last_sequence) < 2:
            return random.choice(self.actions)
        else:
            data = ''.join(list(self.last_sequence))
            seq = ''.join(self.sequence)
            s = SequenceMatcher(None, data, seq)
            count = [0, 0, 0]
            found = False
            for i in range(len(data), 0, -1):
                weight = 1.0
                for j in range(len(seq) - i, 0, -1):
                    frag = seq[j:j + i]
                    if frag == data[-i:] and j + i < len(seq) - 1:
                        other = seq[j + i]
                        count[self.values[other]] += weight
                        if weight > 0.02:
                            weight -= 0.01
                        found = True
                if found:
                    break
            if not found:
                return self.markov.move()
            return opposite(self.actions[np.argmax(count)])

    def train(self, opponent_move, agent_move, result):
        self.sequence.append(opponent_move)
        self.last_sequence.append(opponent_move)
        self.markov.train(opponent_move, agent_move, result)
