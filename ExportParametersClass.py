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


class DiagramParameters:

    def __init__(self):
        """
        Initialisation of parameters by default
        """
        self.nodedistance = "2.8cm"

    def get_nodedistance(self):
        """

        :return: char
        Return distance between states for every nodes
        """
        return self.nodedistance

    def set_nodedistance(self, v):
        """

        :param v: char
        :return: char
        Change distance between states for every nodes
        """
        self.nodedistance = v


