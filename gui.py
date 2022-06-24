from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from PyQt5.QtCore import Qt
from gui_qt import Ui_MainWindow
from os import listdir
from sql import SQL


class GUI(Ui_MainWindow):
    def __init__(self):
        self.main_window = QMainWindow()
        self.setupUi(self.main_window)

        # Make it possible to select a directory by double-clicking on the field.
        self.lineedit_directory.setPlaceholderText('Double-click for open explorer')
        self.lineedit_directory.selectionChanged.connect(self.browse_directory)

        self.btn_view_files.clicked.connect(self.view_files)

        self.btn_upload.clicked.connect(self.upload_data)

        # Init SQL-object for connect to DB.
        self.sql = SQL()

    def browse_directory(self):
        """
        Open explorer to select a directory.
        """

        directory = QFileDialog.getExistingDirectory()
        self.lineedit_directory.setText(directory)

    def view_files(self):
        """
        Fills the table with DBFs for further selection and upload.
        """
        try:
            directory = self.lineedit_directory.text()
            dbf_file_list = [f for f in listdir(directory) if f.lower().endswith('.dbf')]
            # test_list = ['test1', 'test2', 'test3', 'test4', 'test5']
            # row = 0
            # for i in test_list:
            #     self.tbl_dbfs.setItem(row, 0, QTableWidgetItem(f'{i}'))
            #     row += 1
            self.tbl_dbfs.setRowCount(len(dbf_file_list))
            row = 0
            while row < len(dbf_file_list):
                item = QTableWidgetItem()
                item.setText(f'{dbf_file_list[row]}')
                item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                item.setCheckState(Qt.CheckState.Unchecked)
                self.tbl_dbfs.setItem(row, 0, item)
                row += 1
        except WindowsError:
            self.warning_msg('ERROR', 'Select a directory first!')

    def upload_data(self):
        """
        Uploads selected DBFs into SQL.
        """
        pass

    def warning_msg(self, title, message):
        """
        Shows a warning message.
        :param title: Title of the message box.
        :param message: The main text of the message box.
        """
        QMessageBox.warning(self.main_window, title, message)
