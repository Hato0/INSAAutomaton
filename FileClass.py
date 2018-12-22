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
        files.write("\\usepackage{tikz}\n \\usetikzlibrary{automata,arrows}\n \\begin{document}\n\n "
                    "\\begin{tikzpicture}")
        for item in StateClass.States.registry:
            if item.get_status() == 0:
                files.write("\n node[state, initial, shape = ")
                files.write(item.get_shape)
                files.write("draw = ")
                files.write(item.get_color)
                files.write("]   (")
                files.write(item.get_attributeletter())
                files.write(") at ")
                files.write(item.get_position())
                files.write(" {$")
                files.write(item.get_name())
                files.write("$};")
            elif item.get_status() == 1:
                files.write("\n node[state, shape = ")
                files.write(item.get_shape)
                files.write("draw = ")
                files.write(item.get_color)
                files.write("]   (")
                files.write(item.get_attributeletter())
                files.write(") at ")
                files.write(item.get_position())
                files.write("{$")
                files.write(item.get_name())
                files.write("$};")
            else:
                files.write("\n node[state, accepting, shape = ")
                files.write(item.get_shape)
                files.write("draw = ")
                files.write(item.get_color)
                files.write("]   (")
                files.write(item.get_attributeletter())
                files.write(") at ")
                files.write(item.get_position())
                files.write(" {$")
                files.write(item.get_name())
                files.write("$};")
        files.write("\\path  ")
        iterateurbis = 0
        for itemlink in StateClass.States.registry:
            a = itemlink.link
            for i in range(len(a)):
                if a[i] == itemlink.get_name():
                    files.write("(")
                    files.write(itemlink.get_attributeletter())
                    files.write(")     [loop]   node  {")
                    files.write(itemlink.link_name[iterateurbis])
                    files.write("}  (")
                    files.write(a[i])
                    files.write("\n")
                else:
                    files.write("(")
                    files.write(itemlink.get_attributeletter())
                    files.write(")     node  {")
                    files.write(itemlink.link_name[iterateurbis])
                    files.write("}  (")
                    files.write(a[i])
                    files.write("\n")
                iterateurbis += 1
        files.write("\\end{tikzpicture} \n \\end{document}")
        files.close()

    def save(self, header):
        """
        Set a safe to recover the user work
        :return: None
        """
        file = open(self.name, "w")
        print("a")
        file.write(header)
        print("b")
        for item in StateClass.States.registry:
            print("c")
            file.write("\\StateSafe \n")
            file.write(item.get_name())
            file.write(item.get_position())
            file.write(item.get_link())
            file.write(item.get_link_name())
            file.write(item.get_color())
            file.write(item.get_shape())
            file.write(item.get_attributeletter())
            file.write("\\EndStateSafe \n")
        print("d")
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
                        line = file.readline()
                        alpha[cursor].set_position(line)
                        line = file.readline()
                        linebis = file.readline()
                        alpha[cursor].add_link(line, linebis)
                        line = file.readline()
                        alpha[cursor].set_color(line)
                        line = file.readline()
                        alpha[cursor].set_shape(line)
                        line = file.readline()
                        alpha[cursor].set_attributeletter(line)
            line = file.readline()
        file.close()
