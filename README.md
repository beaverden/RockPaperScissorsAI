# RockPaperScissorsAI
Some AI techniques for RPS game

### Biased Agent
Returns a specific move depending on a given probability distribution.
Seem to lose to any other type of agent that counts probabilities and can detect the bias

### Markov Agent
Returns the move depending on the probability distribution of sequences of moves.
Sequence length is a parameter for the agent. Obviously, is susceptible to sequences
of bluffs that will shift the probabilities, beats the biased agent

### NN Agent
Returns the move based on a simple HNN with a few layers and inputs given
by the last X observed moves. Beats _Markov Agent_ and _Biased Agent_

### Matching Agent
Find the longest sequence in all the moves made by the adversary that
matches the last X moves. Returns the opposite of the next item in that sequence
If the sequence is not found, it uses a _Markov Agent_ as a proxy for the answer.
Beasts all of the above