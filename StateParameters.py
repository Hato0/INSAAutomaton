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
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton


class StateParameters(QDialog):
    push_button: QPushButton
    shape_get: QLineEdit
    color_get: QLineEdit
    position_y_get: QLineEdit
    position_x_get: QLineEdit
    status_get: QLineEdit
    name_get: QLineEdit
    print("StateParameters Class")

    def setup_popup(self, MainWindowParameters):
        print("window creation")
        print("initialisation of state parameters")
        """name = States.get_name()
        status = States.get_status()
        position_x = States.get_position_x()
        position_y = States.get_position_y()
        color = States.get_color()
        shape = States.get_shape()"""

        super().__init__()
        MainWindowParameters.setWindowTitle("States parameters edit")
        MainWindowParameters.setGeometry(50, 50, 400, 600)
        MainWindowParameters.setWindowIcon(QtGui.QIcon('Picture/Logo.png'))

        self.name_get = QLineEdit()
        self.name_get.setObjectName("State Name")
        """self.name_get.setText(str(name))"""

        self.status_get = QLineEdit()
        self.status_get.setObjectName("Status: 'Initial', 'Final', 'Classic'")
        """self.status_get.setText(str(status))"""

        self.position_x_get = QLineEdit()
        self.position_x_get.setObjectName("Position X ")
        """self.position_x_get.setText(str(position_x))"""

        self.position_y_get = QLineEdit()
        self.position_y_get.setObjectName("Position Y")
        """self.position_y_get.setText(str(position_y))"""

        self.color_get = QLineEdit()
        self.color_get.setObjectName("State color wish")
        """self.color_get.setText(str(color))"""

        self.shape_get = QLineEdit()
        self.shape_get.setObjectName("State shape (Square, Rectangle, Circle)")
        """self.shape_get.setText(str(shape))"""

        print("before button initialisation")
        self.push_button = QPushButton("Validate", self)
        self.push_button.setToolTip("This will upgrade your state")
        self.push_button.clicked.connect(self.end_window)
        print("After button initialisation")
        layout = QtWidgets.QFormLayout()
        layout.addWidget(self.name_get)
        layout.addWidget(self.status_get)
        layout.addWidget(self.position_x_get)
        layout.addWidget(self.position_y_get)
        print("layout setup done")
        layout.addWidget(self.shape_get)
        layout.addWidget(self.color_get)
        layout.addWidget(self.push_button)
        print("faitttttt")
        self.setLayout(layout)

    def end_window(self):
        print("end_window")
        self.close()

    def get_name(self):
        return self.name_get

    def get_position_x(self):
        return self.position_x_get

    def get_position_y(self):
        return self.position_y_get

    def get_status(self):
        return self.status_get

    def get_shape(self):
        return self.shape_get
