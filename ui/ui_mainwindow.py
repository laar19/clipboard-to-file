# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Wed Nov 17 18:40:24 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(269, 400, 371, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_change_theme = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_change_theme.setObjectName("btn_change_theme")
        self.horizontalLayout.addWidget(self.btn_change_theme)
        self.btn_exit = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 10, 621, 331))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.clipboard_qtextbrowser = QtWidgets.QTextBrowser(self.layoutWidget_2)
        self.clipboard_qtextbrowser.setDocumentTitle("")
        self.clipboard_qtextbrowser.setObjectName("clipboard_qtextbrowser")
        self.verticalLayout.addWidget(self.clipboard_qtextbrowser)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(270, 350, 368, 31))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_clear = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_3.addWidget(self.btn_clear)
        self.btn_save = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_3.addWidget(self.btn_save)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 380, 621, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 660, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAutores = QtWidgets.QAction(MainWindow)
        self.actionAutores.setObjectName("actionAutores")
        self.actionClasificar = QtWidgets.QAction(MainWindow)
        self.actionClasificar.setObjectName("actionClasificar")
        self.actionBuscar = QtWidgets.QAction(MainWindow)
        self.actionBuscar.setObjectName("actionBuscar")
        self.actionLicencia = QtWidgets.QAction(MainWindow)
        self.actionLicencia.setObjectName("actionLicencia")
        self.actionAcerca_de_Qt = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de_Qt.setObjectName("actionAcerca_de_Qt")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionAuthors = QtWidgets.QAction(MainWindow)
        self.actionAuthors.setObjectName("actionAuthors")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuHelp.addAction(self.actionAuthors)
        self.menuHelp.addAction(self.actionLicense)
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Clipboard to file", None, -1))
        self.btn_change_theme.setText(QtWidgets.QApplication.translate("MainWindow", "Change theme", None, -1))
        self.btn_exit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.btn_clear.setText(QtWidgets.QApplication.translate("MainWindow", "Clean", None, -1))
        self.btn_save.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.actionAutores.setText(QtWidgets.QApplication.translate("MainWindow", "Autores", None, -1))
        self.actionClasificar.setText(QtWidgets.QApplication.translate("MainWindow", "Clasificar", None, -1))
        self.actionBuscar.setText(QtWidgets.QApplication.translate("MainWindow", "Buscar", None, -1))
        self.actionLicencia.setText(QtWidgets.QApplication.translate("MainWindow", "Licencia", None, -1))
        self.actionAcerca_de_Qt.setText(QtWidgets.QApplication.translate("MainWindow", "Acerca de Qt", None, -1))
        self.actionAbout_Qt.setText(QtWidgets.QApplication.translate("MainWindow", "About Qt", None, -1))
        self.actionAuthors.setText(QtWidgets.QApplication.translate("MainWindow", "Authors", None, -1))
        self.actionLicense.setText(QtWidgets.QApplication.translate("MainWindow", "License", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
