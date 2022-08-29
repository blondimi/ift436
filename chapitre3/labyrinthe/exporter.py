from labyrinthe import generer_labyrinthe, trouver_chemin, Dir

def pos(v):
    return (v[1], -v[0])

def dessiner_grille(grille):
    def somme(*points):
        return (sum(v[0] for v in points),
                sum(v[1] for v in points))

    def ligne(v, d):
        x = somme(v, 0.5 * d,  0.5 * d.inverse())
        y = somme(v, 0.5 * d, -0.5 * d.inverse())

        return "\\draw[thick] {} -- {};".format(pos(x), pos(y))

    def case(v):
        return "\n".join([ligne(v, d) for d in set(Dir) - grille.cases[v]])

    return "\n".join(map(case, grille.cases))

def dessiner_chemin(chemin):
    depart = chemin[0]
    cible  = chemin[-1]
    cercle = lambda p: "\\fill[draw, red] {} circle (7pt);".format(p)
    
    return "\n".join([cercle(pos(depart)),
                      "\\draw[red, line width=4pt]",
                      " -- ".join(map(str, map(pos, chemin))) + ";",
                      cercle(pos(cible))])

def exporter(grille, chemin):
    return "\n".join(["\\documentclass{standalone}",
                      "\\usepackage{tikz}",
                      "",
                      "\\begin{document}",
                      "  \\begin{tikzpicture}",
                      "    %% Labyrinthe", dessiner_grille(grille),
                      "    %% Chemin",     dessiner_chemin(chemin),
                      "  \\end{tikzpicture}",
                      "\\end{document}"])

# Exemple
if __name__ == "__main__":
    hauteur = 20
    largeur = 30

    grille = generer_labyrinthe(hauteur, largeur)
    chemin = trouver_chemin(grille)

    print(exporter(grille, chemin))
