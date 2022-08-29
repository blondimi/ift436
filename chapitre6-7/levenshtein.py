def dist(u, v):
    m = len(u)
    n = len(v)
    T = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        T[i][0] = i

    for j in range(1, n + 1):
        T[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            c = 1 if u[i - 1] != v[j - 1] else 0

            T[i][j] = min(T[i - 1][j]     + 1, # Suppression
                          T[i][j - 1]     + 1, # Insertion
                          T[i - 1][j - 1] + c) # Modification
    
    return T[-1][-1]

# Exemples
if __name__ == "__main__":
    def exemple(u, v):
        print(f"dist({u}, {v}) =", dist(u, v))

    exemple("ab",  "ac")
    exemple("abc", "ba")
    exemple("",    "ab")
    exemple("bonjour!", "bnjouur1!")
