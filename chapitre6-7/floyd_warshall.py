def floyd_warshall(G, p):
    V, _ = G
    d = {(u, v): float("inf") for u in V for v in V}

    for v in V:
        d[v, v] = 0

    for (u, v) in p:
        d[u, v] = p[u, v]

    for k in V:
        for i in V:
            for j in V:
                d[i, j] = min(d[i, j], d[i, k] + d[k, j])

    return d

if __name__ == "__main__":
    # Graphe des notes de cours
    V = ["v1", "v2", "v3", "v4"]
    E = {"v1": ["v2", "v4"],
         "v2": ["v4"],
         "v3": ["v2"],
         "v4": ["v1", "v3"]}
    G = (V, E)

    p = {("v1", "v2"): 2,
         ("v1", "v4"): 5,
         ("v2", "v4"): 1,
         ("v3", "v2"): 3,
         ("v4", "v1"): 4,
         ("v4", "v3"): 2}

    dist = floyd_warshall(G, p)

    # Afficher distances
    print("  ", " ".join(V))

    for u in V:
        print(u, " ".join("{0:2}".format(dist[u, v]) for v in V))
        
