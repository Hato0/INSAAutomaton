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


from StateClass import *


class StateParameters(QDialog, States):
    def __init__(self):
        super(StateParameters, self).__init__()
        print("window creation")
        name = States.get_name()
        status = States.get_status()
        position_x = States.get_position_x()
        position_y = States.get_position_y()
        color = States.get_color()
        shape = States.get_shape()

        self.setGeometry(50, 50, 400, 600)
        self.setWindowTitle("States parameters edit")
        self.setWindowIcon(QIcon('Picture/Logo.png'))

        self.name_get = QLineEdit()
        self.name_get.setObjectName("State Name")
        self.name_get.setText(str(name))

        self.status_get = QLineEdit()
        self.status_get.setObjectName("Status: 'Initial', 'Final', 'Classic'")
        self.status_get.setText(str(status))

        self.position_x_get = QLineEdit()
        self.position_x_get.setObjectName("Position X ")
        self.position_x_get.setText(str(position_x))

        self.position_y_get = QLineEdit()
        self.position_y_get.setObjectName("Position Y")
        self.position_y_get.setText(str(position_y))

        self.color_get = QLineEdit()
        self.color_get.setObjectName("State color wish")
        self.color_get.setText(str(color))

        self.shape_get = QLineEdit()
        self.shape_get.setObjectName("State shape (Square, Rectangle, Circle)")
        self.shape_get.setText(str(shape))

        self.push_button = QPushButton()
        self.push_button.setObjectName("connect")
        self.push_button.setText("Validate")
        self.push_button.clicked.connect(self.end_window)

        layout = QFormLayout()
        layout.addWidget(self.name_get)
        layout.addWidget(self.status_get)
        layout.addWidget(self.position_x_get)
        layout.addWidget(self.position_y_get)

        layout.addWidget(self.shape_get)
        layout.addWidget(self.color_get)
        layout.addWidget(self.push_button)

        self.setLayout(layout)
        self.show()

    def end_window(self):
        self.close()
        States.set_name(self.name_get)
        States.set_status(self.status_get)
        States.set_position_x(self.position_x_get)
        States.set_position_y(self.position_y_get)
        States.set_color(self.color_get)
        States.set_shape(self.shape_get)



