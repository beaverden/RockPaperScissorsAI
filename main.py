import matching_agent
import random_agent
from helpers import evaluate
from agent import Agent


class Game:
    def __init__(self, iterations: int, player1: Agent, player2: Agent) -> None:
        self.player1 = player1
        self.player2 = player2
        self.iterations = iterations

    def start(self) -> None:
        ties = 0
        p1 = 0
        p2 = 0

        for i in range(self.iterations):
            player1_move = self.player1.move()
            player2_move = self.player2.move()
            result = evaluate(player1_move, player2_move)

            if result == 0:
                ties += 1
            elif result == 1:
                p1 += 1
            else:
                p2 += 1
            self.player1.train(player2_move, player1_move, result)
            self.player2.train(player1_move, player2_move, result)
            # print('Player1: %s, Player2: %s, %s' % (player1_move, player2_move, r_str))
            print('Player1: %d, Player2: %d, Ties: %d' % (p1, p2, ties))


if __name__ == '__main__':
    game = Game(8000, matching_agent.MatchingAgent(), random_agent.RandomAgent())
    game.start()
