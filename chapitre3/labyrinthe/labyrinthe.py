from collections import deque
from enum        import Enum
from random      import shuffle

class Dir(Enum):
    HAUT   = (-1,  0)
    DROITE =  (0,  1)
    BAS    =  (1,  0)
    GAUCHE =  (0, -1)

    def __radd__(self, pos):
        return (pos[0] + self.value[0], pos[1] + self.value[1])

    def __rmul__(self, coeff):
        return (coeff  * self.value[0], coeff  * self.value[1])

    def reflexion(self):
        return Dir(-1 * self)

    def inverse(self):
        return Dir((self.value[1], self.value[0]))
    
class Grille:
    def __init__(self, hauteur, largeur):
        self.hauteur = hauteur
        self.largeur = largeur
        self.cases   = {(i, j): set() for i in range(hauteur)
                                      for j in range(largeur)}

    def contient(self, pos):
        return (0 <= pos[0] < self.hauteur) and (0 <= pos[1] < self.largeur)

    def voisins(self, pos):
        return [pos + d for d in self.cases[pos] if self.contient(pos + d)]

def generer_labyrinthe(largeur, hauteur):
    depart = (0, 0)

    # Parcours en profondeur
    grille     = Grille(largeur, hauteur)
    directions = list(Dir)
    visite     = set()

    def gen(u):
        visite.add(u)

        shuffle(directions)
            
        for d in directions:
            v = u + d

            if grille.contient(v) and v not in visite:
                gen(v)

                grille.cases[u].add(d)
                grille.cases[v].add(d.reflexion())

    gen(depart)

    return grille

def trouver_chemin(grille):
    depart = (0, 0)
    cible  = (grille.hauteur - 1, grille.largeur - 1)

    # Parcours en largeur de la grille
    candidats = deque([depart])
    visite    = {depart: None}
    termine   = False

    while len(candidats) > 0 and not termine:
        u = candidats.popleft()

        for v in grille.voisins(u):
            if v not in visite:
                visite[v] = u

                if v == cible:
                    termine = True
                    break
                else:
                    candidats.append(v)

    # Reconstruire le chemin
    sommet = cible
    chemin = [sommet]

    while visite[sommet] is not None:
        chemin.append(visite[sommet])
        sommet = visite[sommet]
   
    return chemin
