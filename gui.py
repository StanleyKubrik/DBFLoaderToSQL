from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from gui_qt import Ui_MainWindow
from os import listdir


class GUI(Ui_MainWindow):
    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        self.setupUi(self.main_window)

        self.lineedit_directory.setPlaceholderText('Double-click for open explorer')
        self.lineedit_directory.selectionChanged.connect(self.browse_directory)

        self.btn_view_files.clicked.connect(self.view_files)

        self.error_select_dir = QMessageBox()
        self.error_select_dir.setWindowTitle('ERROR')
        self.error_select_dir.setText('Select a directory first!')
        self.error_select_dir.setIcon(QMessageBox.Warning)
        self.error_select_dir.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    def browse_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory()
        self.lineedit_directory.setText(directory)

    def view_files(self):
        if self.lineedit_directory is not None:
            print(listdir(self.lineedit_directory.text()))
        else:
            self.error_select_dir.exec_()

    def upload_data(self):
        for file in self.tbl_dbfs.row():
            print(file)
