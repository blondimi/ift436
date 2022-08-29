def bellman_ford(G, p, s):
    V, _ = G

    d = {v: float("inf") for v in V}
    d[s] = 0

    for _ in range(len(V) - 1):
        for (u, v) in p:
            d[v] = min(d[v], d[u] + p[u, v])

    return d

if __name__ == "__main__":
    # Graphe des notes de cours
    V = ["a", "b", "c", "d", "e"]
    E = {"a": ["b", "e"],
         "b": ["c", "d"],
         "c": ["d"],
         "d": ["e"],
         "e": []}
    G = (V, E)

    p = {("a", "b"):  3,
         ("a", "e"):  2,
         ("b", "c"):  2,
         ("b", "d"):  1,
         ("c", "d"): -2,
         ("d", "e"): -2,}

    dist = bellman_ford(G, p, "a")

    # Afficher distances
    print(" ".join(V))
    print(" ".join(str(dist[v]) for v in V))
