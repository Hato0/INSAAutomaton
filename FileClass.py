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

import os.path

import StateClass


class FilesBlock:

    def __init__(self):
        """
        Initilisation of file
        """
        self.name = ""
        self.accesspath = ""

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

    def get_accesspath(self):
        """
        Return path access for the file
        :return: char
        """
        return self.accesspath

    def set_accesspath(self, v):
        """
        Change path access for the file
        :param v:
        :return:
        """
        self.accesspath = v

    def export(self):
        """
        Open or create a file to export the automaton on Latex/Tikz
        :return: None
        """
        if os.path.isfile(self.name):
            """
            Check if file name already exist
            """
            print("Fichier déjà existant, \n Veuillez saisir un autre nom")
            newfile = input()
            FilesBlock.set_name(self, newfile)
            return FilesBlock.export(self)
        else:
            """
            Write the Latex/Tikz code on the file realated to the current automaton
            """
            files = open(self.name, "w")
            files.write("\\usepackage{tikz}\n \\usetikzlibrary{automata,arrows}\n \\begin{document}\n\n "
                        "\\begin{tikzpicture}")
            for item in StateClass.States.registry:
                if item.get_status() == 0:
                    files.write("\n node[state, initial]  (")
                    files.write(item.get_attributeletter())
                    files.write(")")
                    files.write(item.get_position())
                    files.write(" {$")
                    files.write(item.get_name())
                    files.write("$};")
                elif item.get_status() == 1:
                    files.write("\n node[state](")
                    files.write(item.get_attributeletter())
                    files.write(")")
                    files.write(item.get_position())
                    files.write("{$")
                    files.write(item.get_name())
                    files.write("$};")
                else:
                    files.write("\n node[state, accepting]   (")
                    files.write(item.get_attributeletter())
                    files.write(")")
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
                    else:
                        files.write("(")
                        files.write(itemlink.get_attributeletter())
                        files.write(")     node  {")
                        files.write(itemlink.link_name[iterateurbis])
                        files.write("}  (")
                        files.write(a[i])
                    iterateurbis += 1
            files.write("\\end{tikzpicture} \n \\end{document}")
            files.close()

"afdsfsdfsdfsdfsdfsd"
    """def __iimport(a):
        list = os.listdir('Cible')
    
        print(list)
        input("Entrez le nom du fichier à importer",a);
        fichier = open(a,"r")
        
    def __sauvegarde(self):
        if os.path.isfile(nomfichier):
            return "Fichier déjà existant, \n Veuillez saisir un autre nom", __sauvegarde(inpout())
        else:
            fichier = open (nomfichier,"w")
            fichier.write("")
    """