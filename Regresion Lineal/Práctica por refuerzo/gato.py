class Gato:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.player = 1

    def get_winner(self):
        for i in range(3):
            if abs(sum(self.board[i])) == 3:
                return self.board[i][0]

        for i in range(3):
            s = self.board[0][i] + self.board[1][i] + self.board[2][i]
            if abs(s) == 3:
                return self.board[0][i]

        return None

    def get_state(self):
        return str(self.board)

    def get_valid_actions(self):
        actions = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    actions.append((i, j))
        return actions

    def is_ended(self):
        if self.get_winner() is not None:
            return True
        return len(self.get_valid_actions()) == 0

    def _print(self):
        for row in self.board:
            print(row)
        print()

    def play(self, x, y):
        if self.board[x][y] != 0:
            return None

        self.board[x][y] = self.player
        winner = self.get_winner()

        if winner is not None:
            return winner

        self.player *= -1
        return None
