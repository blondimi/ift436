from enum import Enum

class Couleur(Enum):
    AUCUNE = None
    NOIR   = False
    ROUGE  = True

    def inverse(self):
        return Couleur(not self.value)

def est_biparti(G):
    V, E = G

    couleur = {v: Couleur.AUCUNE for v in V}
    biparti = True

    def colorier(u, c):
        if couleur[u] is Couleur.AUCUNE:
            couleur[u] = c

            for v in E[u]:
                colorier(v, Couleur.inverse(c))
        elif couleur[u] != c:
            nonlocal biparti
            biparti = False

    for v in V:
        if couleur[v] is Couleur.AUCUNE:
            colorier(v, Couleur.ROUGE)

    return biparti

# Exemples
if __name__ == "__main__":
    # Graphes cycliques
    def C(n):
        V = set(range(n))
        E = {v: [(v - 1) % n, (v + 1) % n] for v in V}

        return (V, E)
    
    print("C_4:", est_biparti(C(4)))
    print("C_5:", est_biparti(C(5)))
    print("C_6:", est_biparti(C(6)))

    # Graphe sous forme de «maison» (non biparti)
    V = {0, 1, 2, 3, 4}
    E = {0: [1, 4],
         1: [0, 2],
         2: [1, 3, 4],
         3: [2, 4],
         4: [0, 2, 3]}
    G = (V, E)

    print("G:  ", est_biparti(G))

    # Autre graphe (biparti)
    V = {0, 1, 2, 3, 4, 5, 6}
    E = {0: [1, 2, 3],
         1: [0, 4, 6],
         2: [0, 4],
         3: [0, 4],
         4: [1, 2, 3, 5],
         5: [4, 6],
         6: [1, 5]}
    H = (V, E)

    print("H:  ", est_biparti(H))
