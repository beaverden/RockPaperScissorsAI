import random
from helpers import opposite


class BiasedAgent:
    def __init__(self):
        self.bias = {'r': 0.35, 'p': 0.3233, 's': 0.3267}
        self.cumulative = []
        self.names = []
        for val, p in self.bias.items():
            if self.cumulative:
                self.cumulative.append(p + self.cumulative[-1])
            else:
                self.cumulative.append(p)
            self.names.append(val)

    def move(self):
        rand = random.random()
        for i in range(len(self.cumulative)):
            if rand < self.cumulative[i]:
                return self.names[i]

    def train(self, opponent_move, agent_move, result):
        pass
