from heapq               import heapify, heappop, heappush
from ensembles_disjoints import EnsemblesDisjoints

# Fonction auxiliaire qui retourne une paire non ordonnée
def arete(u, v):
    return frozenset({u, v})

def prim(G, p):
    V, E = G

    depart    = next(iter(V)) # Choisir un sommet de départ arbitaire
    candidats = [(p[e], e) for e in p if depart in e]
    marque    = {v: (v == depart) for v in V}
    arbre     = []

    heapify(candidats)
    
    while len(candidats) > 0:
        _, e = heappop(candidats)
        u, v = e

        # L'arête e relie l'arbre à un nouveau sommet?
        if marque[u] != marque[v]:
            arbre.append(e)

            # Identifier le nouveau sommet ajouté à l'arbre
            x = u if not marque[u] else v

            # Marquer nouveau sommet et ajouter les arêtes de son voisinage
            marque[x] = True

            for y in E[x]:
                e = arete(x, y)
                heappush(candidats, (p[e], e))
            
    return arbre

def kruskal(G, p):
    V, E = G

    aretes = sorted(list(p), key = lambda e: p[e]) # Trier arêtes selon poids
    foret  = EnsemblesDisjoints(V)
    arbre  = []

    for e in aretes:
        u, v = e
        
        if foret.trouver(u) != foret.trouver(v):
            foret.union(u, v)
            arbre.append(e)

    return arbre

# Exemple
if __name__ == "__main__":
    # Graphe des notes de cours
    V = {"a", "b", "c", "d", "e", "f", "g"}
    E = {"a": ["b", "c"],
         "b": ["a", "c", "d", "e"],
         "c": ["a", "b", "e"],
         "d": ["b", "e", "f"],
         "e": ["b", "c", "d", "g"],
         "f": ["d", "g"],
         "g": ["e", "f"]}
    G = (V, E)

    p = {arete("a", "b"): 2,
         arete("a", "c"): 3,
         arete("b", "c"): 4,
         arete("b", "d"): 2,
         arete("b", "e"): 1,
         arete("c", "e"): 1,
         arete("d", "e"): 3,
         arete("d", "f"): 5,
         arete("e", "g"): 4,
         arete("f", "g"): 2}

    # Algorithme de Prim
    arbre = prim(G, p)

    print("Algorithme de Prim:")
    print(" Arbre:", list(map(tuple, arbre)))
    print(" Poids:", sum(p[e] for e in arbre))
    print()

    # Algorithme de Kruskal
    arbre = kruskal(G, p)

    print("Algorithme de Kruskal:")
    print(" Arbre:", list(map(tuple, arbre)))
    print(" Poids:", sum(p[e] for e in arbre))
