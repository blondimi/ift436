from collections import deque
from hanoi       import hanoi

def latex(piles, n):    
    # Générer tiges
    base    = 7
    hauteur = 4
    ecart   = 4
    
    tiges  = ["\\draw[black] (5, 0)  -- (25, 0);"]
    tiges += [("\\draw[line width=6pt, gray!25] "
               "({0}, -1/4) -- ({0}, {1});").format(base + i * ecart, hauteur)
               for i in range(len(piles))]

    # Générer disques
    disques = []
    
    for i in range(len(piles)):
        k = len(piles[i])
        
        for j in range(k):
            couleur   = "col{}".format(piles[i][j])
            epaisseur = 12 * hauteur / n
            largeur   = (ecart / 8) + ((ecart / 4) / n * piles[i][j])
            coord0    = (base + ecart * i - largeur, hauteur / n * (k - j - 1))
            coord1    = (base + ecart * i + largeur, hauteur / n * (k - j - 1))

            disques.append(("\draw[{}, line width={}pt]"
                            "({}, {}) -- ({}, {});").format(couleur, epaisseur,
                                                            *coord0, *coord1))

    return "\n".join(["\\begin{frame}",
                      "  \\begin{center}",
                      "    \\hspace*{-20pt}",
                      "    \\begin{tikzpicture}[line width=15pt]",
                      "      \n".join(tiges),
                      "      \n".join(disques),
                      "    \\end{tikzpicture}",
                      "  \\end{center}",
                      "\\end{frame}"])

def exporter(n):
    # Générer couleurs
    rouge    = lambda i: 1 if n <= 1 else (i / (n - 1)) - 1 / (n - 1)
    couleurs = [("\\definecolor{{col{}}}{{rgb}}"
                 "{{{} ,0, {}}}").format(i, rouge(i), 1 - rouge(i))
                for i in range(1, n + 1)]

    # Générer figures
    piles    = (deque(range(1, n + 1)), deque(), deque())
    solution = hanoi(tuple(map(deque, piles)))
    figures  = [latex(piles, n)]

    for (i, j) in solution:
        piles[j].appendleft(piles[i].popleft())

        figures.append(latex(piles, n))
    
    return "\n".join(["\\documentclass{beamer}",
                      "\\setbeamertemplate{navigation symbols}{}",
                      "\\setbeamercolor{background canvas}{bg=black}",
                      "\\usepackage{tikz}",
                      "\n".join(couleurs),
                      "",
                      "\\begin{document}",
                      "  \n".join(figures),
                      "\\end{document}"])

if __name__ == "__main__":
    num_disques = 3
    
    print(exporter(num_disques))
