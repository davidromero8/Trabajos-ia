from collections import defaultdict
import pickle

class Q:
    def __init__(self, alpha=0.5, discount=0.5):
        self.alpha = alpha
        self.discount = discount
        self.values = defaultdict(lambda: defaultdict(float))

    def update(self, state, action, next_state, reward):
        old = self.values[state][action]

        if len(self.values[next_state]) > 0:
            next_max = max(self.values[next_state].values())
        else:
            next_max = 0

        new = old + self.alpha * (reward + self.discount * next_max - old)
        self.values[state][action] = new

    def get_best_action(self, state):
        if state not in self.values:
            return None
        if len(self.values[state]) == 0:
            return None
        return max(self.values[state], key=self.values[state].get)

    def save(self):
        with open("qtable.pkl", "wb") as f:
            pickle.dump(dict(self.values), f)

    def load(self):
        try:
            with open("qtable.pkl", "rb") as f:
                data = pickle.load(f)
                self.values = defaultdict(lambda: defaultdict(float), data)
        except:
            pass
