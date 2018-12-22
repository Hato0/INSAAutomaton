#  Copyright (C) 2018 Thibaut Lompech - All Rights Reserved
#  You may use, distribute and modify this code under the
#  terms of the legal license, which unfortunately won't be
#  written for another century.
#
#  You should have received a copy of the legal license with
#  this file. If not, please write to: thibaut.lompech@insa-cvl.fr
#
#
#  You should have received a copy of the legal license with
#  this file. If not, please write to: thibaut.lompech@insa-cvl.fr
#

import sys

from PyQt5 import QtGui, QtCore, QtWidgets


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1000, 600)
        self.setWindowTitle("AutoMates project")
        self.setWindowIcon(QtGui.QIcon('Picture/Logo.png'))
        """ Define a file argument """
        extract_action = QtWidgets.QAction("&GET TO THE CHOPPAH!!!", self)
        """ Define a shortcut to leave  """
        extract_action.setShortcut("Ctrl+Q")
        """ Define a description for the file argument """
        extract_action.setStatusTip('Leave The App')
        """ Make the file argument append """
        extract_action.triggered.connect(self.close_application)

        self.statusBar()

        main_menu = self.menuBar()
        """ Create the file drop down menu """
        file_menu = main_menu.addMenu('&File')
        """ Add the previous definition """
        file_menu.addAction(extract_action)
        """ Start the home def """
        self.home()

    def home(self):
        """
        """
        """ Define a button quit """
        btn = QtWidgets.QPushButton("Quit", self)
        """ Define the button action """
        btn.clicked.connect(self.close_application)
        """ Define the button size """
        btn.resize(btn.minimumSizeHint())
        """ Move the button at (x = 0, y = 100) """
        btn.move(0, 100)
        """ Define an icon shortcut with under_text while mouse is on """
        extract_action = QtWidgets.QAction(QtGui.QIcon('todachoppa.png'), 'Flee the Scene', self)
        """ Make the button work """
        extract_action.triggered.connect(self.close_application)
        """ Make the extract_action widget a toolBar which can be move everywhere on the window | Right clic on the top
         able or disable the option"""
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extract_action)
        """ Checkbox to resize the main window """
        check_box = QtWidgets.QCheckBox('Enlarge Window', self)
        check_box.move(100, 25)
        check_box.stateChanged.connect(self.enlarge_window)
        self.show()

    def enlarge_window(self, state):
        """
        Resize Window with Check Box parameters
        :param state: State of CheckBox
        """
        if state == QtCore.Qt.Checked:
            self.showFullScreen()
        else:
            self.setGeometry(50, 50, 1000, 600)

    def close_application(self):
        """
        Define a pop up window used to inform the user above all active window
        """
        choice = QtWidgets.QMessageBox.question(self, 'Extract!', "Get into the chopper?", QtWidgets.QMessageBox.Yes |
                                                QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())


run()