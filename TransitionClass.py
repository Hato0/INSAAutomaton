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


import math

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Transition(QGraphicsItem):
    mid_x: float
    mid_y: float
    print("Transition Class")

    def __init__(self, state_source, state_final, name):
        super(Transition, self).__init__()
        self.arrow_size = 7
        self.source_point = QPointF()
        self.final_point = QPointF()
        self.setAcceptedMouseButtons(Qt.NoButton)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.start = state_source
        self.end = state_final
        self.start.add_transition(self, name)
        self.end.add_transition(self, name)
        self.name = name
        self.adjust()
        self.selected = False

    def set_start_arrow(self, state):
        print("set_start_arrow")
        self.start = state
        self.adjust()

    def set_end_arrow(self, state):
        print("set_end_arrow")
        self.end = state
        self.adjust()

    def adjust(self):
        print("adjust")
        if not self.start or not self.end:
            return
        if self.final_point.x() - self.source_point.x() > 0:
            line = QLineF(self.mapFromItem(self.start, 0, -3), self.mapFromItem(self.end, 0, -3))
        else:
            line = QLineF(self.mapFromItem(self.start, 0, 3), self.mapFromItem(self.end, 0, 3))
        length = line.length()

        self.prepareGeometryChange()

        if length > 20:
            state_offset = QtCore.QPointF((line.dx()*10)/length, (line.dy()*10)/length)
            self.source_point = line.p1() + state_offset
            self.final_point = line.p2() - state_offset
        else:
            self.source_point = line.p1()
            self.final_point = line.p2()

    def boundingRect(self):
        """print("bounding_rectangle")"""
        if not self.start or not self.end:
            return QRectF()
        pen_width = 1
        extra = (pen_width + self.arrow_size)/2

        return QRectF(self.source_point, QSizeF(self.final_point.x() - self.source_point.x(), self.final_point.y() -
                                                self.source_point.y())).normalized()\
            .adjusted(-extra, -extra, extra, extra)

    def paint(self, painter, option, widget):
        """print("painted")"""
        if not self.start or not self.end:
            pass
        line = QLineF(self.source_point, self.final_point)
        if line.length() == 0:
            pass
        if self.selected:
            painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        else:
            painter.setPen(QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(line)
        angle = math.acos(line.dx() / line.length())
        if line.dy() >= 0:
            angle = math.pi * 2 - angle
        dest_arrow_p1 = self.final_point + QtCore.QPointF(math.sin(angle - math.pi / 3) * self.arrow_size,
                                                          math.cos(angle - math.pi / 3 * self.arrow_size))
        dest_arrow_p2 = self.final_point + QtCore.QPointF(math.sin(angle - math.pi + math.pi / 3) * self.arrow_size,
                                                          math.cos(angle - math.pi + math.pi / 3) * self.arrow_size)

        painter.setBrush(Qt.black)
        painter.drawPolygon(QPolygonF([line.p2(), dest_arrow_p1, dest_arrow_p2]))
        self.mid_x = (self.source_point.x() + self.final_point.x()) / 2
        self.mid_y = (self.source_point.y() + self.final_point.y()) / 2
        if self.final_point.x() - self.final_point.x() > 0:
            painter.drawText(self.mid_x - 10, self.mid_y - 10, self.name)
        else:
            painter.drawText(self.mid_x - 10, self.mid_y + 20, self.name)
        self.update()


class SelfTransition(Transition):
    print("SelfTransition Class")
    """
    Class defines transitions of automata.
    """
    Type = QGraphicsItem.UserType + 2

    def __init__(self, state, trans_val):
        Transition.__init__(self, state, state, trans_val)

    def boundingRect(self):
        print("boundingRect")
        if not self.start or not self.end:
            return QRectF()

        pen_width = 1.0
        extra = (pen_width + self.arrow_size) / 2.0

        return QRectF(self.source_point, QSizeF(self.final_point.x() + self.source_point.x() - 50, self.final_point.y()
                                                -
                                                self.source_point.y() - 50)).normalized().\
            adjusted(-extra, -extra, extra, extra)

    def paint(self, painter, option, widget):
        """print("painted")"""
        if not self.source_point or not self.final_point:
            return
        # Draw the line itself.
        path = QPainterPath()
        path.moveTo(self.source_point.x()+10, self.source_point.y()-8)
        path.cubicTo(self.source_point.x(), self.source_point.y()-75, self.source_point.x()-20,
                     self.source_point.y()-75,
                     self.source_point.x()-8, self.source_point.y()-10)
        # draw the curve
        self.mid_x = (self.source_point.x() + self.final_point.x()-75)/2
        self.mid_y = (self.source_point.y()-75 + self.final_point.y())/2

        # change color when self_transition is selected or not.
        if not self.selected:
            painter.setPen(QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        else:
            painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawPath(path)
        painter.drawText(self.mid_x, self.mid_y, self.name)
        self.update()

