# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1156, 665)
        self.Main = QtWidgets.QWidget(MainWindow)
        self.Main.setObjectName("Main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_manga = QtWidgets.QWidget(self.Main)
        self.input_manga.setObjectName("input_manga")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.input_manga)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblUrlManga = QtWidgets.QLabel(self.input_manga)
        self.lblUrlManga.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUrlManga.setObjectName("lblUrlManga")
        self.verticalLayout.addWidget(self.lblUrlManga)
        self.leUrl = QtWidgets.QLineEdit(self.input_manga)
        self.leUrl.setObjectName("leUrl")
        self.verticalLayout.addWidget(self.leUrl)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblEnd = QtWidgets.QLabel(self.input_manga)
        self.lblEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEnd.setObjectName("lblEnd")
        self.horizontalLayout_4.addWidget(self.lblEnd)
        self.lblStart = QtWidgets.QLabel(self.input_manga)
        self.lblStart.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStart.setObjectName("lblStart")
        self.horizontalLayout_4.addWidget(self.lblStart)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leStart = QtWidgets.QLineEdit(self.input_manga)
        self.leStart.setObjectName("leStart")
        self.horizontalLayout.addWidget(self.leStart)
        self.leEnd = QtWidgets.QLineEdit(self.input_manga)
        self.leEnd.setObjectName("leEnd")
        self.horizontalLayout.addWidget(self.leEnd)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.input_manga)
        self.widget_3 = QtWidgets.QWidget(self.Main)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblFolder = QtWidgets.QLabel(self.widget_3)
        self.lblFolder.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFolder.setObjectName("lblFolder")
        self.verticalLayout_4.addWidget(self.lblFolder)
        self.leFolder = QtWidgets.QLineEdit(self.widget_3)
        self.leFolder.setObjectName("leFolder")
        self.verticalLayout_4.addWidget(self.leFolder)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnGo = QtWidgets.QPushButton(self.widget_3)
        self.btnGo.setObjectName("btnGo")
        self.horizontalLayout_2.addWidget(self.btnGo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.progressBar = QtWidgets.QProgressBar(self.Main)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.Main)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1156, 26))
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
        self.lblUrlManga.setText(_translate("MainWindow", "Url manga"))
        self.lblEnd.setText(_translate("MainWindow", "start"))
        self.lblStart.setText(_translate("MainWindow", "end"))
        self.lblFolder.setText(_translate("MainWindow", "folder"))
        self.btnGo.setText(_translate("MainWindow", "GO!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

