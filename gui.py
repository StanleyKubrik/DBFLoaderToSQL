from PyQt5 import QtWidgets
from gui_qt import Ui_MainWindow


class GUI(Ui_MainWindow):
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        self.setupUi(self.main_window)

        self.btn_browse.clicked.connect(self.browse_directory)

    def browse_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory()
        self.lineedit_directory.setText(directory)
