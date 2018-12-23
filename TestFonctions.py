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
#
#  You should have received a copy of the legal license with
#  this file. If not, please write to: thibaut.lompech@insa-cvl.fr
#
#
#  You should have received a copy of the legal license with
#  this file. If not, please write to: thibaut.lompech@insa-cvl.fr
#
#
#  You should have received a copy of the legal license with
#  this file. If not, please write to: thibaut.lompech@insa-cvl.fr


import sys

from PyQt5 import QtGui, QtWidgets

from FileClass import FilesBlock;


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        files = FilesBlock()
        self.setGeometry(50, 50, 1500, 800)
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
        self.setCentralWidget(self.centralWidget())

        main_menu = self.
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
        """ Define an icon shortcut with under_text while mouse is on """
        leave_action = QtWidgets.QAction(QtGui.QIcon('Picture/QuitIcon.png'), 'Quit the application', self)
        """ Make the button work """
        leave_action.triggered.connect(self.close_application)
        """ Define button to create new transition """
        transition_action = QtWidgets.QAction(QtGui.QIcon('Picture/Arrow.png'), 'Create transitions', self)
        transition_action.triggered.connect(self.add_transition)

        """ Make the extract_action widget a toolBar which can be move everywhere on the window | Right clic on the top
         able or disable the option"""

        self.menu_select_states = QtWidgets.QMenu("")

        self.tbutton = QtWidgets.QToolButton(self)
        self.tbutton.setMenu(self.menu_select_states)
        self.tbutton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.tbutton.setIcon(QtGui.QIcon("Picture/states.png"))
        self.tbutton.setToolTip("Select state form")

        self.action_select_circle = QtWidgets.QAction(QtGui.QIcon("Picture/circle.png"), "Circle", self)
        self.action_select_circle.triggered.connect(self.create_states_circle)
        self.menu_select_states.addAction(self.action_select_circle)

        self.action_select_rectangle = QtWidgets.QAction(QtGui.QIcon("Picture/Rectangle.png"), "Rectangle", self)
        self.action_select_rectangle.triggered.connect(self.create_states_rectangle)
        self.menu_select_states.addAction(self.action_select_rectangle)

        self.action_select_square = QtWidgets.QAction(QtGui.QIcon("Picture/square.png"), "Square", self)
        self.action_select_square.triggered.connect(self.create_states_square)
        self.menu_select_states.addAction(self.action_select_square)

        self.toolBar = self.addToolBar("Able or Disable Tool Bar")
        self.toolBar.addWidget(self.tbutton)
        self.toolBar.addAction(transition_action)
        self.toolBar.addAction(leave_action)

        self.show()

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
        self.__init__()

    def import_application(self):
        file = FilesBlock()
        text = QtWidgets.QFileDialog.getOpenFileName(self, 'Import File')
        file.set_name(text[0])
        FilesBlock.importation(file)

    def export_application(self):
        file = FilesBlock()
        text = QtWidgets.QFileDialog.getSaveFileName(self, 'Export File')
        file.set_name(text[0])
        FilesBlock.export(file)

    def save_application(self):
        file = FilesBlock()
        text = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        header, ok_pressed = QtWidgets.QInputDialog.getText(self, "Get header ", "Enter a header for "
                                                            "the save file(optional)",
                                                            QtWidgets.QLineEdit.Normal, "")
        file.set_name(text[0])
        if ok_pressed and header != '':
                FilesBlock.save(file, header)

    def create_states_circle(self):
        print(1)
        pass

    def create_states_rectangle(self):
        print(2)
        pass

    def create_states_square(self):
        print(3)
        pass

    def add_transition(self):
        pass


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())


run()