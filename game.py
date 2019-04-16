class TicTacToe:
    def __init__(self):
        self.board = [["", "", ""] for i in range(3)]
        self.start_game()

    def start_game():
        for i in self.board:
            print(*i, end="|")


if __name__ == "__main__":
    t = TicTacToe()
