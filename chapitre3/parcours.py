from collections import deque

def parcours_profondeur_rec(G, v):
    V, E = G
    visite  = set()
    sommets = []

    def parcours(u):
        if u not in visite:
            visite.add(u)

            for v in E[u]:
                parcours(v)

            sommets.append(u)

    parcours(v)

    return sommets

def parcours_profondeur_iter(G, v):
    V, E = G
    visite    = set()
    candidats = [v]
    sommets   = []

    while len(candidats) > 0:
        u = candidats.pop()

        if u not in visite:
            visite.add(u)
            sommets.append(u)

            for v in E[u]:
                candidats.append(v)

    sommets.reverse()
    
    return sommets

def parcours_largeur(G, v):
    V, E = G

    visite    = set()
    candidats = deque(v)
    sommets   = []

    while len(candidats) > 0:
        u = candidats.popleft()

        if u not in visite:
            visite.add(u)
            sommets.append(u)

            for v in E[u]:
                candidats.append(v)

    return sommets

def est_acyclique(G):
    V, E = G

    visite   = set()
    sur_pile = set()

    def cycle(u):
        if u in sur_pile:
            return True
        elif u not in visite:
            visite.add(u)
            sur_pile.add(u)
            
            for v in E[u]:
                if cycle(v):
                    return True

            sur_pile.remove(u)

        return False

    for v in V:
        if cycle(v):
            return False

    return True

# Exemples
if __name__ == "__main__":
    V = {"a", "b", "c", "d", "e"}
    E = {"a": ["b"],
         "b": ["c"],
         "c": ["a", "d"],
         "d": ["b", "c", "e"],
         "e": []}
    G = (V, E)

    print("Parcours en profondeur:", parcours_profondeur_rec(G, "a"))
    print("Parcours en profondeur:", parcours_profondeur_iter(G, "a"))
    print("Parcours en largeur:   ", parcours_largeur(G, "a"))
    print("Graphe acyclique?      ", "Oui" if est_acyclique(G) else "Non")
