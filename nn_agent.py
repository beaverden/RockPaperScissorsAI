import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Activation, Dense
import random
from helpers import opposite

class NNAgent:
    def __init__(self, maxlen=20):
        self.seq_len = maxlen
        self.model = Sequential([
            Dense(150, input_dim=self.seq_len),
            Activation('relu'),
            Dense(50),
            Activation('relu'),
            Dense(3),
            Activation('softmax')
        ])
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        self.last_sequence = deque(maxlen=self.seq_len)
        self.actions = ['r', 'p', 's']
        self.values = {'r': 0, 'p': 1, 's': 2}
        self.last_move = None

    def _transform(self, input):
        return list(map(lambda value: self.values[value], input))# + [self.values[self.last_move]]

    def move(self):
        if len(self.last_sequence) < self.seq_len:
            self.last_move = random.choice(self.actions)
        else:
            _input = self._transform(self.last_sequence)
            _input = np.array(_input).reshape((1, -1))
            probabilities = self.model.predict(_input)[0]
            self.last_move = opposite(self.actions[np.argmax(probabilities)])
        return self.last_move

    def train(self, opponent_move, agent_move, result):
        if len(self.last_sequence) >= self.seq_len:
            _input = self._transform(self.last_sequence)
            _input = np.array(_input).reshape((1, -1))
            output = np.zeros(3)
            output[self.actions.index(opponent_move)] = 1
            output = output.reshape((1, -1))
            self.model.fit(_input, output, verbose=0)
        self.last_sequence.append(opponent_move)
