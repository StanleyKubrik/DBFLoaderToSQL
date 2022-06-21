from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from PyQt5.QtCore import Qt
from gui_qt import Ui_MainWindow
from os import listdir


class GUI(Ui_MainWindow):
    def __init__(self):
        self.main_window = QMainWindow()
        self.setupUi(self.main_window)

        self.lineedit_directory.setPlaceholderText('Double-click for open explorer')
        self.lineedit_directory.selectionChanged.connect(self.browse_directory)

        self.btn_view_files.clicked.connect(self.view_files)

        for row in range(self.tbl_dbfs.rowCount() + 1):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.tbl_dbfs.setItem(row, 0, item)

        self.btn_upload.clicked.connect(self.upload_data)

    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory()
        self.lineedit_directory.setText(directory)

    def view_files(self):
        try:
            dbf_file_list = [f for f in listdir(self.lineedit_directory.text()) if f.endswith('.DBF')]
            # for file in dbf_file_list:
            #     for row in range(len(dbf_file_list) + 1):
            #         item = QTableWidgetItem()
            #         item.setText(f'{file}')
            #         self.tbl_dbfs.setItem(row, 0, item)
        except WindowsError:
            self.warning_msg('ERROR', 'Select a directory first!')

    def upload_data(self):
        pass

    def warning_msg(self, title, message):
        QMessageBox.warning(self.main_window, title, message)
