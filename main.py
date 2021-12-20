# coding: utf-8

import sys
import qdarkstyle

from qtpy           import QtWidgets
from qtpy.QtWidgets import QApplication, QMainWindow

from qdarkstyle.dark.palette  import DarkPalette
from qdarkstyle.light.palette import LightPalette

from library.functions import *
from ui.ui_mainwindow  import Ui_MainWindow

appname  = "Clipboard to file"

about    = appname + " version 2.0\n\nThis program copy every entry from \
clipboard and\nstore it in a list, then you can save it in a text file"
    
authors  = ["Luis Acevedo", "<laar@pm.me>"]

license_ = "Copyright 2020. All code is copyrighted by the respective authors.\n" \
+ appname + " can be redistributed and/or modified under the terms of \
the GNU GPL versions 3 or by any future license endorsed by " + authors[0] + \
".\nThis program is distributed in the hope that it will be useful, but \
WITHOUT ANY WARRANTY; without even the implied warranty of \
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE."

clipboard_list = list()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        # Save
        self.btn_save.clicked.connect(self.save_as)
        self.btn_save.setStyleSheet(
            "QPushButton { background-color: green; } \
                QPushButton::hover { \
                background-color: grey; \
            }"
        )

        # Clear list button
        self.btn_clear.clicked.connect(self.clear)

        # About
        self.actionAbout.triggered.connect(self.about_)

        # About Qt
        self.actionAbout_Qt.triggered.connect(self.aboutQt)

        # Authors
        self.actionAuthors.triggered.connect(self.authors)

        # License
        self.actionLicense.triggered.connect(self.license_)

        # Change theme
        self.btn_change_theme.setStyleSheet(
            "QPushButton { background-color: purple; } \
                QPushButton::hover { \
                background-color: grey; \
            }"
        )
        self.btn_change_theme.setCheckable(True)
        #self.btn_change_theme.setChecked(True)
        self.btn_change_theme.clicked.connect(self.toggle_theme)

        # Exit
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

    def about_(self):
        QtWidgets.QMessageBox.about(self, "About", about)

    def aboutQt(self):
        QtWidgets.QMessageBox.aboutQt(self)
    
    def authors(self):
        text = authors[0] + " " + authors[1]
        QtWidgets.QMessageBox.about(self, "authors", text)
        
    def license_(self):
        QtWidgets.QMessageBox.about(self, "license_", license_)
        
    def toggle_theme(self):
        if not self.btn_change_theme.isChecked():
            app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside2", palette=DarkPalette))
        else:
            app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside2", palette=LightPalette))

    def exit(self):
        sys.exit()

if __name__ == "__main__":
    
    print("\n" + appname + " Copyright (C) 2020 " + authors[0] + ".\nEste programa viene con ABSOLUTAMENTE NINGUNA GARANTÍA.\nEsto es software libre, y le invitamos a redistribuirlo\nbajo ciertas condiciones.\nPor favor, leer el archivo README.")

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside2", palette=DarkPalette))

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
