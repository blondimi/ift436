def souschaine_contigue(u, v):
    def prefixe(i, j):
        p = ""
        
        while i < len(u) and j < len(v) and u[i] == v[j]:
            p += u[i]
            i += 1
            j += 1

        return p

    # Identifier le plus long préfixe commun de tous les suffixes
    s = ""

    for i in range(len(u)):
        for j in range(len(v)):
            s_ = prefixe(i, j)

            if len(s_) > len(s):
                s = s_

    return s

def souschaine(u, v):
    # Tester toutes les sous-chaînes de u et v
    def aux(x, y, i, j):
        if i < len(u):
            a = aux(x + u[i], y, i + 1, j)
            b = aux(x,        y, i + 1, j)

            return a if len(a) >= len(b) else b
        elif j < len(v):
            a = aux(x, y + v[j], i, j + 1)
            b = aux(x, y,        i, j + 1)

            return a if len(a) >= len(b) else b
        else:
            return x if x == y else ""

    return aux("", "", 0, 0)

def souschaine_contigue_dyn(u, v):
    T = [[0 for _ in range(len(v) + 1)] for _ in range(len(u) + 1)]
    i_max = j_max = 0

    for i in range(1, len(u) + 1):
        for j in range(1, len(v) + 1):
            a = u[i - 1]
            b = v[j - 1]

            if a == b:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = 0

            if T[i][j] > T[i_max][j_max]:
                i_max, j_max = i, j

    # Reconstruire la sous-chaîne max.
    i, j = i_max, j_max
    s = ""

    while T[i][j] > 0:
        s = u[i - 1] + s
        i -= 1
        j -= 1

    return s

def souschaine_dyn(u, v):
    T = [[0 for _ in range(len(v) + 1)] for _ in range(len(u) + 1)]

    for i in range(1, len(u) + 1):
        for j in range(1, len(v) + 1):
            if u[i - 1] == v[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])

    # Reconstruire la sous-chaîne max.
    i, j = len(u), len(v)
    s = ""

    while T[i][j] > 0:
        if u[i - 1] == v[j - 1]:
            s = u[i - 1] + s
            i -= 1
            j -= 1
        elif T[i - 1][j] >= T[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return s

# Exemple des notes de cours
if __name__ == "__main__":
    u = "abcaba"
    v = "abaccab"
    
    print("Sous-chaîne contiguë max. (force brute):",
          souschaine_contigue(u, v))
    print("Sous-chaîne contiguë max. (prog. dyn.): ",
          souschaine_contigue_dyn(u, v))
    print()
    print("Sous-chaîne max. (force brute):", souschaine(u, v))
    print("Sous-chaîne max. (prog. dyn.): ", souschaine_dyn(u, v))
