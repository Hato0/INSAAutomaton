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

import math

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(903, 555)

        self.centralWidget = QtWidgets.QWidget(main_window)
        self.centralWidget.setObjectName("centralWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")

        """ Graphic Views """
        self.graphicsView = GraphWidget()
        self.graphicsView.setObjectName("graphicsView")

        """ Set vertical layout """
        self.verticalLayout.addLayout(self.horizontalLayout)

        """ Graphic Scene """
        self.verticalLayout.addWidget(self.graphicsView)
        main_window.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(main_window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 903, 28))

        # Menu Bar
        self.menuBar.setObjectName("menuBar")
        main_window.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(main_window)
        self.mainToolBar.setObjectName("mainToolBar")
        main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(main_window)
        self.statusBar.setObjectName("statusBar")
        main_window.setStatusBar(self.statusBar)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Graph GUI "))

    """ This is functions of layout """
    def state(self):
        pass

    def initial(self):
        pass

    def final(self):
        pass

    def transition(self):
        pass

    def export(self):
        pass

    def remove(self):
        pass

    def remove_transition(self):
        pass

    def rename(self):
        pass

    def reorganize(self):
        pass

    def manual(self):
        # import sys
        ui1 = manual()
        ui1.setup_ui(window_manual)
        window_manual.show()


class GraphWidget(QGraphicsView):
    """
    Graph Widget definition
    """
    def __init__(self):
        super(GraphWidget, self).__init__()
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.setDragMode(QGraphicsView.RubberBandDrag)

    def wheelEvent(self, event):
        """
        We can zoom in/ zoom out the GraphicsView by using wheelButton of the mouse.
        """
        self.zoomView(math.pow(2.0, -event.angleDelta().y() / 200.0))

    def zoomView(self, zoomFactor):
        """
        Scale with the factor calculated.
        """
        factor = self.transform().scale(zoomFactor, zoomFactor).mapRect(QRectF(0, 0, 1, 1)).width()
        if factor < 0.09 or factor > 50:
            return
        self.scale(zoomFactor, zoomFactor)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    window_manual = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
