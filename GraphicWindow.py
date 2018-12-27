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
from ActionClass import *
from FileClass import FilesBlock
from StateClass import States


class Window(QtWidgets.QMainWindow):

    action_select_square: QAction
    action_select_circle: QAction
    menu_select_states: QMenu
    tbutton: QToolButton
    action_select_rectangle: QAction
    toolBar: QToolBar
    toolBar_list_states: QToolBar
    centralWidget: QWidget
    verticalLayout: QVBoxLayout

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1500, 800)
        self.setWindowTitle("AutoMates project")
        self.setWindowIcon(QtGui.QIcon('Picture/Logo.png'))
        self.graphicsView = GraphWidget()
        self.graphicsView.setObjectName("graphicsView")
        """ Create new widget and associate it to new_application"""
        """ Define a file argument """
        new_action = QtWidgets.QAction("&New", self)
        """ Define a shortcut to extract_action  """
        new_action.setShortcut("Ctrl+N")
        """ Define a description for the file argument """
        new_action.setStatusTip('Create a new empty graph')
        """ Make the file argument append """
        new_action.triggered.connect(self.new_application)
        """ Create open widget and assoiate it to import_application """
        open_action = QtWidgets.QAction("&Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.setStatusTip('Open a saved file')
        open_action.triggered.connect(self.import_application)
        """ Create export widget and associate it to export_application """
        export_action = QtWidgets.QAction("&Export", self)
        export_action.setShortcut("Ctrl+E")
        export_action.setStatusTip('Export to Latex/Tikz')
        export_action.triggered.connect(self.export_application)
        """ Create save widget and associate it to save_application"""
        save_action = QtWidgets.QAction("&Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.setStatusTip('Save the current file')
        save_action.triggered.connect(self.save_application)
        """ Create leave widget and associate it to close_application """
        leave_action = QtWidgets.QAction("&Quit", self)
        leave_action.setShortcut("Ctrl+Q")
        leave_action.setStatusTip('Quit the application')
        leave_action.triggered.connect(self.close_application)
        self.statusBar()

        mainmenu = self.menuBar()
        """ Create the file drop down menu """
        file_menu = mainmenu.addMenu('&File')
        """ Add file parameters """
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(export_action)
        file_menu.addAction(leave_action)
        """ Start the home def """
        self.home()

    def home(self):
        """
        """
        """ Define an icon shortcut with under_text while mouse is on """
        leave_action = QtWidgets.QAction(QtGui.QIcon('Picture/QuitIcon.png'), 'Quit the application', self)
        """ Make the button work """
        leave_action.triggered.connect(self.close_application)
        """ Define button to create new transition """
        transition_action = QtWidgets.QAction(QtGui.QIcon('Picture/Arrow.png'), 'Create transitions', self)
        transition_action.triggered.connect(self.add_transition)

        """ Make the extract_action widget a toolBar which can be move everywhere on the window | Right clic on the top
         able or disable the option"""

        self.menu_select_states = QtWidgets.QMenu("")

        self.tbutton = QtWidgets.QToolButton(self)
        self.tbutton.setMenu(self.menu_select_states)
        self.tbutton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.tbutton.setIcon(QtGui.QIcon("Picture/states.png"))
        self.tbutton.setToolTip("Select state form")

        self.action_select_circle = QtWidgets.QAction(QtGui.QIcon("Picture/circle.png"), "Circle", self)
        """ self.action_select_circle.triggered.connect(self.create_state_circle()) """
        self.menu_select_states.addAction(self.action_select_circle)

        self.action_select_rectangle = QtWidgets.QAction(QtGui.QIcon("Picture/Rectangle.png"), "Rectangle", self)
        """ self.action_select_rectangle.triggered.connect(self.create_states_rectangle()) """
        self.menu_select_states.addAction(self.action_select_rectangle)

        self.action_select_square = QtWidgets.QAction(QtGui.QIcon("Picture/square.png"), "Square", self)
        """ self.action_select_square.triggered.connect(self.create_states_square()) """
        self.menu_select_states.addAction(self.action_select_square)

        self.toolBar = self.addToolBar("Able or Disable options tool_Bar")
        self.toolBar.addWidget(self.tbutton)
        self.toolBar.addAction(transition_action)
        self.toolBar.addAction(leave_action)

        self.toolBar_list_states = self.addToolBar("Able or Disable states show")

        self.setObjectName("main_window")
        self.resize(903, 555)

        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        """ Graphic Views """
        self.graphicsView = GraphWidget()
        self.graphicsView.setObjectName("graphicsView")

        """ Set vertical layout """

        """ Graphic Scene """
        self.setCentralWidget(self.centralWidget)

        self.verticalLayout.addWidget(self.graphicsView)
        self.retranslate_ui(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Graph GUI "))

        self.show()

    def close_application(self):
        """
        Define a pop up window used to inform the user above all active window
        """
        choice = QtWidgets.QMessageBox.question(self, 'Quit application check_box', "Do you really want to quit \n "
                                                                                    "Press No if you haven't save "
                                                                                    "your work",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def new_application(self):
        self.__init__()

    def import_application(self):
        file = FilesBlock()
        text = QtWidgets.QFileDialog.getOpenFileName(self, 'Import File')
        file.set_name(text[0])
        FilesBlock.importation(file)

    def export_application(self):
        file = FilesBlock()
        text = QtWidgets.QFileDialog.getSaveFileName(self, 'Export File')
        file.set_name(text[0])
        FilesBlock.export(file)

    def save_application(self):
        file = FilesBlock()
        text = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        header, ok_pressed = QtWidgets.QInputDialog.getText(self, "Get header ", "Enter a header for "
                                                            "the save file(optional)",
                                                            QtWidgets.QLineEdit.Normal, "")
        file.set_name(text[0])
        if ok_pressed and header != '':
                FilesBlock.save(file, header)

    def create_state_circle(self):
        self.graphicsView.scene.create_states_circle()

    def create_states_rectangle(self):
        pass

    def create_states_square(self):
        pass

    def add_transition(self):
        pass


class GraphWidget(QtWidgets.QGraphicsView):
    """
    Graph Widget definition
    """
    def __init__(self):
        super(GraphWidget, self).__init__()

        self.scene = Scene()
        self.scene.setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)
        self.setScene(self.scene)
        self.setCacheMode(QtWidgets.QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)

    def wheel_event(self, event):
        """
        We can zoom in/ zoom out the GraphicsView by using wheelButton of the mouse.
        """
        self.zoomView(math.pow(2.0, -event.angleDelta().y() / 200.0))

    def zoom_view(self, zoom_factor):
        """
        Scale with the factor calculated.
        """
        factor = self.transform().scale(zoom_factor, zoom_factor).mapRect(QtCore.QRectF(0, 0, 1, 1)).width()
        if factor < 0.09 or factor > 50:
            return
        self.scale(zoom_factor, zoom_factor)


class Scene(QGraphicsScene):
    def __init__(self):
        super(QGraphicsScene, self).__init__()
        self.state_selected = []
        self.trans_selected = []
        self.states_list = []
        self.InvalidInMsg = QtWidgets.QMessageBox()
        self.InvalidInMsg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.InvalidInMsg.setWindowTitle('Invalid input alert!')

    def create_states_circle(self):
        state = States()
        self.addItem(state)
        state.set_position_x(randint(-50, 50))
        state.set_position_y(randint(-50, 50))
        self.states_list.append(state)
        self.update()

    def create_states_rectangle(self):
        pass

    def create_states_square(self):
        pass

    def add_transition(self):
        pass


def run():
    gui: Window
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())


run()
