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
#
#
#  You should have received a copy of the legal license with
#  this file. If not, please write to: thibaut.lompech@insa-cvl.fr
#


from PyQt5 import QtGui

from TransitionClass import *


class States(QGraphicsItem):
    registry = []
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print("States Class")

    def __init__(self, graphwidget):
        """
        Initialisation of States Object
        """
        super(States, self).__init__()
        self.registry.append(self)
        self.position = QtCore.QPointF()
        self.position_x = self.position.x()
        self.position_y = self.position.y()
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setCursor(Qt.OpenHandCursor)
        self.status = 1
        self.selected = False
        self.name = ""
        self.arrowSize = 5
        self.link = []
        self.color = "white"
        self.shape = "circle"
        self.link_name = []
        self.attributeletter = self.alpha[len(self.registry)]

    def add_transition(self, transition, transition_name):
        print("add_transition")
        """
        Add a transition to the node
        :param transition:
        :return:
        """
        self.add_link(transition)
        self.add_link_name(transition_name)

    def add_transition_courbe(self, transition, transition_name):
        print("add_transition_courbe")
        """
        Add a transition curved to the node
        :param transition:
        :return:
        """
        self.add_link(transition)
        self.add_link_name(transition_name)
        transition.adjust()

    def move_state(self, position_x, position_y):
        print("move_state")
        if self.position == self.pos():
            return False
        self.setPos(position_x, position_y)
        self.position_x = self.position.x()
        self.position_y = self.position.y()
        return True

    def boundingRect(self):
        """print("boundingRect")"""
        param = 2
        return QtCore.QRectF(-10 - param, -10 - param, 23 + param, 23 + param)

    @staticmethod
    def shape_determination():
        figure = QtGui.QPainterPath()
        figure.addEllipse(-15, -15, 30, 30)
        return figure

    def paint(self, painter, option, widget: QWidget = None):
        """print("paint")"""
        """
        Set color for States , change color when select and deselect state
        """
        if self.selected:
            """In this case, we choose as right click"""
            self.setSelected(0)
            """if the state is seleted paint it blue"""
            """Set pen to black"""
            painter.setPen(Qt.black)
            painter.setBrush(Qt.red)
            """paint the initial state orange when selected and keep the arrow. Description for drawing arrow is 
            explained in method Transition.paint()"""
            if self.status == 0:
                arrow = QPointF(-10, 0)
                line = QLineF(-30, 0, -10, 0)
                angle = math.acos(line.dx() / line.length())
                if line.dy() >= 0:
                    angle = math.pi * 2 - angle
                dest_arrow_p1 = arrow + QtCore.QPointF(math.sin(angle - math.pi / 3) * self.arrowSize,
                                                       math.cos(angle - math.pi / 3) * self.arrowSize)
                dest_arrow_p2 = arrow + QtCore.QPointF(math.sin(angle - math.pi + math.pi / 3) * self.arrowSize,
                                                       math.cos(angle - math.pi + math.pi / 3) * self.arrowSize)
                painter.drawPolygon(QPolygonF([line.p2(), dest_arrow_p1, dest_arrow_p2]))
                painter.setPen(Qt.black)
                painter.drawLine(-10, 0, -30, 0)
                """paint the final state blue when selected, keep the outside circle"""
            elif self.status == 2:
                painter.drawEllipse(QtCore.QRectF(-25 / 2.0, -25 / 2.0, 25, 25))
            elif self.status == 3:
                arrow = QPointF(-10, 0)
                line = QLineF(-30, 0, -10, 0)
                angle = math.acos(line.dx() / line.length())
                if line.dy() >= 0:
                    angle = math.pi * 2 - angle
                dest_arrow_p1 = arrow + QtCore.QPointF(math.sin(angle - math.pi / 3) * self.arrowSize,
                                                       math.cos(angle - math.pi / 3) * self.arrowSize)
                dest_arrow_p2 = arrow + QtCore.QPointF(math.sin(angle - math.pi + math.pi / 3) * self.arrowSize,
                                                       math.cos(angle - math.pi + math.pi / 3) * self.arrowSize)
                painter.drawPolygon(QPolygonF([line.p2(), dest_arrow_p1, dest_arrow_p2]))
                painter.setPen(Qt.black)
                painter.drawLine(-10, 0, -30, 0)
                painter.drawEllipse(QtCore.QRectF(-25 / 2.0, -25 / 2.0, 25, 25))
                """draw the state initial"""
        elif self.isSelected():
            """In this case, we choose as left click or choose mouse area by left click"""
            """pain it blue when selected"""
            painter.setPen(Qt.black)
            painter.setBrush(Qt.blue)
            if self.status == 0:
                arrow = QPointF(-10, 0)
                line = QLineF(-30, 0, -10, 0)
                angle = math.acos(line.dx() / line.length())
                if line.dy() >= 0:
                    angle = math.pi * 2 - angle
                dest_arrow_p1 = arrow + QtCore.QPointF(math.sin(angle - math.pi / 3) * self.arrowSize,
                                                       math.cos(angle - math.pi / 3) * self.arrowSize)
                dest_arrow_p2 = arrow + QtCore.QPointF(math.sin(angle - math.pi + math.pi / 3) * self.arrowSize,
                                                       math.cos(angle - math.pi + math.pi / 3) * self.arrowSize)
                painter.drawPolygon(QPolygonF([line.p2(), dest_arrow_p1, dest_arrow_p2]))
                painter.setPen(Qt.black)
                painter.drawLine(-10, 0, -30, 0)
            elif self.status == 2:
                painter.drawEllipse(QtCore.QRectF(-25 / 2.0, -25 / 2.0, 25, 25)) # draw the state initial
            elif self.status == 3:
                arrow = QPointF(-10, 0)
                line = QLineF(-30, 0, -10, 0)
                angle = math.acos(line.dx() / line.length())
                if line.dy() >= 0:
                    angle = math.pi * 2 - angle
                dest_arrow_p1 = arrow + QtCore.QPointF(math.sin(angle - math.pi / 3) * self.arrowSize,
                                                       math.cos(angle - math.pi / 3) * self.arrowSize)
                dest_arrow_p2 = arrow + QtCore.QPointF(math.sin(angle - math.pi + math.pi / 3) * self.arrowSize,
                                                       math.cos(angle - math.pi + math.pi / 3) * self.arrowSize)
                painter.drawPolygon(QPolygonF([line.p2(), dest_arrow_p1, dest_arrow_p2]))
                painter.setPen(Qt.black)
                painter.drawLine(-10, 0, -30, 0)
                painter.drawEllipse(QtCore.QRectF(-25 / 2.0, -25 / 2.0, 25, 25))
            """draw the initial state (when we create or unselected)"""
        elif self.status == 0:
                arrow = QPointF(-10, 0)
                line = QLineF(-30, 0, -10, 0)
                angle = math.acos(line.dx() / line.length())
                if line.dy() >= 0:
                    angle = math.pi * 2 - angle
                dest_arrow_p1 = arrow + QtCore.QPointF(math.sin(angle - math.pi / 3) * self.arrowSize,
                                                       math.cos(angle - math.pi / 3) * self.arrowSize)
                dest_arrow_p2 = arrow + QtCore.QPointF(math.sin(angle - math.pi + math.pi / 3) * self.arrowSize,
                                                       math.cos(angle - math.pi + math.pi / 3) * self.arrowSize)
                painter.drawPolygon(QPolygonF([line.p2(), dest_arrow_p1, dest_arrow_p2]))
                painter.setPen(Qt.black)
                painter.drawLine(-10, 0, -30, 0)
                """draw the final state (when we create or unselected)"""
        elif self.status == 2:
            painter.drawEllipse(QtCore.QRectF(-25 / 2.0, -25 / 2.0, 25, 25))
        elif self.status == 3:
                arrow = QPointF(-10, 0)
                line = QLineF(-30, 0, -10, 0)
                angle = math.acos(line.dx() / line.length())
                if line.dy() >= 0:
                    angle = math.pi * 2 - angle
                dest_arrow_p1 = arrow + QtCore.QPointF(math.sin(angle - math.pi / 3) * self.arrowSize,
                                                       math.cos(angle - math.pi / 3) * self.arrowSize)
                dest_arrow_p2 = arrow + QtCore.QPointF(math.sin(angle - math.pi + math.pi / 3) * self.arrowSize,
                                                       math.cos(angle - math.pi + math.pi / 3) * self.arrowSize)
                painter.drawPolygon(QPolygonF([line.p2(), dest_arrow_p1, dest_arrow_p2]))
                painter.setPen(Qt.black)
                painter.drawLine(-10, 0, -30, 0)
                painter.drawEllipse(QtCore.QRectF(-25 / 2.0, -25 / 2.0, 25, 25))
        else:
            """draw the normal state (when we create or unselected)"""
            painter.setPen(Qt.black)
            painter.setBrush(Qt.white)
        painter.drawEllipse(QtCore.QRectF(-20 / 2.0, -20 / 2.0, 20, 20))
        painter.drawText(QtCore.QRect(-10, -10, 20, 20), QtCore.Qt.AlignCenter, self.name)
        self.update()

    def state_color(self, painter):
        print("state_color")
        if self.selected:
            painter.setPen(Qt.black)
            painter.setBrush(QColor(self.get_color()))
            painter.drawEllipse(QtCore.QRectF(-20 / 2, -20 / 2, 20, 20))
            painter.drawText(QtCore.QRect(-10, -10, 20, 20), QtCore.Qt.AlignCenter, self.name)
            self.update()

    def itemChange(self, change, value):
        print("movement")
        if change == QGraphicsItem.ItemPositionHasChanged:
            self.position_x = self.pos().x()
            self.position_y = self.pos().y()
            for transition in self.link:
                transition.adjust()
        return super(States, self).itemChange(change, value)

    def get_status(self):
        """

        :return: int
        Return states status
        """
        return self.status

    def set_status(self, v):
        """

        :param v: int
        :return: None
        Change states status
        """
        if v != self.status:
            self.status = v
            self.update()

    def get_name(self):
        """

        :return: char
        Return states name
        """
        return self.name

    def set_name(self, v):
        """

        :param v: char
        :return: None
        Change states name
        """
        self.name = v

    def get_position_x(self):
        """

        :return: Tuple
        Return states position
        """
        return self.position_x

    def set_position_x(self, v):
        """

        :param v: Tuple
        :return: None
        Change states position
        """
        self.position_x = v

    def get_position_y(self):
        """

        :return: Tuple
        Return states position
        """
        return self.position_y

    def set_position_y(self, v):
        """

        :param v: Tuple
        :return: None
        Change states position
        """
        self.position_y = v

    def get_link(self):
        """

        :return: list
        Return states which is link to the actual states
        """
        return self.link

    def get_link_name(self):
        """

        :return: list
        Return states which is link to the actual states
        """
        return self.link_name

    def add_link(self, v):
        """

        :param v: char
        :return: None
        Add link with an other states
        """
        self.link.append(v)

    def enlimination_link(self, v):
        """
        :param v: char
        :return:  Supress a link for the current states
        """
        self.link.remove(v)

    def add_link_name(self, v):
        """

        :param v: char
        :return: None
        Add link name with an other states
        """
        self.link_name.append(v)

    def enlimination_link_name(self, v):
        """
        :param v: char
        :return:  Supress a link for the current states
        """
        del self.link_name[self.link.index(v)]

    def set_color(self, v):
        """

        :param v: char
        Change states background color
        """
        self.color = v

    def get_color(self):
        """

        :return: char
        Return states background color
        """
        return self.color

    def set_shape(self, v):
        """

        :param v: char
        Change states shape
        """
        self.shape = v

    def get_shape(self):
        """

        :return: char
        Return states shape
        """
        return self.shape

    def get_attributeletter(self):
        """

        :return: int
        Return states letter attribute
        """
        return self.attributeletter

    def set_attributeletter(self, v):
        """

        :param v: int
        :return: None
        Change states letter associate
        """

        self.attributeletter = v
