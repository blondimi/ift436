from random import randrange

def arete(u, v):
    return frozenset({u, v})

def karger(adj):
    V = set(adj)
    E = list({arete(u, v) for u in adj for v in adj[u]})
        
    while len(V) > 2:
        u, v = E.pop(randrange(len(E)))
        w    = u + v

        V.remove(u)
        V.remove(v)
        V.add(w)

        E_ = []

        for (x, y) in E:
            x = w if x in {u, v} else x
            y = w if y in {u, v} else y

            if x != y:
                E_.append(arete(x, y))

        E = E_

    return len(E)

def karger_amplifie(adj):
    coupe_min = float("inf")

    for _ in range(len(adj)**2):
        coupe_min = min(coupe_min, karger(adj))

    return coupe_min

if __name__ == "__main__":
    def echantillonner(adj, f):
        num_essais = 1000
        distrib    = {}

        for _ in range(num_essais):
            c = f(adj)

            distrib[c] = distrib.get(c, 0) + 1

        for c in sorted(distrib):
            print("{}: {}%".format(c, 100.0 * distrib[c] / num_essais))

    def tester(adj):
        print("Sans amplification:")
        echantillonner(adj, karger)
        print()
        print("Avec amplification:")
        echantillonner(adj, karger_amplifie)
        

    adj = {"a": ["b", "c", "d"],
           "b": ["a", "e", "c", "d"],
           "c": ["a", "b", "d", "e"],
           "d": ["a", "b", "c"],
           "e": ["b", "c"]}

    print("Graphe des notes de cours")
    tester(adj)
    print()
    
    adj = {"a": ["b", "c", "d", "i"],
           "b": ["a", "d", "e", "g", "i"],
           "c": ["a", "d", "f", "i"],
           "d": ["a", "b", "c", "e", "f", "h", "i"],
           "e": ["b", "d", "f", "g", "h"],
           "f": ["c", "d", "e", "g", "h"],
           "g": ["b", "e", "f", "h"],
           "h": ["d", "e", "f", "g"],
           "i": ["a", "b", "c", "d"]}

    print("Autre exemple")
    tester(adj)
