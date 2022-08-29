import sys; sys.path.append("../introduction/") # Hack pour accéder à l'intro
from monnaie import monnaie_mod

def monnaie_brute(m, s):
    # k   = montant qu'on doit encore rendre
    # num = nombre de pièces utilisées jusqu'ici
    # i   = indice de la pièce considérée
    def aux(k, num, i):
        if i == len(s):
            return num if k == 0 else float("inf")
        else:
            p = s[i]
            a = monnaie_brute(k, num, i + 1)
            b = monnaie_brute(k - p, num + 1, i) if k >= p else float("inf")

            return min(a, b)

    return aux(m, 0, 0)

def monnaie_dyn(m, s):
    # T[i][j] = nombre de pièces min. pour rendre j avec i premières pièces
    T = [[float("inf") for _ in range(m + 1)] for _ in range(len(s) + 1)]
    
    # Aucun pièce nécessaire pour rendre 0
    T[0][0] = 0

    # Calculer nombre de pièces en introduisant les pièces itérativement
    for i in range(1, len(s) + 1):
        for j in range(m + 1):
            p = s[i - 1]
            a = T[i - 1][j]
            b = T[i][j - p] + 1 if j >= p else float("inf")

            T[i][j] = min(a, b)
    
    return T[-1][-1]

def monnaie_dyn_econome(m, s):
    T = [float("inf") for _ in range(m + 1)]
    
    # Aucun pièce nécessaire pour rendre 0
    T[0] = 0

    # Calculer nombre de pièces en introduisant les pièces itérativement
    for i in range(len(s)):
        U = [float("inf") for _ in range(m + 1)]

        for j in range(m + 1):
            p = s[i - 1]
            a = T[j]
            b = U[j - p] + 1 if j >= p else float("inf")

            U[j] = min(a, b)

        T = U
    
    return T[-1]

# Exemples
if __name__ == "__main__":
    def exemple(ex, m, s):
        t = sorted(s, reverse=True)
        
        print(f"{ex}:")
        print()
        print(f" m = {m}")
        print(f" s = {s}")
        print()
        print("Nombre de pièces (prog. dynam.):   ", monnaie_dyn(m, s))
        print("Nombre de pièces (prog. dyn. éco.):", monnaie_dyn_econome(m, s))
        print("Nombre de pièces (force brute):    ", monnaie_dyn(m, s))
        print("Nombre de pièces (glouton):        ", monnaie_mod(t, m))

    exemple("Exemple du diaporama d'introduction",
            582, [1, 5, 10, 25, 100, 200])
    print()
    exemple("Exemple qui échoue avec l'algorithme glouton",
            10, [1, 5, 7])
    print()
    exemple("Exemple où l'on ne peut pas retourner la monnaie",
            43, [6, 9, 20])
