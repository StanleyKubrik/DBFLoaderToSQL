from gui import GUI
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = GUI()
    ui.main_window.show()
    sys.exit(app.exec_())
