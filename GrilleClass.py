#  Copyright (C) 2018 Thibaut Lompech - All Rights Reserved
#  You may use, distribute and modify this code under the
#  terms of the legal license, which unfortunately won't be
#  written for another century.
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
        numBlockY = 500
        numBlockX = 500
        blockWidth = 50
        blockHeigth = 50
        painter.setBrush(QBrush(QtCore.Qt.SolidPattern))

        for i in range(numBlockY) :
            if i == 0:
                painter.setPen(Qt.red)
                painter.drawLine(0, -numBlockY * blockWidth, 0, 0)
            else:
                painter.setPen(Qt.gray)
                painter.drawLine(i * blockHeigth, -numBlockY * blockWidth, i * blockHeigth, 0)

        for i in range(numBlockY) :
            if i == 0:
                painter.setPen(Qt.red)
                painter.drawLine(0, -numBlockY * blockWidth, 0, 0)
            else:
                painter.setPen(Qt.gray)
                painter.drawLine(-i * blockHeigth, -numBlockY * blockWidth, -i * blockHeigth, 0)

        for i in range(numBlockY) :
            if i == 0:
                painter.setPen(Qt.red)
                painter.drawLine(0, 0, 0, numBlockY * blockWidth)
            else:
                painter.setPen(Qt.gray)
                painter.drawLine(-i * blockHeigth, numBlockY * blockWidth, -i * blockHeigth, 0)

        for i in range(numBlockY) :
            if i == 0:
                painter.setPen(Qt.red)
                painter.drawLine(0, 0, 0, numBlockY * blockWidth)
            else:
                painter.setPen(Qt.gray)
                painter.drawLine(i * blockHeigth, numBlockY * blockWidth, i * blockHeigth, 0)

        for i in range(numBlockX):
            if i == 0:
                painter.setPen(Qt.red)
                painter.drawLine(-numBlockX * blockHeigth, 0, 0, 0)
            else:
                painter.setPen(Qt.gray)
                painter.drawLine( -numBlockX * blockHeigth, i * blockWidth, 0, i * blockWidth)

        for i in range(numBlockX):
            if i == 0:
                painter.setPen(Qt.red)
                painter.drawLine(-numBlockX * blockHeigth, 0, 0, 0)
            else:
                painter.setPen(Qt.gray)
                painter.drawLine( -numBlockX * blockHeigth, -i * blockWidth, 0, -i * blockWidth)

        for i in range(numBlockX):
            if i == 0:
                painter.setPen(Qt.red)
                painter.drawLine(0, 0, numBlockX * blockHeigth, 0)
            else:
                painter.setPen(Qt.gray)
                painter.drawLine(0, -i * blockWidth, numBlockX * blockHeigth, -i * blockWidth)

        for i in range(numBlockX):
            if i == 0:
                painter.setPen(Qt.red)
                painter.drawLine(0, 0, numBlockX * blockHeigth, 0)
            else:
                painter.setPen(Qt.gray)
                painter.drawLine(0, i * blockWidth, numBlockX * blockHeigth, i * blockWidth)
