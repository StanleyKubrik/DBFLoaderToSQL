from gui import GUI
from PyQt5 import QtWidgets
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = GUI()
    ui.main_window.show()
    sys.exit(app.exec_())

