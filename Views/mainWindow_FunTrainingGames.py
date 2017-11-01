# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/mainWindow_FunTrainingGames.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_mainWindow = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_mainWindow.setGeometry(QtCore.QRect(-20, 0, 791, 571))
        self.scrollArea_mainWindow.setWidgetResizable(True)
        self.scrollArea_mainWindow.setObjectName("scrollArea_mainWindow")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 789, 569))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.treeWidget_FullGameHistory = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.treeWidget_FullGameHistory.setGeometry(QtCore.QRect(510, 40, 256, 192))
        self.treeWidget_FullGameHistory.setObjectName("treeWidget_FullGameHistory")
        self.pushButton_NewGame = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_NewGame.setGeometry(QtCore.QRect(150, 210, 101, 23))
        self.pushButton_NewGame.setObjectName("pushButton_NewGame")
        self.label_CurrentLevel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_CurrentLevel.setGeometry(QtCore.QRect(80, 70, 71, 20))
        self.label_CurrentLevel.setObjectName("label_CurrentLevel")
        self.label_FullGameHistory = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_FullGameHistory.setGeometry(QtCore.QRect(570, 20, 91, 20))
        self.label_FullGameHistory.setObjectName("label_FullGameHistory")
        self.spinBox_CurrentLevel = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_CurrentLevel.setGeometry(QtCore.QRect(170, 70, 42, 22))
        self.spinBox_CurrentLevel.setObjectName("spinBox_CurrentLevel")
        self.treeWidget_Last10Games = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.treeWidget_Last10Games.setGeometry(QtCore.QRect(510, 270, 256, 192))
        self.treeWidget_Last10Games.setObjectName("treeWidget_Last10Games")
        self.label_Last10Games = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Last10Games.setGeometry(QtCore.QRect(580, 240, 91, 20))
        self.label_Last10Games.setObjectName("label_Last10Games")
        self.comboBox_Game = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_Game.setGeometry(QtCore.QRect(170, 30, 69, 22))
        self.comboBox_Game.setObjectName("comboBox_Game")
        self.label_Game = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Game.setGeometry(QtCore.QRect(110, 30, 31, 20))
        self.label_Game.setObjectName("label_Game")
        self.spinBox_W = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_W.setGeometry(QtCore.QRect(170, 140, 42, 22))
        self.spinBox_W.setObjectName("spinBox_W")
        self.spinBox_L = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_L.setGeometry(QtCore.QRect(240, 140, 42, 22))
        self.spinBox_L.setObjectName("spinBox_L")
        self.label_Record = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Record.setGeometry(QtCore.QRect(100, 140, 41, 20))
        self.label_Record.setObjectName("label_Record")
        self.label_W = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_W.setGeometry(QtCore.QRect(150, 140, 16, 16))
        self.label_W.setObjectName("label_W")
        self.label_L = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_L.setGeometry(QtCore.QRect(220, 140, 16, 16))
        self.label_L.setObjectName("label_L")
        self.pushButton_SeasonSettings = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_SeasonSettings.setGeometry(QtCore.QRect(150, 260, 101, 23))
        self.pushButton_SeasonSettings.setObjectName("pushButton_SeasonSettings")
        self.scrollArea_mainWindow.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget_FullGameHistory.headerItem().setText(0, _translate("MainWindow", "User ID"))
        self.treeWidget_FullGameHistory.headerItem().setText(1, _translate("MainWindow", "User Name"))
        self.treeWidget_FullGameHistory.headerItem().setText(2, _translate("MainWindow", "Game"))
        self.treeWidget_FullGameHistory.headerItem().setText(3, _translate("MainWindow", "Level"))
        self.treeWidget_FullGameHistory.headerItem().setText(4, _translate("MainWindow", "Result"))
        self.treeWidget_FullGameHistory.headerItem().setText(5, _translate("MainWindow", "Target"))
        self.treeWidget_FullGameHistory.headerItem().setText(6, _translate("MainWindow", "Attempts"))
        self.treeWidget_FullGameHistory.headerItem().setText(7, _translate("MainWindow", "Successful"))
        self.treeWidget_FullGameHistory.headerItem().setText(8, _translate("MainWindow", "%"))
        self.treeWidget_FullGameHistory.headerItem().setText(9, _translate("MainWindow", "Clutch Attempts"))
        self.treeWidget_FullGameHistory.headerItem().setText(10, _translate("MainWindow", "Clutch Successful"))
        self.treeWidget_FullGameHistory.headerItem().setText(11, _translate("MainWindow", "Clutch %"))
        self.treeWidget_FullGameHistory.headerItem().setText(12, _translate("MainWindow", "1"))
        self.treeWidget_FullGameHistory.headerItem().setText(13, _translate("MainWindow", "2"))
        self.treeWidget_FullGameHistory.headerItem().setText(14, _translate("MainWindow", "3"))
        self.treeWidget_FullGameHistory.headerItem().setText(15, _translate("MainWindow", "4"))
        self.treeWidget_FullGameHistory.headerItem().setText(16, _translate("MainWindow", "5"))
        self.treeWidget_FullGameHistory.headerItem().setText(17, _translate("MainWindow", "6"))
        self.treeWidget_FullGameHistory.headerItem().setText(18, _translate("MainWindow", "7"))
        self.treeWidget_FullGameHistory.headerItem().setText(19, _translate("MainWindow", "8"))
        self.treeWidget_FullGameHistory.headerItem().setText(20, _translate("MainWindow", "9"))
        self.treeWidget_FullGameHistory.headerItem().setText(21, _translate("MainWindow", "10"))
        self.treeWidget_FullGameHistory.headerItem().setText(22, _translate("MainWindow", "11"))
        self.pushButton_NewGame.setText(_translate("MainWindow", "New Game"))
        self.label_CurrentLevel.setText(_translate("MainWindow", "Current Level:"))
        self.label_FullGameHistory.setText(_translate("MainWindow", "Full Game History"))
        self.treeWidget_Last10Games.headerItem().setText(0, _translate("MainWindow", "User ID"))
        self.treeWidget_Last10Games.headerItem().setText(1, _translate("MainWindow", "User Name"))
        self.treeWidget_Last10Games.headerItem().setText(2, _translate("MainWindow", "Game"))
        self.treeWidget_Last10Games.headerItem().setText(3, _translate("MainWindow", "Level"))
        self.treeWidget_Last10Games.headerItem().setText(4, _translate("MainWindow", "Result"))
        self.treeWidget_Last10Games.headerItem().setText(5, _translate("MainWindow", "Target"))
        self.treeWidget_Last10Games.headerItem().setText(6, _translate("MainWindow", "Attempts"))
        self.treeWidget_Last10Games.headerItem().setText(7, _translate("MainWindow", "Successful"))
        self.treeWidget_Last10Games.headerItem().setText(8, _translate("MainWindow", "%"))
        self.treeWidget_Last10Games.headerItem().setText(9, _translate("MainWindow", "Clutch Attempts"))
        self.treeWidget_Last10Games.headerItem().setText(10, _translate("MainWindow", "Clutch Successful"))
        self.treeWidget_Last10Games.headerItem().setText(11, _translate("MainWindow", "Clutch %"))
        self.treeWidget_Last10Games.headerItem().setText(12, _translate("MainWindow", "1"))
        self.treeWidget_Last10Games.headerItem().setText(13, _translate("MainWindow", "2"))
        self.treeWidget_Last10Games.headerItem().setText(14, _translate("MainWindow", "3"))
        self.treeWidget_Last10Games.headerItem().setText(15, _translate("MainWindow", "4"))
        self.treeWidget_Last10Games.headerItem().setText(16, _translate("MainWindow", "5"))
        self.treeWidget_Last10Games.headerItem().setText(17, _translate("MainWindow", "6"))
        self.treeWidget_Last10Games.headerItem().setText(18, _translate("MainWindow", "7"))
        self.treeWidget_Last10Games.headerItem().setText(19, _translate("MainWindow", "8"))
        self.treeWidget_Last10Games.headerItem().setText(20, _translate("MainWindow", "9"))
        self.treeWidget_Last10Games.headerItem().setText(21, _translate("MainWindow", "10"))
        self.treeWidget_Last10Games.headerItem().setText(22, _translate("MainWindow", "11"))
        self.label_Last10Games.setText(_translate("MainWindow", "Last 10 Games"))
        self.label_Game.setText(_translate("MainWindow", "Game:"))
        self.label_Record.setText(_translate("MainWindow", "Record:"))
        self.label_W.setText(_translate("MainWindow", "W"))
        self.label_L.setText(_translate("MainWindow", "L"))
        self.pushButton_SeasonSettings.setText(_translate("MainWindow", "Season Settings"))

