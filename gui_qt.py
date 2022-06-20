# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(1, 0, 701, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.btn_upload = QtWidgets.QPushButton(self.tab_main)
        self.btn_upload.setGeometry(QtCore.QRect(0, 245, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_upload.setFont(font)
        self.btn_upload.setObjectName("btn_upload")
        self.txt_console = QtWidgets.QTextEdit(self.tab_main)
        self.txt_console.setGeometry(QtCore.QRect(0, 275, 691, 200))
        self.txt_console.setObjectName("txt_console")
        self.btn_close = QtWidgets.QPushButton(self.tab_main)
        self.btn_close.setGeometry(QtCore.QRect(615, 480, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_close.setFont(font)
        self.btn_close.setObjectName("btn_close")
        self.tbl_dbfs = QtWidgets.QTableWidget(self.tab_main)
        self.tbl_dbfs.setGeometry(QtCore.QRect(0, 39, 691, 201))
        self.tbl_dbfs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tbl_dbfs.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tbl_dbfs.setGridStyle(QtCore.Qt.SolidLine)
        self.tbl_dbfs.setRowCount(0)
        self.tbl_dbfs.setColumnCount(4)
        self.tbl_dbfs.setObjectName("tbl_dbfs")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tbl_dbfs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dbfs.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dbfs.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dbfs.setHorizontalHeaderItem(3, item)
        self.tbl_dbfs.horizontalHeader().setVisible(True)
        self.tbl_dbfs.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_dbfs.horizontalHeader().setDefaultSectionSize(100)
        self.tbl_dbfs.horizontalHeader().setSortIndicatorShown(True)
        self.tbl_dbfs.horizontalHeader().setStretchLastSection(True)
        self.tbl_dbfs.verticalHeader().setVisible(False)
        self.tbl_dbfs.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_dbfs.verticalHeader().setSortIndicatorShown(False)
        self.layoutWidget = QtWidgets.QWidget(self.tab_main)
        self.layoutWidget.setGeometry(QtCore.QRect(0, -1, 691, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_choose = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_choose.setFont(font)
        self.lbl_choose.setObjectName("lbl_choose")
        self.horizontalLayout.addWidget(self.lbl_choose)
        self.lineedit_directory = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineedit_directory.setObjectName("lineedit_directory")
        self.horizontalLayout.addWidget(self.lineedit_directory)
        self.btn_browse = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_browse.setFont(font)
        self.btn_browse.setObjectName("btn_browse")
        self.horizontalLayout.addWidget(self.btn_browse)
        self.tabWidget.addTab(self.tab_main, "")
        self.tab_config = QtWidgets.QWidget()
        self.tab_config.setObjectName("tab_config")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_config)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 511))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.config_column1 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.config_column1.setContentsMargins(5, 5, 0, 0)
        self.config_column1.setObjectName("config_column1")
        self.lbl_server = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_server.setObjectName("lbl_server")
        self.config_column1.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_server)
        self.lineedit_server = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineedit_server.setObjectName("lineedit_server")
        self.config_column1.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineedit_server)
        self.lbl_database = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_database.setObjectName("lbl_database")
        self.config_column1.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_database)
        self.lineedit_database = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineedit_database.setObjectName("lineedit_database")
        self.config_column1.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineedit_database)
        self.lbl_username = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_username.setObjectName("lbl_username")
        self.config_column1.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_username)
        self.lineedit_username = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineedit_username.setObjectName("lineedit_username")
        self.config_column1.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineedit_username)
        self.lbl_password = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_password.setObjectName("lbl_password")
        self.config_column1.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_password)
        self.lineedit_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineedit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineedit_password.setObjectName("lineedit_password")
        self.config_column1.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineedit_password)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_config)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(360, 0, 91, 511))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.config_column2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.config_column2.setContentsMargins(5, 5, 0, 0)
        self.config_column2.setObjectName("config_column2")
        self.lb_port = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lb_port.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_port.setObjectName("lb_port")
        self.config_column2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_port)
        self.lineedit_port = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineedit_port.setEnabled(True)
        self.lineedit_port.setObjectName("lineedit_port")
        self.config_column2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineedit_port)
        self.tabWidget.addTab(self.tab_config, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.btn_close.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DBF Loader To SQL v1.0"))
        self.btn_upload.setText(_translate("MainWindow", "Upload"))
        self.btn_close.setText(_translate("MainWindow", "Close"))
        self.tbl_dbfs.setSortingEnabled(True)
        item = self.tbl_dbfs.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Filename"))
        item = self.tbl_dbfs.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Update Date"))
        item = self.tbl_dbfs.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "File Size"))
        item = self.tbl_dbfs.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SQL Table Name"))
        self.lbl_choose.setText(_translate("MainWindow", "Choose directory with DBF files:"))
        self.btn_browse.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("MainWindow", "Main"))
        self.lbl_server.setText(_translate("MainWindow", "SQL server"))
        self.lbl_database.setText(_translate("MainWindow", "Database"))
        self.lbl_username.setText(_translate("MainWindow", "Username"))
        self.lbl_password.setText(_translate("MainWindow", "Password"))
        self.lb_port.setText(_translate("MainWindow", "Port"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), _translate("MainWindow", "Configuration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())