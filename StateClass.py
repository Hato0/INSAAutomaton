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


class States:
    registry = []

    def __init__(self):
        """
        Initialisation of States Object
        """
        self.registry.append(self)
        self.status = 0
        self.name = ""
        self.position = (0, 0)
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

    def get_position(self):
        """

        :return: Tuple
        Return states position
        """
        return self.position

    def set_position(self, v):
        """

        :param v: Tuple
        :return: None
        Change states position
        """
        self.position = v

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

    def add_link(self, v, n):
        """

        :param v: char
        :return: None
        Add link with an other states
        """
        self.link.append(v)
        self.link_name.append(n)

    def enlimination_link(self, v):
        """
        :param v: char
        :return:  Supress a link for the current states
        """
        self.link.remove(v)
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
chaud = States()
pomme.set_name("bonjour")
pomme.set_status(0)
chaud.set_name("rahhhhh")
chaud.add_link("bonjour", "rat")
for i in States.registry:
    print(i.name)
    print(i.status)
    print(i.get_name())
    print(i.get_link())
    print(i.get_link_name())
