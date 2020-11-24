# coding: utf-8

import sys

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QFile, QObject
from PySide2.QtUiTools import QUiLoader

# Using PyQt5
#from PyQt5 import uic, QtWidgets
#from PyQt5.Qt import QApplication

from functions.functions import *

appname  = "Clipboard to file"
authors  = ["Luis Acevedo", "<laar@protonmail.com>"]
license_ = "Copyright 2020. All code is copyrighted by the respective authors.\n" + appname + " can be redistributed and/or modified under the terms of the GNU GPL versions 3 or by any future license endorsed by " + authors[0] +"." + "\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE."

# Spcify user interface location
if (len(sys.argv) < 2):
    ui_file = "ui/window.ui"        # Default
elif (len(sys.argv) == 2):
    ui_file = sys.argv[1]           # Custom, in order to make and exeutable with pyinstaller
else:
    print("Argumento/s inválido/s") # Any other option, error
    sys.exit()

clipboard_list = list()

#class MyApp(QtWidgets.QMainWindow): # Using PyQt5
class MyApp(QDialog):
    #def __init__(self): # Using PyQt5
    def __init__(self, ui_file):
        super().__init__()
        self.ui_file = QFile(ui_file)
        self.ui_file.open(QFile.ReadOnly)
        
        # Using PyQty5
        #super(MyApp, self).__init__()
        #uic.loadUi(ui_file, self)
        #self.show()

        self.loader = QUiLoader()
        self.window = self.loader.load(self.ui_file)
        self.window.show()

        #self.clipboard_qtextbrowser = self.findChild(QtWidgets.QTextBrowser, "clipboard_qtextbrowser") # Show selected files from clipboard
        self.clipboard_qtextbrowser = self.window.findChild(QtWidgets.QTextBrowser, "clipboard_qtextbrowser") # Show selected files from clipboard

        self.btn_save = self.window.findChild(QtWidgets.QPushButton, "btn_save")       # Save
        self.btn_save.clicked.connect(self.save_as)

        self.btn_clear = self.window.findChild(QtWidgets.QPushButton, "btn_clear")     # Clear list button
        self.btn_clear.clicked.connect(self.clear)

        self.btn_about = self.window.findChild(QtWidgets.QPushButton, "btn_about")     # About Qt
        self.btn_about.clicked.connect(self.aboutQt)

        self.btn_authors = self.window.findChild(QtWidgets.QPushButton, "btn_authors") # Authors
        self.btn_authors.clicked.connect(self.authors)

        self.btn_license = self.window.findChild(QtWidgets.QPushButton, "btn_license") # License
        self.btn_license.clicked.connect(self.license_)

        self.btn_exit = self.window.findChild(QtWidgets.QPushButton, "btn_exit")       # Exit
        self.btn_exit.clicked.connect(self.exit)

        QApplication.clipboard().dataChanged.connect(self.listen_clipboard)

    # Listen clipboard and update window
    def listen_clipboard(self):
        if (list_append(clipboard_list, QApplication.clipboard().text()) == 0):
            self.clipboard_qtextbrowser.setText(list_to_string(clipboard_list))
        #print(clipboard_list)

    def save_as(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self, "Save File")
        create_text_file(clipboard_list, file_name[0])

    # Clear clipboard list
    def clear(self):
        self.clipboard_qtextbrowser.setText("")
        clipboard_list.clear()

    def aboutQt(self):
        QtWidgets.QMessageBox.aboutQt(self)
    
    def authors(self):
        mensaje = authors[0] + " " + authors[1]
        QtWidgets.QMessageBox.about(self, "authors", mensaje)
        
    def license_(self):
        QtWidgets.QMessageBox.about(self, "license_", license_)

    def exit(self):
        sys.exit()

if __name__ == "__main__":    
    print(appname + " Copyright (C) 2020 " + authors[0] +".\nEste programa viene con ABSOLUTAMENTE NINGUNA GARANTÍA.\nEsto es software libre, y le invitamos a redistribuirlo\nbajo ciertas condiciones.\nPor favor, leer el archivo README.")

    app = QApplication(sys.argv)
    w = MyApp(ui_file)
    sys.exit(app.exec_())

    # Using PyQt5
    #app = QtWidgets.QApplication(sys.argv)
    #window = MyApp()
    #app.exec_()
