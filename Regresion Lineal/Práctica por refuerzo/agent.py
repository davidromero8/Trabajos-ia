import random
from qlearning import Q

class Agent:
    def __init__(self):
        self.eps = 1.0
        self.q = Q()
        self.q.load()

    def get_action(self, state, valid_actions):
        if random.random() < self.eps:
            return random.choice(valid_actions)

        best = self.q.get_best_action(state)
        if best is None:
            return random.choice(valid_actions)

        if best not in valid_actions:
            return random.choice(valid_actions)

        return best

    def learn(self):
        if self.eps > 0.1:
            self.eps *= 0.99

    def learn_game(self, state, action, next_state, reward):
        self.q.update(state, action, next_state, reward)
