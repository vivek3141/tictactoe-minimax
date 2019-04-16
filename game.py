from copy import deepcopy


class TicTacToe:
    def __init__(self, other=None):
        self.board = [["   ", "   ", "   "] for i in range(3)]
        self.player = "X"
        self.opponent = "O"
        if other:
            self.__dict__ = deepcopy(other.__dict__)

    def move(self, inp):
        b = TicTacToe(self)
        b.board[inp // 3][inp % 3] = " " + b.player + " "
        (b.player, b.opponent) = (b.opponent, b.player)
        return b

    def tie(self):
        t = True
        for i in self.board:
            for k in i:
                if k == "   ":
                    t = False
        return t

    def check_game(self):
        if self.tie():
            return "TIE!"
        for i in range(3):
            if self.board[i][0] != "   " and \
                    self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return f"{self.board[i][0][1:]}has won!"

            if self.board[0][i] != "   " and \
                    self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return f"{self.board[0][i][1:]}has won!"

        if self.board[0][0] != "   " and \
                self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return f"{self.board[0][0][1:]}has won!"

        if self.board[0][2] != "   " and \
                self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return f"{self.board[0][2][1:]}has won!"

        return False

    def won(self):
        for i in range(3):
            if self.board[i][0] == f" {self.opponent} " and \
                    self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return True

            if self.board[0][i] == f" {self.opponent} " and \
                    self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return True

        if self.board[0][0] == f" {self.opponent} " and \
                self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return True

        if self.board[0][2] == f" {self.opponent} " and \
                self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return True

        return False

    def __str__(self):
        return "".join([x for i in self.board for x in ["".join([z for k in i for z in [k, "|"]][:-1]) +
                                                        "\n", "-----------" + "\n"]][:-1])

    def best(self):
        return self._minimax(True)[1]

    def _minimax(self, player):
        if self.won():
            if player:
                return (-1, None)
            else:
                return (1, None)

        elif self.tie():
            return (0, None)

        elif player:
            best = (-2, None)
            for i in range(9):
                if self.board[i // 3][i % 3] == "   ":
                    value = self.move(i)._minimax(not(player))[0]
                    if value > best[0]:
                        best = (value, i)
            return best

        else:
            best = (2, None)
            for i in range(9):
                if self.board[i // 3][i % 3] == "   ":
                    value = self.move(i)._minimax(not(player))[0]
                    if value < best[0]:
                        best = (value, i)
            return best


if __name__ == "__main__":
    t = TicTacToe()
    print(t)

    while True:
        t = t.move(int(input(":")) - 1)
        m = t.best()
        t = t.move(m)
        print(t)
        # print(t.won())
