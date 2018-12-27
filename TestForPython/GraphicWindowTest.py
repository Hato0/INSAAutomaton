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

from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.le = QLineEdit()
        self.le.setObjectName("host")
        self.le.setText("Host")

        self.pb = QPushButton()
        self.pb.setObjectName("connect")
        self.pb.setText("Connect") 

        layout = QFormLayout()
        layout.addWidget(self.le)
        layout.addWidget(self.pb)

        self.setLayout(layout)
        """self.connect(self.pb, pyqtSignal("clicked()"), self.button_click)"""
        self.setWindowTitle("Learning")

    def button_click(self):
        # shost is a QString object
        shost = self.le.text()
        print(shost)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()