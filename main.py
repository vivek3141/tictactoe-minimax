import sys
from ui import *
from game import TicTacToe


class TicTac(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pb_1.clicked.connect(self.pb)
        """QtCore.QObject.connect(
            self.ui.pb_1, QtCore.SIGNAL('clicked()'), self.pb(1))
        QtCore.QObject.connect(
            self.ui.pb_2, QtCore.SIGNAL('clicked()'), self.pb2)
        QtCore.QObject.connect(
            self.ui.pb_3, QtCore.SIGNAL('clicked()'), self.pb3)
        QtCore.QObject.connect(
            self.ui.pb_4, QtCore.SIGNAL('clicked()'), self.pb4)
        QtCore.QObject.connect(
            self.ui.pb_5, QtCore.SIGNAL('clicked()'), self.pb5)
        QtCore.QObject.connect(
            self.ui.pb_6, QtCore.SIGNAL('clicked()'), self.pb6)
        QtCore.QObject.connect(
            self.ui.pb_7, QtCore.SIGNAL('clicked()'), self.pb7)
        QtCore.QObject.connect(
            self.ui.pb_8, QtCore.SIGNAL('clicked()'), self.pb8)
        QtCore.QObject.connect(
            self.ui.pb_9, QtCore.SIGNAL('clicked()'), self.pb9)"""
        self.board = TicTacToe()

    def pb(self, n):
        print(n)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = TicTac()
    myapp.show()
    sys.exit(app.exec_())
