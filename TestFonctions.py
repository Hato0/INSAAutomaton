#  Copyright (C) 2018 Thibaut Lompech - All Rights Reserved
#  You may use, distribute and modify this code under the
#  terms of the legal license, which unfortunately won't be
#  written for another century.
#
#  You should have received a copy of the legal license with
#  this file. If not, please write to: thibaut.lompech@insa-cvl.fr
#

from PyQt5 import QtCore , QtWidgets


class GraphicsScene:
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        self.setSceneRect(-100, -100, 200, 200)
        self.opt = ""

    def setOption(self, opt):
        self.opt = opt

    def mousePressEvent(self, event):
        pen = QPen(QtCore.Qt.black)
        brush = QBrush(QtCore.Qt.black)
        x = event.scenePos().x()
        y = event.scenePos().y()
        if self.opt == "Generate":
            self.addEllipse(x, y, 4, 4, pen, brush)
        elif self.opt == "Select":
            print(x, y)


class SimpleWindow(QtWidgets.QMainWindow, QtCore.QPoint.Ui_Dialog):
    def __init__(self, parent=None):
        super(SimpleWindow, self).__init__(parent)
        self.setupUi(self)

        self.scene = GraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        group = QButtonGroup(self)
        group.addButton(self.radioButton)
        group.addButton(self.radioButton_2)

        group.buttonClicked.connect(lambda btn: self.scene.setOption(btn.text()))
        self.radioButton.setChecked(True)
        self.scene.setOption(self.radioButton.text())

run()