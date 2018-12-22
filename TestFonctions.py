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

import os.path

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
        if not os.path.isfile(self.name):
            print("File not found, \n Please correct the file name(Type a new name) "
                  "or overwrite the existing file (Type Y)")
            newfile = input()
            if newfile != "Y":
                FilesBlock.set_name(self, newfile)
                return FilesBlock.save(self)
            else:
                pass
        else:
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

    def save(self):
        """
        Set a safe to recover the user work
        :return: None
        """
        if os.path.isfile(self.name):
            print("File not found, \n Please correct the file name(Type a new name) "
                  "or overwrite the existing file (Type Y)")
            newfile = input()
            if newfile != "Y":
                FilesBlock.set_name(self, newfile)
                return FilesBlock.save(self)
            else:
                pass
        else:
            fichier = open(self.name, "w")
            a = input("Set a header")
            fichier.write(a)
            for item in StateClass.States.registry:
                fichier.write("\\StateSafe \n")
                fichier.write(item.get_name())
                fichier.write(item.get_position())
                fichier.write(item.get_link())
                fichier.write(item.get_link_name())
                fichier.write(item.get_color())
                fichier.write(item.get_shape())
                fichier.write(item.get_attributeletter())
                fichier.write("\\EndStateSafe \n")
            fichier.close()

    def importation(self):
        """
        Initialise state with existing file
        :return: None
        """
        if not os.path.isfile(self.name):
            print("File not found, \n Please correct the file name or correct path")
            newfile = input()
            FilesBlock.set_name(self, newfile)
            return FilesBlock.save(self)
        else:
            alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            cursor = 0
            fichier = open(self.name,'r')
            line = fichier.readline()
            while line != "":
                if line == "\\StateSafe \n":
                        alpha[cursor] = StateClass.States()
                        while line != "\\EndStateSafe \n":
                            line = fichier.readline()
                            alpha[cursor].set_name(line)
                            line = fichier.readline()
                            alpha[cursor].set_position(line)
                            line = fichier.readline()
                            linebis = fichier.readline()
                            alpha[cursor].add_link(line, linebis)
                            line = fichier.readline()
                            alpha[cursor].set_color(line)
                            line = fichier.readline()
                            alpha[cursor].set_shape(line)
                            line = fichier.readline()
                            alpha[cursor].set_attributeletter(line)
                line = fichier.readline()
            fichier.close()