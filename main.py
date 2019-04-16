import sys
from ui import *
from game import TicTacToe


class TicTac(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.btns = [
            self.ui.pb_1,
            self.ui.pb_2,
            self.ui.pb_3,
            self.ui.pb_4,
            self.ui.pb_5,
            self.ui.pb_6,
            self.ui.pb_7,
            self.ui.pb_8,
            self.ui.pb_9,
        ]
        self.btns[0].clicked.connect(lambda: self.pb(0))
        #for n in range(9):
        #    self.btns[n].clicked.connect(lambda: self.pb(n))
        self.tic = TicTacToe()

    def pb(self, n):
        print(f"HELLO {n}")
        self.tic.move(n)
        self.update()

    def update(self):
        for i in range(9):
            self.btns[i].setText(self.tic.board[i // 3][i % 3].strip())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = TicTac()
    myapp.show()
    sys.exit(app.exec_())
