import numpy as np
import random
import markov
import nn_agent
import random_agent
import biased_agent
from helpers import evaluate, opposite


def real_opponent():
    def gen():
        return input().strip()

    return gen


def play():
    # player1 = markov.MarkovAgent()
    # player1 = random_agent.RandomAgent()
    player1 = biased_agent.BiasedAgent()
    player2 = nn_agent.NNAgent()

    for i in range(15):
        player1_move = player1.move()
        player2_move = player2.move()
        print(player1_move, player2_move)
        result = evaluate(player1_move, player2_move)
        player1.train(player2_move, player1_move, result)
        player2.train(player1_move, player2_move, result)

    ties = 0
    p1 = 0
    p2 = 0

    for i in range(8000):
        player1_move = player1.move()
        player2_move = player2.move()
        result = evaluate(player1_move, player2_move)

        r_str = ''
        if result == 0:
            ties += 1
        elif result == 1:
            p1 += 1
        else:
            p2 += 1
        player1.train(player2_move, player1_move, result)
        player2.train(player1_move, player2_move, result)
        # print('Player1: %s, Player2: %s, %s' % (player1_move, player2_move, r_str))
        print('Player1: %d, Player2: %d, Ties: %d' % (p1, p2, ties))


if __name__ == '__main__':
    play()
