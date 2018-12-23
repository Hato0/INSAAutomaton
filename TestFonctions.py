#  Copyright (C) 2018 Thibaut Lompech - All Rights Reserved
#  You may use, distribute and modify this code under the
#  terms of the legal license, which unfortunately won't be
#  written for another century.
#
#  You should have received a copy of the legal license with
#  this file. If not, please write to: thibaut.lompech@insa-cvl.fr
#

def __init__(self):
    super().__init__()
    self.width = 5000
    self.height = 4000
    self.margin = 10

    self.keys = {
        Qt.Key_W: False,
        Qt.Key_A: False,
        Qt.Key_S: False,
        Qt.Key_D: False,
    }  # This will be modified by View, and be read by GuiClient
    self.mouseDown = False
    self.mousePos = QPoint()
    self.decaying = []
    self.setSceneRect(5, 5, self.width, self.height)
    self.polygons = ObjectTracker()
    self.heroes = ObjectTracker()
    self.bullets = ObjectTracker()
    self.experienceBar = ExperienceBar()
    self.addItem(self.experienceBar)
    self.scoreboard = Scoreboard()
    self.addItem(self.scoreboard)

    Qt