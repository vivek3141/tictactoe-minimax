class TicTacToe:
    def __init__(self):
        self.board = [["   ", "   ", "   "] for i in range(3)]
        self.start_game()

    def start_game(self, human=False):
        print(self)
        if human:
            inp = int(input("Make a move: "))
            self.move(inp)

    def move(self, inp, player="X"):
        if self.board[(inp - 1) // 3][(inp - 1) % 3] == "   ":
            self.board[(inp - 1) // 3][(inp - 1) % 3] = " " + player + " "
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

    def _minimax(self):
        pass


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
