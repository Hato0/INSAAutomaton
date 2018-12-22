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


class States:
    registry = []

    def __init__(self):
        """
        Initialisation of States Object
        """
        self.registry.append(self)
        self.status = 1
        self.name = ""
        self.position_x = 0
        self.position_y = 0
        self.link = []
        self.color = ""
        self.shape = ""
        self.link_name = []
        self.attributeletter = ""

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

        self.status = v

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


pomme = States()
pomme.set_name("States1")
pomme.set_position_x(0)
pomme.set_position_y(1)
pomme.set_color("blue")
pomme.set_shape("circle")
pomme.set_attributeletter("A")
pomme.set_status(0)

apple = States()
apple.set_name("States2")
apple.set_position_x(1)
apple.set_position_y(3)
apple.set_color("red")
apple.set_shape("rectangle")
apple.set_attributeletter("B")
apple.set_status(2)


test = apple.get_attributeletter()
pomme.add_link(test)
pomme.add_link_name("test_link")
