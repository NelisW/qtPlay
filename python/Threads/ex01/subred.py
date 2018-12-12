# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subred.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.subreddits_input_layout = QtWidgets.QHBoxLayout()
        self.subreddits_input_layout.setObjectName("subreddits_input_layout")
        self.label_subreddits = QtWidgets.QLabel(self.centralwidget)
        self.label_subreddits.setObjectName("label_subreddits")
        self.subreddits_input_layout.addWidget(self.label_subreddits)
        self.edit_subreddits = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_subreddits.setObjectName("edit_subreddits")
        self.subreddits_input_layout.addWidget(self.edit_subreddits)
        self.verticalLayout.addLayout(self.subreddits_input_layout)
        self.label_submissions_list = QtWidgets.QLabel(self.centralwidget)
        self.label_submissions_list.setObjectName("label_submissions_list")
        self.verticalLayout.addWidget(self.label_submissions_list)
        self.list_submissions = QtWidgets.QListWidget(self.centralwidget)
        self.list_submissions.setObjectName("list_submissions")
        self.verticalLayout.addWidget(self.list_submissions)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout.addWidget(self.btn_start)
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setEnabled(False)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout.addWidget(self.btn_stop)
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Threading Tutorial"))
        self.label_subreddits.setText(_translate("MainWindow", "Subreddits:"))
        self.edit_subreddits.setPlaceholderText(_translate("MainWindow", "python,programming,linux,etc (comma separated,no spaces)"))
        self.label_submissions_list.setText(_translate("MainWindow", "Submissions:"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))

