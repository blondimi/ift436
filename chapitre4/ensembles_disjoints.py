class EnsemblesDisjoints:
    def __init__(self, elements):
        self.parent  = {x: x for x in elements}
        self.hauteur = {x: 0 for x in elements}

    def trouver(self, x):
        r = x

        # Recherche de la racine
        while r != self.parent[r]:
            r = self.parent[r]

        # # Compression du chemin de x vers r (facultatif)
        # while x != r:
        #     x, self.parent[x] = self.parent[x], r

        return r

    def union(self, x, y):
        x = self.trouver(x)
        y = self.trouver(y)
        
        if self.hauteur[x] > self.hauteur[y]:
            self.parent[y] = x
        elif self.hauteur[y] > self.hauteur[x]:
            self.parent[x] = y
        else:
            self.parent[y]   = x
            self.hauteur[x] += 1
