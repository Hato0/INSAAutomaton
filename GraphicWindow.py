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


import os.path
import sys

from PyQt5 import QtGui, QtCore, QtWidgets

from FileClass import FilesBlock;


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        files = FilesBlock()
        self.setGeometry(50, 50, 1000, 600)
        self.setWindowTitle("AutoMates project")
        self.setWindowIcon(QtGui.QIcon('Picture/Logo.png'))
        """ Create new widget and associate it to new_application"""
        """ Define a file argument """
        new_action = QtWidgets.QAction("&New", self)
        """ Define a shortcut to extract_action  """
        new_action.setShortcut("Ctrl+N")
        """ Define a description for the file argument """
        new_action.setStatusTip('Create a new empty graph')
        """ Make the file argument append """
        new_action.triggered.connect(self.new_application)
        """ Create open widget and assoiate it to import_application """
        open_action = QtWidgets.QAction("&Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.setStatusTip('Open a saved file')
        open_action.triggered.connect(self.import_application)
        """ Create export widget and associate it to export_application """
        export_action = QtWidgets.QAction("&Export", self)
        export_action.setShortcut("Ctrl+E")
        export_action.setStatusTip('Export to Latex/Tikz')
        export_action.triggered.connect(self.export_application)
        """ Create save widget and associate it to save_application"""
        save_action = QtWidgets.QAction("&Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.setStatusTip('Save the current file')
        save_action.triggered.connect(self.save_application)
        """ Create leave widget and associate it to close_application """
        leave_action = QtWidgets.QAction("&Quit", self)
        leave_action.setShortcut("Ctrl+Q")
        leave_action.setStatusTip('Quit the application')
        leave_action.triggered.connect(self.close_application)

        self.statusBar()

        main_menu = self.menuBar()
        """ Create the file drop down menu """
        file_menu = main_menu.addMenu('&File')
        """ Add file parameters """
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(export_action)
        file_menu.addAction(leave_action)
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
        choice = QtWidgets.QMessageBox.question(self, 'Quit application check_box', "Do you really want to quit \n "
                                                                                    "Press No if you haven't save "
                                                                                    "your work",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def new_application(self):
        pass

    def import_application(self):
        file = FilesBlock()
        list_file = []
        text, ok_pressed = QtWidgets.QInputDialog.getText(self, "Get File Name to import", "File Name or Path:",
                                                          QtWidgets.QLineEdit.Normal, "")
        list_file.append(text)
        if ok_pressed and text != '':
            if not os.path.isfile(text):
                while list_file[-1] != "Quit":
                    text, ok_pressed = QtWidgets.QInputDialog.getText(self, "Get File Name to import",
                                                                      "File not found, try an "
                                                                      "other name or path: \n Or enter Quit to close "
                                                                      "this window",
                                                                      QtWidgets.QLineEdit.Normal, "")
                    list_file.append(text)
                    if os.path.isfile(list_file[-1]):
                        break
            if list_file[-1] == "Quit":
                pass
            else:
                file.set_name(list_file[-2])
                FilesBlock.importation(file)

    def export_application(self):
        file = FilesBlock()
        list_file = []
        text, ok_pressed = QtWidgets.QInputDialog.getText(self, "Get File Name to import", "File Name or Path:",
                                                          QtWidgets.QLineEdit.Normal, "")
        list_file.append(text)
        if ok_pressed and text != '':
            if os.path.isfile(text):
                while list_file[-1] != "OverWrite":
                    text, ok_pressed = QtWidgets.QInputDialog.getText(self, "Get File Name to export",
                                                                      "File already exist please enter a new file or "
                                                                      "type 'OverWrite' to continue \n "
                                                                      "Type Quit to leave"
                                                                      , QtWidgets.QLineEdit.Normal, "")
                    list_file.append(text)
                    if not os.path.isfile(list_file[-1]):
                        break
            if list_file[-1] == "Quit":
                pass
            elif list_file[-1] == "OverWrite":
                file.set_name(list_file[-2])
                FilesBlock.export(file)
            else:
                file.set_name(list_file[-1])
                FilesBlock.export(file)

    def save_application(self):
        file = FilesBlock()
        list_file = []
        text, ok_pressed = QtWidgets.QInputDialog.getText(self, "Get File Name to save", "File Name or Path:",
                                                          QtWidgets.QLineEdit.Normal, "")
        list_file.append(text)
        if ok_pressed and text != '':
            if os.path.isfile(text):
                while list_file[-1] != "OverWrite":
                    text, ok_pressed = QtWidgets.QInputDialog.getText(self, "Get File Name to save",
                                                                      "File already exist please enter a new file or "
                                                                      "type 'OverWrite' to continue \n "
                                                                      "Type Quit to leave"
                                                                      , QtWidgets.QLineEdit.Normal, "")
                    list_file.append(text)
                    if not os.path.isfile(list_file[-1]):
                        break

            if list_file[-1] == "Quit":
                pass
            elif list_file[-1] == "OverWrite":
                file.set_name(list_file[-2])
                header, ok_pressed = QtWidgets.QInputDialog.getText(self, "Get header ", "Enter a header for "
                                                                                         "the save file(optional)",
                                                                    QtWidgets.QLineEdit.Normal, "")
                if ok_pressed and header != '':
                    FilesBlock.save(file, header)

            else:
                file.set_name(list_file[-1])
                header, ok_pressed = QtWidgets.QInputDialog.getText(self, "Get header ", "Enter a header for "
                                                                                         "the save file(optional)",
                                                                    QtWidgets.QLineEdit.Normal, "")
                if ok_pressed and header != '':
                    FilesBlock.save(file, header)


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())


run()