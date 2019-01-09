from agent import Agent


class PlayerAgent(Agent):
    def __init__(self):
        Agent.__init__(self)

    def move(self):
        return input('r/s/p: ').strip()

    def train(self, opponent_move, agent_move, result):
        pass
