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

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class GridScene(QGraphicsItem):

    def __init__(self):
        super(GridScene, self).__init__()
        self.gridSetView = False

    def paint(self, painter, option, widget):
        numBlockY = 100
        numBlockX = 100
        blockWidth = 10
        blockHeigth = 10
        painter.setBrush(QBrush(QtCore.Qt.SolidPattern))

        for i in range(numBlockY) :
            if i == 0:
                painter.setPen(Qt.red)
                painter.drawLine(-1000, 0, numBlockY * blockWidth, 0)
            else:
                painter.setPen(Qt.gray)
                painter.drawLine(-1000, i * blockHeigth, numBlockY * blockWidth, i * blockHeigth)

        for i in range(numBlockY) :
            if i == 0:
                painter.setPen(Qt.red)
                painter.drawLine(-1000, 0, numBlockY * blockWidth, 0)
            else:
                painter.setPen(Qt.gray)
                painter.drawLine(-1000, -i * blockHeigth, numBlockY * blockWidth, -i * blockHeigth)

        for i in range(numBlockX):
            if i == 0:
                painter.setPen(Qt.red)
                painter.drawLine(0, -600, 0, numBlockX * blockHeigth)
            else:
                painter.setPen(Qt.gray)
                painter.drawLine(i * blockWidth, -600, i * blockWidth, numBlockX * blockHeigth)

        for i in range(numBlockX):
            if i == 0:
                painter.setPen(Qt.red)
                painter.drawLine(0, -600, 0, numBlockX * blockHeigth)
            else:
                painter.setPen(Qt.gray)
                painter.drawLine(-i * blockWidth, -600, -i * blockWidth, numBlockX * blockHeigth)