class TicTacToe:
    def __init__(self):
        self.board = [["   ", "   ", "   "] for i in range(3)]
        self.start_game()

    def start_game(self, human=True):
        print(self)
        if human:
            inp = int(input("Make a move: "))
            self.move(inp)

    def move(self, inp, player="X"):
        self.board[(inp - 1) // 3][(inp - 1) % 3] = " " + player + " "
        self.check_game()

    def check_game(self):
        print(self)
        pass

    def __str__(self):
        return "".join([x for i in self.board for x in ["".join([z for k in i for z in [k, "|"]][:-1]) +
                                                        "\n", "-----------" + "\n"]][:-1])


if __name__ == "__main__":
    t = TicTacToe()
