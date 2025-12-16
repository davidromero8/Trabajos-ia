from gato import Gato
from agent import Agent
import random

game = Gato()
agent = Agent()

while not game.is_ended():
    game._print()

    if game.player == 1:
        x = int(input("Fila (0-2): "))
        y = int(input("Columna (0-2): "))
        game.play(x, y)
    else:
        state = game.get_state()
        action = agent.get_action(state, game.get_valid_actions())
        game.play(action[0], action[1])

        reward = 0
        winner = game.get_winner()

        if winner == -1:
            reward = 100
        elif winner == 1:
            reward = -100

        agent.learn_game(state, action, game.get_state(), reward)
        agent.learn()
        agent.q.save()

game._print()

w = game.get_winner()
if w == 1:
    print("Gana el jugador")
elif w == -1:
    print("Gana la IA")
else:
    print("Empate")
