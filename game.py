from copy import deepcopy


class TicTacToe:
    def __init__(self, other=None):
        self.board = [["   ", "   ", "   "] for i in range(3)]
        self.start_game()
        self.player = "X"
        self.opponent = "O"
        if other:
            self.__dict__ = deepcopy(other.__dict__)

    def start_game(self, human=False):
        print(self)
        if human:
            inp = int(input("Make a move: "))
            self.move(inp)

    def _move(self, inp):
        b = TicTacToe(self)
        b.board[(inp - 1) // 3][(inp - 1) % 3] = " " + self.player + " "
        (self.player, self.opponent) = (self.opponent, self.player)
        return b

    def move(self, inp):
        if self.board[(inp - 1) // 3][(inp - 1) % 3] == "   ":
            self.board[(inp - 1) // 3][(inp - 1) % 3] = " " + self.player + " "
        else:
            return None
        return self.check_game()

    def tie(self):
        t = True
        for i in self.board:
            for k in i:
                if k == "   ":
                    t = False
        return t

    def won(self):
        for i in range(3):
            if self.board[i][0] == f" {self.player} " and \
                    self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                print(f"{self.board[i][0][1:]}has won!")
                return True

            if self.board[0][i] == f" {self.player} " and \
                    self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                print(f"{self.board[0][i][1:]}has won!")
                return True

        if self.board[0][0] == f" {self.player} " and \
                self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            print(f"{self.board[0][0][1:]}has won!")
            return True

        if self.board[0][2] == f" {self.player} " and \
                self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            print(f"{self.board[0][2][1:]}has won!")
            return True

        return False

    def check_game(self):
        t = False
        for i in self.board:
            for k in i:
                if k == "   ":
                    t = True
        if not t:
            print("TIE")
            return True
        for i in range(3):
            if self.board[i][0] != "   " and \
                    self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                print(f"{self.board[i][0][1:]}has won!")
                return True

            if self.board[0][i] != "   " and \
                    self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                print(f"{self.board[0][i][1:]}has won!")
                return True

        if self.board[0][0] != "   " and \
                self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            print(f"{self.board[0][0][1:]}has won!")
            return True

        if self.board[0][2] != "   " and \
                self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            print(f"{self.board[0][2][1:]}has won!")
            return True

        return False

    def __str__(self):
        return "".join([x for i in self.board for x in ["".join([z for k in i for z in [k, "|"]][:-1]) +
                                                        "\n", "-----------" + "\n"]][:-1])

    def _minimax(self, player):
        if self.won():
            if player:
                return (-1, None)
            else:
                return (+1, None)
        elif self.tied():
            return (0, None)
        elif player:
            best = (-2, None)
            for i in range(9):
                if self.board[i // 3][i % 3] == "   ":
                    value = self.move(i).__minimax(not player)[0]
                    if value > best[0]:
                        best = (value, i)
            return best
        else:
            best = (+2, None)
            for i in range(9):
                if self.board[i // 3][i % 3] == "   ":
                    value = self.move(i).__minimax(not player)[0]
                    if value < best[0]:
                        best = (value, i)
            return best


if __name__ == "__main__":
    t = TicTacToe()

    while True:
        done = t.move(int(input(":")), "X")
        print(t)
        if done:
            break

        done = t.move(int(input(":")), "O")
        print(t)
        if done:
            break
