def dijkstra(G, p, s):
    V, E = G

    candidats = set(V)
    dist = {v: float("inf") for v in V}
    pred = {v: None         for v in V}

    def plus_petit(): # À remplacer par une implémentation efficace, par ex.
        v = None      #                              un monceau de Fibonacci
        
        for u in candidats:
            if v is None or dist[u] < dist[v]:
                v = u

        return v

    dist[s] = 0
    suivant = s

    while suivant is not None:
        for voisin in E[suivant]:
            if voisin in candidats:
                longueur = p[suivant, voisin]

                if dist[voisin] > dist[suivant] + longueur:
                    dist[voisin] = dist[suivant] + longueur
                    pred[voisin] = suivant

        candidats.remove(suivant)
        
        suivant = plus_petit()

    return (dist, pred)

# Exemple
if __name__ == "__main__":
    # Graphe des notes de cours
    V = ["a", "b", "c", "d", "e", "f"]
    E = {"a": ["b", "c"],
         "b": ["a", "c", "d", "e"],
         "c": ["a", "b", "e"],
         "d": ["b", "e", "f"],
         "e": ["b", "c", "d", "f"],
         "f": ["d", "e"]}
    G = (V, E)

    p = {("a", "b"): 3, ("b", "a"): 3,
         ("a", "c"): 1, ("c", "a"): 1,
         ("b", "c"): 5, ("c", "b"): 5,
         ("b", "d"): 2, ("d", "b"): 2,
         ("b", "e"): 3, ("e", "b"): 3,
         ("c", "e"): 7, ("e", "c"): 7,
         ("d", "e"): 1, ("e", "d"): 1,
         ("d", "f"): 3, ("f", "d"): 3,
         ("e", "f"): 7, ("f", "e"): 7}

    dist, pred = dijkstra(G, p, "a")
    
    # Afficher distances
    print("Distances:")
    print(" ".join(V))
    print(" ".join(str(dist[v]) for v in V))
    print()
    
    # Afficher prédecesseurs
    print("Prédecesseurs:")
    print(" ".join(V))
    print(" ".join(str(pred[v]) if pred[v] is not None else "-" for v in V))
