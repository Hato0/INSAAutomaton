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


from GraphicWindow import *
from StateClass import *


class Scene(QGraphicsScene):
    def __init__(self):
        super(QGraphicsScene, self).__init__()
        self.state_selected = []
        self.trans_selected = []
        self.InvalidInMsg = QMessageBox()
        self.InvalidInMsg.setStandardButtons(QMessageBox.Ok)
        self.InvalidInMsg.setWindowTitle('Invalid input !')

    def deselect_states(self):
        """
        Deselect all states
        """
        for state in self.state_selected:
            state.selected = False
        self.state_selected = []

    def deselect_transitions(self):
        """
        Deselect all transitions
        """
        for trans in self.trans_selected:
            trans.selected = False
        self.trans_selected = []

    def keyPressEvent(self, event):
        """
        if delete pressed
        remove edge between selected nodes
        """
        if event.key() == QtCore.Qt.Key_Delete:
            self.delete_selected_states()

    def mouseDoubleClickEvent(self, event):
        """
        CHANGE TO OPEN WINDOW PARAMETERS
        Rename with double mouse click
        """
        self.select_elements(event)
        self.get
        self.StateParameters

    def mousePressEvent(self, event):
        """
        Click right button to chose items
        Click mid button to rename item chosen ( only 1 item chosen can be renamed)
        """

        if event.button() == QtCore.Qt.RightButton:
            self.select_elements(event)
            return
        if event.button() == QtCore.Qt.MidButton:
            self.rename()
            return
        QtWidgets.QGraphicsScene.mousePressEvent(self, event)

    def create_state(self):
        """
        Create new state , random place it on scene, add to states_list
        """
        state = State(self,"")
        self.addItem(state)
        state.setPos(randint(-50, 50), randint(-50, 50))
        self.states_list.append(state)
        self.update()
        print(2)
    def create_initial(self):
        """
        Make chosen states  initials
        """
        for state in self.state_selected:
            state.final = False
            state.initial = True
        self.deselect_states()
        self.update()
    def create_final(self):
        """
        Make chosen states  finals
        """
        for state in self.state_selected:
            state.initial = False
            state.final = True
        self.deselect_states()
        self.update()

    def select_elements(self, event):
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

    def create_transition(self):
        """
        Create transition between 2 chosen state. The first chosen one is source, the second is destination
        We can choose one state to create a transition towards itself.
        """
        trans_val, ok_pressed = QtWidgets.QInputDialog.getText(QtWidgets.QMainWindow(), 'Create Transition',
            'Enter Transition Name:')
        if ok_pressed:
            """ If 2 states are chosen, create a transition with a name between these. """
            if len(self.state_selected)== 2:
                """ Check if between 2 states there is already a transition """
                for trans in self.items():
                    if isinstance(trans, Transition):
                        if trans.source == self.state_selected[0] and trans.dest == self.state_selected[1]:
                            self.InvalidInMsg.setText('Transition already exists')
                            self.InvalidInMsg.exec_()
                            self.deselect_states()
                            return
                """ If there isn't, we create a new transition """
                self.addItem(Transition(self.state_selected[0],self.state_selected[1], trans_val))
                self.deselect_states()
                self.update()
            elif len(self.state_selected) == 1:
                """ if only 1 state is chosen, we create a self-transition of that state """
                self.addItem(SelfTransition(self.state_selected[0],trans_val))
                self.deselect_states()
                self.update()
            else:
                """ if we choose > 2 transition, we can not create a transition """
                self.InvalidInMsg.setText('Must select 2 states to create transition')
                self.InvalidInMsg.exec_()

    def delete_selected_states(self):
        """
        Delete chosen state and all transitions connect to it.
        """
        for state in self.state_selected:
            for i in range(len(state.link)):
                self.removeItem(state.link[i])
            self.removeItem(state)
        for state in self.selectedItems():
            # check on all selected items, if there are states then delete them.
            if isinstance(state,States):
                for i in range(len(state.link)):
                    self.removeItem(state.link[i])
                self.removeItem(state)
                state.setSelected(0)
        self.state_selected = []
        self.update()

    def delete_transition(self):
        """
        Delete chosen transitions.
        """
        # Firstly, on delete the transition in TransitionList of source state and dest state
        for transition in self.trans_selected:
            source = transition.source
            dest = transition.dest
            for trans in source.TransitionList:
                if trans == transition:
                    source.TransitionList.remove(transition)
            for trans in dest.TransitionList:
                if trans == transition:
                    dest.TransitionList.remove(transition)
            # then remove item from scene.
            self.removeItem(transition)
            #self.trans_list.remove(state)
        for transition in self.selectedItems():
            # check on all selected items, if there are states then delete them.
            if isinstance(transition,Transition) or isinstance(transition,SelfTransition):
                self.removeItem(transition)
                transition.setSelected(0)
        self.trans_selected = []
        self.update()

    def rename(self):
        new_val, ok = QtWidgets.QInputDialog.getText(QtWidgets.QMainWindow(), 'Rename state',
            'Enter new name of state or transition:')
        if ok:
            # if the entered champ is empty, we push an Invalid message
            if new_val == "":
                self.InvalidInMsg.setText('A state or transition must have a new name!')
                self.InvalidInMsg.exec_()
            else:
                # We only allow one transition or one state can be renamed each time
                if len(self.trans_selected) == 1:
                    for transition in self.trans_selected:
                        # Delete the transition and create a new one with new name
                        if type(transition) == Transition:
                            self.removeItem(transition)
                            self.addItem(Transition(self.trans_selected[0].source,self.trans_selected[0].dest, new_val))
                            self.trans_selected.clear()
                            self.deselect_transitions()
                            self.update()
                        else:
                            self.removeItem(transition)
                            self.addItem(selfTransition(self.trans_selected[0].source, new_val))
                            self.trans_selected.clear()
                            self.deselect_transitions()
                            self.update()
                elif len(self.state_selected) == 1:
                    flag = True
                    for state in self.state_selected:
                         # Delete the state and create a new one with new name
                        for item in self.items():
                            if isinstance(item,State):
                                if item.val == new_val:
                                    flag = False
                        if flag:
                            state.val=new_val
                            state.setPos(state.pos().x(),state.pos().y())
                            self.deselect_states()
                            self.state_selected.clear()
                            self.update()
                        else:
                            self.InvalidInMsg.setText('A state with this name exist')
                            self.InvalidInMsg.exec_()

                # If we choose plus than 2 items, we push an InvalidMsg
                else:
                    self.InvalidInMsg.setText('Only 1 state !')
                    self.InvalidInMsg.exec_()


    def reorganize(self,radius=150, s=0):
        """
        Reorganise chosen state as a form of a regular polygon
        """
        deplace = 800
        stateselected=[]
        for state in self.selectedItems():
            if isinstance(state,State):
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
        stateselected = []

