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
#
#  You should have received a copy of the legal license with
#  this file. If not, please write to: thibaut.lompech@insa-cvl.fr
#


from random import randint

from PyQt5 import QtWidgets

from GrilleClass import GridScene
from StateClass import *
from StateParameters import StateParameters


class Scene(QGraphicsScene):
    print("Scene Class")
    state_parameters: StateParameters
    grid: GridScene

    def __init__(self):
        super(QGraphicsScene, self).__init__()
        self.state_selected = []
        self.trans_selected = []
        self.grid = GridScene()
        self.states_list = []
        self.InvalidInMsg = QMessageBox()
        self.InvalidInMsg.setStandardButtons(QMessageBox.Ok)
        self.InvalidInMsg.setWindowTitle('Invalid input !')

        self.popup = StateParameters()
        self.PopUpWindow = QtWidgets.QDialog()

    def deselect_states(self):
        print("deselect_states")
        """
        Deselect all states
        """
        for state in self.state_selected:
            state.selected = False
        self.state_selected = []

    def deselect_transitions(self):
        print("deselect_transitions")
        """
        Deselect all transitions
        """
        for trans in self.trans_selected:
            trans.selected = False
        self.trans_selected = []

    def keyPressEvent(self, event):
        print("keyPressEvent")
        """
        if delete pressed
        remove edge between selected nodes
        """
        print("key press event", event.key())
        if event.key() == QtCore.Qt.Key_Delete:
            if len(self.state_selected) != 0:
                self.delete_selected_states()
            elif len(self.trans_selected) != 0:
                self.delete_transition()

    def mouseDoubleClickEvent(self, event):
        print("mouseDoubleClickEvent")
        """
        CHANGE TO OPEN WINDOW PARAMETERS
        Rename with double mouse click
        """
        self.select_elements(event)
        print(self.state_selected)
        if len(self.state_selected) == 1:
            self.popup_window()
        else:
            pass

    def popup_window(self):
        print("popup_window")
        if len(self.state_selected) == 1:
            self.popup.setup_popup(self.PopUpWindow, self.state_selected[0])
            self.deselect_states()
            self.update()
        else:
            pass

    def mousePressEvent(self, event):
        print("mousePressEvent")

        if event.button() == QtCore.Qt.RightButton:
            self.select_elements(event)
            return
        if event.button() == QtCore.Qt.MidButton:
            self.rename()
            return
        QtWidgets.QGraphicsScene.mousePressEvent(self, event)
        print("Mouse press Event")

    def create_state(self):
        print("create_state")
        """
        Create new state , random place it on scene, add to states_list
        """
        state = States(self)
        self.addItem(state)
        state.setPos(randint(-50, 50), randint(-50, 50))
        self.states_list.append(state)
        self.update()
        return state

    def create_initial(self):
        print("create_initial")
        """
        Make chosen states  initials
        """
        for state in self.state_selected:
            state.status = 0
        self.deselect_states()
        self.update()

    def create_final(self):
        print("create_final")
        """
        Make chosen states  finals
        """
        for state in self.state_selected:
            state.status = 2
        self.deselect_states()
        self.update()

    def create_finalAndInitial(self):
        print("create_final_and_initial")
        """
        Make chosen states  finals and initial
        """
        for state in self.state_selected:
            state.status = 3
        self.deselect_states()
        self.update()

    def select_elements(self, event):
        print("select_elements")
        """
        Change color and status of chosen items. Add to list state_selected or trans_selected
        """
        element = self.itemAt(event.scenePos(), QtGui.QTransform())
        """ get item clicked on at this position in scene """
        """ if it is a state,and not chosen yet, choose it add to state_selected,  if it is already chosen we deselect 
        it and remove from state_selected"""
        if isinstance(element, States):
            if not element.selected:
                element.selected = True
                self.state_selected.append(element)
            else:
                element.selected = False
                self.state_selected.remove(element)
        """ if it is a transition or self-transition,and not chosen yet, choose it add to trans_selected,  if it is 
        already chosen we deselect it and remove from trans_selected """
        if isinstance(element, Transition) or isinstance(element, SelfTransition):
            if not element.selected:
                element.selected = True
                self.trans_selected.append(element)
            else:
                element.selected = False
                self.trans_selected.remove(element)
        self.update()

    def addGrid(self):
        print("Change show")
        if not self.grid.gridSetView:
            print("Show grid")
            self.grid.gridSetView = True
            self.addItem(self.grid)
            self.update()
        elif self.grid.gridSetView:
            print("Hide grid")
            self.grid.gridSetView = False
            self.removeItem(self.grid)
            self.update()

    def create_transition(self):
        print("create_transition")
        """
        Create transition between 2 chosen state. The first chosen one is source, the second is destination
        We can choose one state to create a transition towards itself.
        """
        trans_name, ok_pressed = QtWidgets.QInputDialog.getText(QtWidgets.QMainWindow(), 'Create Transition',
                                                                'Enter Transition Name:')
        if ok_pressed:
            """ If 2 states are chosen, create a transition with a name between these. """
            if len(self.state_selected) == 2:
                """ Check if between 2 states there is already a transition """
                for trans in self.items():
                    if isinstance(trans, Transition):
                        if trans.source_point == self.state_selected[0] and trans.dest == self.state_selected[1]:
                            self.InvalidInMsg.setText('Transition already exists')
                            self.InvalidInMsg.exec_()
                            self.deselect_states()
                            return
                """ If there isn't, we create a new transition """
                self.addItem(Transition(self.state_selected[0], self.state_selected[1], trans_name))
                self.deselect_states()
                self.update()
            elif len(self.state_selected) == 1:
                """ if only 1 state is chosen, we create a self-transition of that state """
                self.addItem(SelfTransition(self.state_selected[0], trans_name))
                self.deselect_states()
                self.update()
            else:
                """ if we choose > 2 transition, we can not create a transition """
                self.InvalidInMsg.setText('Must select 2 states to create transition')
                self.InvalidInMsg.exec_()

    def create_transition_courbe(self):
        print("create_transition_courbe")
        """
        Create transition between 2 chosen state. The first chosen one is source, the second is destination
        We can choose one state to create a transition towards itself.
        """
        trans_val, ok_pressed = QtWidgets.QInputDialog.getText(QtWidgets.QMainWindow(), 'Create Transition Curved',
                                                               'Enter Transition Name:')
        if ok_pressed:
            """ If 2 states are chosen, create a transition with a name between these. """
            if len(self.state_selected)== 2:
                """ Check if between 2 states there is already a transition """
                for trans in self.items():
                    if isinstance(trans, TransitionCourbe):
                        if trans.source_point == self.state_selected[0] and trans.dest == self.state_selected[1]:
                            self.InvalidInMsg.setText('Transition already exists')
                            self.InvalidInMsg.exec_()
                            self.deselect_states()
                            return
                """ If there isn't, we create a new transition """
                self.addItem(TransitionCourbe(self.state_selected[0], self.state_selected[1], trans_val))
                self.deselect_states()
                self.update()
            elif len(self.state_selected) == 1:
                """ if only 1 state is chosen, we create a self-transition of that state """
                self.addItem(SelfTransition(self.state_selected[0], trans_val))
                self.deselect_states()
                self.update()
            else:
                """ if we choose > 2 transition, we can not create a transition """
                self.InvalidInMsg.setText('Must select 2 states to create transition')
                self.InvalidInMsg.exec_()

    def delete_selected_states(self):
        print("delete_selected_states")
        """
        Delete chosen state and all transitions connect to it.
        """
        for state in self.state_selected:
            for i in range(len(state.link)):
                self.removeItem(state.link[i])
            self.removeItem(state)
        for state in self.selectedItems():
            # check on all selected items, if there are states then delete them.
            if isinstance(state, States):
                for i in range(len(state.link)):
                    self.removeItem(state.link[i])
                self.removeItem(state)
                state.setSelected(0)
        self.state_selected = []
        self.update()

    def delete_transition(self):
        print("delete_transition")
        """
        Delete chosen transitions.
        """
        for transition in self.trans_selected:
            source = transition.start
            destination = transition.end
            for trans in source.link:
                if trans == transition:
                    source.link.remove(transition)
            for trans in destination.link:
                if trans == transition:
                    destination.link.remove(transition)
            self.removeItem(transition)
        for transition in self.selectedItems():
            if isinstance(transition, Transition) or isinstance(transition, SelfTransition):
                self.removeItem(transition)
                transition.setSelected(0)
        self.trans_selected = []
        self.update()

    def rename(self):
        print("re_define")
        new_name, ok_pressed = QtWidgets.QInputDialog.getText(QtWidgets.QMainWindow(), 'Rename state',
                                                             'Enter a name :')
        if ok_pressed:
            if new_name == "":
                self.InvalidInMsg.setText("Can't be empty")
                self.InvalidInMsg.exec_()
            else:
                if len(self.trans_selected) == 1:
                    for transition in self.trans_selected:
                        if type(transition) == Transition:
                            self.removeItem(transition)
                            self.addItem(Transition(self.trans_selected[0].source, self.trans_selected[0].dest, new_name)
                                         )
                            self.trans_selected.clear()
                            self.deselect_transitions()
                            self.update()
                        else:
                            self.removeItem(transition)
                            self.addItem(SelfTransition(self.trans_selected[0].source, new_name))
                            self.trans_selected.clear()
                            self.deselect_transitions()
                            self.update()
                elif len(self.state_selected) == 1:
                    flag = True
                    for state in self.state_selected:
                        for item in self.items():
                            if isinstance(item, States):
                                if item.name == new_name:
                                    flag = False
                        if flag:
                            state.name = new_name
                            state.setPos(state.pos().x(), state.pos().y())
                            state.position_x = state.pos().x()
                            state.position_y = state.pos().y()
                            self.deselect_states()
                            self.state_selected.clear()
                            self.update()
                        else:
                            self.InvalidInMsg.setText('A state with this name exist')
                            self.InvalidInMsg.exec_()

                else:
                    self.InvalidInMsg.setText('Only 1 state !')
                    self.InvalidInMsg.exec_()

    """def reorganize(self, radius=150, s=0):
        print("reorganize")
        
        Reorganise chosen state as a form of a regular polygon
        
        deplace = 800
        stateselected = []
        for state in self.selectedItems():
            if isinstance(state, States):
                stateselected.append(state)

        if len(stateselected) > 0:
            ''' then calcul geometric form '''
            w = 360 / len(stateselected)
            for i in range(len(stateselected)):
                t = w * i + deplace
                x = radius * math.cos(math.radians(t))
                y = radius * math.sin(math.radians(t))
                stateselected[i].move_state(x, y)
        elif len(self.state_selected) > 0:
            ''' then calcul geometric form '''
            w = 360 / len(self.state_selected)
            for i in range(len(self.state_selected)):
                t = w * i + deplace
                x = radius * math.cos(math.radians(t))
                y = radius * math.sin(math.radians(t))
                self.state_selected[i].move_state(x, y)
        self.deselect_states()
        for i in stateselected:
            i.setSelected(0)
        stateselected = []"""

