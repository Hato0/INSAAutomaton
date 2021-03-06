#  Copyright (C) 2018 Thibaut Lompech - All Rights Reserved
#  You may use, distribute and modify this code under the
#  terms of the legal license, which unfortunately won't be
#  written for another century.
#
#  You should have received a copy of the legal license with
#  this file. If not, please write to: thibaut.lompech@insa-cvl.fr
#

from typing import Any, Union

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel

from StateClass import States


class StateParameters(QDialog):
    status: str
    name: str
    position_x: str
    position_y: str
    color: str
    shape: str
    state: Union[States, Any]
    label_name: QLabel
    label_color: QLabel
    label_x_position: QLabel
    label_y_position: QLabel
    label_status: QLabel
    label_shape: QLabel
    push_button: QPushButton
    shape_get: QLineEdit
    color_get: QLineEdit
    position_y_get: QLineEdit
    position_x_get: QLineEdit
    status_get: QLineEdit
    name_get: QLineEdit

    def __init__(self):
        self.status = int()
        super(StateParameters, self).__init__()

    def setup_popup(self, MainWindowParameters, state):
        print("window creation")
        print("initialisation of state parameters")
        self.state = state
        name = state.get_name()
        status = state.get_status()
        position_x = state.get_position_x()
        position_y = state.get_position_y()
        color = state.get_color()
        shape = state.get_shape()

        super().__init__()
        MainWindowParameters.setWindowTitle("States parameters edit")
        MainWindowParameters.setGeometry(50, 50, 400, 600)
        MainWindowParameters.setWindowIcon(QtGui.QIcon('Picture/Logo.png'))

        self.setWindowIcon(QtGui.QIcon('Picture/Logo.png'))
        self.setGeometry(50, 50, 400, 600)
        self.setWindowTitle("States parameters edit")

        self.label_name = QLabel()
        self.label_name.setText("State name :")
        self.label_name.setGeometry(20, 20, 20, 20)

        self.name_get = QLineEdit()
        self.name_get.setObjectName("State Name")
        self.name_get.setText(str(name))

        self.label_status = QLabel()
        self.label_status.setText("State status (initial = 0 , final = 2 , normal = 1 , initial and final = 3 ) :")
        self.label_status.setGeometry(20, 20, 20, 20)

        self.status_get = QLineEdit()
        self.status_get.setObjectName("Status: 'Initial', 'Final', 'Classic' , 'Initial and Final'")
        self.status_get.setText(str(status))

        self.label_x_position = QLabel()
        self.label_x_position.setText("State position X axe :")
        self.label_x_position.setGeometry(20, 20, 20, 20)

        self.position_x_get = QLineEdit()
        self.position_x_get.setObjectName("Position X ")
        self.position_x_get.setText(str(position_x))

        self.label_y_position = QLabel()
        self.label_y_position.setText("State position Y axe :")
        self.label_y_position.setGeometry(20, 20, 20, 20)

        self.position_y_get = QLineEdit()
        self.position_y_get.setObjectName("Position Y")
        self.position_y_get.setText(str(position_y))

        self.label_color = QLabel()
        self.label_color.setText("State color :")
        self.label_color.setGeometry(20, 20, 20, 20)

        self.color_get = QLineEdit()
        self.color_get.setObjectName("State color wish")
        self.color_get.setText(str(color))

        self.label_shape = QLabel()
        self.label_shape.setText("State shape :")
        self.label_shape.setGeometry(20, 20, 20, 20)

        self.shape_get = QLineEdit()
        self.shape_get.setObjectName("State shape (Square, Rectangle, Circle)")
        self.shape_get.setText(str(shape))
        self.push_button = QPushButton("Validate", self)
        self.push_button.setToolTip("This will upgrade your state")
        self.push_button.clicked.connect(self.end_window)

        layout = QtWidgets.QFormLayout()
        layout.addWidget(self.label_name)
        layout.addWidget(self.name_get)
        layout.addWidget(self.label_status)
        layout.addWidget(self.status_get)
        layout.addWidget(self.label_x_position)
        layout.addWidget(self.position_x_get)
        layout.addWidget(self.label_y_position)
        layout.addWidget(self.position_y_get)
        layout.addWidget(self.label_shape)
        layout.addWidget(self.shape_get)
        layout.addWidget(self.label_color)
        layout.addWidget(self.color_get)
        layout.addWidget(self.push_button)
        self.setLayout(layout)
        self.show()

    def end_window(self):
        self.close()

        self.name = self.name_get.text()
        self.status = self.status_get.text()
        self.position_x = self.position_x_get.text()
        self.position_y = self.position_y_get.text()
        self.color = self.color_get.text()
        self.shape = self.shape_get.text()

        self.state.set_name(self.name)
        self.state.status = self.status
        self.state.setPos(float(self.position_x), float(self.position_y))
        self.state.set_position_x(self.position_x)
        self.state.set_position_y(self.position_y)
        self.state.set_color(self.color)
        self.state.set_shape(self.shape)
        self.state.update()

