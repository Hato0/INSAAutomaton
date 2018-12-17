import os.path


def postion(states):
    return 0


def matrice_adjacente(l, nbnoeud):
    matrice = []
    compteur = [0] * nbnoeud
    for i in range(len(l)):
        for j in range(3, len(l[i])):
            compteur[l[i, j]] += 1
        matrice.append(compteur)
    return matrice


def export(fichierbase, graphs):
    if os.path.isfile(fichierbase):
        return "Fichier déjà existant, \n Veuillez saisir un autre nom", export(input(), graphs)
    else:
        fichier = open(fichierbase, "w")
        fichier.write(
            "\\usepackage{tikz}\n \\usetikzlibrary{automata,arrows}\n \\begin{document}\n\n \\begin{tikzpicture}")
        for i in range(len(states)):
            if states[i, 0] == 0:
                fichier.write("\n node[state, accepting]  (", states[i, 1], ")", position(states[i, 2]), " {$",
                              states[i, 1], "$};")
            elif states[i, 1] == 1:
                fichier.write("\n node[state](", states[i, 1], ")", position(states[i, 2]), "{$", states[i, 1], "$};")
            else:
                fichier.write("\n node[initial, state, initial text = ]   (", states[i, 1], ")", "{$", states[i, 1],
                              "$};")
        fichier.write("\\path[->]")
        for i in relations:
            fichier.write()
        fichier.write("\\end{tikzpicture} \n \\end{document}")
        fichier.close()


def Import():
    list = os.listdir('Cible')
    print(list)
    input("Entrez le nom du fichier à importer", a);
    fichier = open(a, "r")


def optimation(matrice):
    if matrice == []:
        return 0
    else:
        max = 0
        intermax = 0
        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                if matrice[i, j] != 0:
                    intermax += matrice[i, j]

    liste_resultat_position = [matrice[i]]
