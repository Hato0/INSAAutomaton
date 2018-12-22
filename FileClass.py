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

import StateClass


class FilesBlock:

    def __init__(self):
        """
        Initilisation of file
        """
        self.name = ""

    def get_name(self):
        """
        Return file name
        :return: char
        """
        return self.name

    def set_name(self, v):
        """
        Change file name
        :param v: char
        :return: None
        """
        self.name = v

    def export(self):
        """
        Open or create a file to export the automaton on Latex/Tikz
        :return: None
        """
        """
        Write the Latex/Tikz code on the file realated to the current automaton
        """
        files = open(self.name, "w")
        files.write("\\usepackage{tikz}\n\\usetikzlibrary{automata,arrows}\n\\begin{document}\n\n"
                    "\\begin{tikzpicture}")
        for item in StateClass.States.registry:
            name = item.get_name()
            shape = item.get_shape()
            color = item.get_color()
            attributeletter = item.get_attributeletter()
            position_x = item.get_position_x()
            position_y = item.get_position_y()
            if item.get_status() == 0:
                files.write("\nnode[state, initial, shape = ")
                files.write(shape)
                files.write(", draw = ")
                files.write(color)
                files.write("]   (")
                files.write(attributeletter)
                files.write(") at (")
                files.write(str(position_x))
                files.write(" , ")
                files.write(str(position_y))
                files.write(") {$")
                files.write(name)
                files.write("$};")
            elif item.get_status() == 1:
                files.write("\nnode[state, shape = ")
                files.write(shape)
                files.write(", draw = ")
                files.write(color)
                files.write("]   (")
                files.write(attributeletter)
                files.write(") at (")
                files.write(str(position_x))
                files.write(" , ")
                files.write(str(position_y))
                files.write(") {$")
                files.write(name)
                files.write("$};")
            else:
                files.write("\nnode[state, accepting, shape = ")
                files.write(shape)
                files.write(", draw = ")
                files.write(color)
                files.write("]   (")
                files.write(attributeletter)
                files.write(") at (")
                files.write(str(position_x))
                files.write(" , ")
                files.write(str(position_y))
                files.write(") {$")
                files.write(name)
                files.write("$};")
        files.write("\n\n\\path  ")
        iterateurbis = 0
        for itemlink in StateClass.States.registry:
            a = itemlink.link
            for i in range(len(a)):
                attributeletter = itemlink.get_attributeletter()
                link_name = itemlink.get_link_name()
                if a[i] == itemlink.get_name():
                    files.write("(")
                    files.write(attributeletter)
                    files.write(") edge [loop]   node  {")
                    files.write(link_name[iterateurbis])
                    files.write("}  (")
                    files.write(a[i])
                    files.write(")")
                    files.write("\n")
                else:
                    files.write("(")
                    files.write(attributeletter)
                    files.write(") edge          node  {")
                    files.write(link_name[iterateurbis])
                    files.write("}  (")
                    files.write(a[i])
                    files.write(")")
                    files.write("\n")
                iterateurbis += 1
        files.write("\\end{tikzpicture} \n\\end{document}")
        files.close()

    def save(self, header):
        """
        Set a safe to recover the user work
        :return: None
        """
        file = open(self.name, "w")
        file.write(header)
        file.write("\n")
        for item in StateClass.States.registry:
            file.write("\\StateSafe \n")
            file.write(item.get_name())
            file.write("\n")
            file.write(str(item.get_position_x()))
            file.write("\n")
            file.write(str(item.get_position_y()))
            file.write("\n")
            file.write(str(len(item.get_link())))
            file.write("\n")
            a = item.get_link()
            for i in a:
                file.write(str(i))
                file.write("\n")
            file.write("end_link_list")
            file.write("\n")
            b = item.get_link_name()
            for i in b:
                file.write(str(i))
                file.write("\n")
            file.write("end_link_name_list")
            file.write("\n")
            file.write(item.get_color())
            file.write("\n")
            file.write(item.get_shape())
            file.write("\n")
            file.write(item.get_attributeletter())
            file.write("\n")
            file.write("\\EndStateSafe \n")
        file.close()

    def importation(self):
        """
        Initialise state with existing file
        :return: None
        """
        alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        cursor = 0
        file = open(self.name, 'r')
        line = file.readline()
        while line != "":
            if line == "\\StateSafe \n":
                    alpha[cursor] = StateClass.States()
                    while line != "\\EndStateSafe \n":
                        line = file.readline()
                        alpha[cursor].set_name(line)
                        file.readline()
                        line = file.readline()
                        alpha[cursor].set_position_x(int(line))
                        file.readline()
                        line = file.readline()
                        alpha[cursor].set_position_y(int(line))
                        file.readline()
                        range_iter = int(file.readline())
                        for i in range(range_iter):
                            file.readline()
                            line = file.readline()
                            alpha[cursor].add_link(line)
                        for i in range(range_iter):
                            file.readline()
                            line = file.readline()
                            alpha[cursor].add_link_name(line)
                        file.readline()
                        line = file.readline()
                        alpha[cursor].set_color(line)
                        file.readline()
                        line = file.readline()
                        alpha[cursor].set_shape(line)
                        file.readline()
                        line = file.readline()
                        alpha[cursor].set_attributeletter(line)
            file.readline()
            line = file.readline()
            cursor += 1
        file.close()
