from collections import deque
from helpers import opposite
import numpy as np
from agent import Agent


class MarkovModel:
    def __init__(self):
        self.pair_count = {}
        self.element_count = {}
        self.model_size = 0

    def add(self, a, b):
        self.model_size += 1
        updated_count = self.pair_count.get((a, b), 0) + 1
        self.pair_count[(a, b)] = updated_count
        self.element_count[a] = self.element_count.get(a, 0) + 1
        self.element_count[b] = self.element_count.get(b, 0) + 1

    def probability(self, sequence: list) -> float:
        p = 1
        for a, b in zip(sequence, sequence[1:]):
            if self.element_count.get(a, 0) == 0:
                return 0
            p *= self.pair_count.get((a, b), 0) / self.element_count[a]
        return p


class MarkovAgent(Agent):
    def __init__(self, maxlen=5):
        Agent.__init__(self)
        self.model = MarkovModel()
        self.last_opponent_moves = deque(maxlen=maxlen)

    def train(self, opponent_move, agent_move, result):
        if self.last_opponent_moves:
            self.model.add(self.last_opponent_moves[-1], opponent_move)
        self.last_opponent_moves.append(opponent_move)

    def move(self):
        all_moves = [
            (list(self.last_opponent_moves) + ['r'], 'r'),
            (list(self.last_opponent_moves) + ['s'], 's'),
            (list(self.last_opponent_moves) + ['p'], 'p'),
        ]
        probs = [self.model.probability(pair[0]) for pair in all_moves]
        return opposite(all_moves[np.argmax(probs)][1])
