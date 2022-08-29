from random import choice, shuffle
from timeit import repeat

def maj_simple(T):
    n = len(T)

    for i in range(n):
        c = 0

        for j in range(n):
            if T[j] == T[i]:
                c += 1

        if c  > n // 2:
            return T[i]

    return None


def maj_sansrep(T):
    n = len(T)
    T = list(T)

    for i in range(n):
        if T[i] != None:
            c = 0
            x = T[i]

            for j in range(i, n):
                if T[j] == x:
                    c += 1
                    T[j] = None

            if c > n // 2: return x
                    
    return None


def maj_boyermoore(T):
    n = len(T)

    # Phase 1
    x, c = None, 0

    for i in range(n):
        if c == 0:
            x = T[i]
            c = 1
        elif T[i] == x:
            c += 1
        else:
            c -= 1

    # Phase 2
    c = 0

    for i in range(n):
        if T[i] == x:
            c += 1

    return x if c > n // 2 else None

# Exemples
if __name__ == "__main__":
    # Premier exemple des notes de cours
    T = ["a", "b", "b", "a", "a", "a", "c", "a"]

    print("Majorité de T =", T)
    print(" maj_simple:    ", maj_simple(T))
    print(" maj_sansrep:   ", maj_sansrep(T))
    print(" maj_boyermoore:", maj_boyermoore(T))
    print()

    # Deuxième exemple des notes de cours
    T = ["a", "b", "a", "b", "c"]

    print("Majorité de T =", T)
    print(" maj_simple:    ", maj_simple(T))
    print(" maj_sansrep:   ", maj_sansrep(T))
    print(" maj_boyermoore:", maj_boyermoore(T))
    print()

    # Exemple aléatoire de 15 éléments parmi {a, b}
    T = [choice(["a", "b"]) for _ in range(10)]

    print("Majorité de T =", T)
    print(" maj_simple:    ", maj_simple(T))
    print(" maj_sansrep:   ", maj_sansrep(T))
    print(" maj_boyermoore:", maj_boyermoore(T))
    print()

    # Exemple de grande taille avec une valeur majoritaire
    n = 10000
    T = [choice(["a", "b", "c"]) for _ in range(n)]

    print("Majorité d'une séquence aléatoire "
          "de {} éléments parmi {{a, b, c}}...".format(n))

    a = min(repeat(lambda:     maj_simple(T), number=1, repeat=3))
    b = min(repeat(lambda:    maj_sansrep(T), number=1, repeat=3))
    c = min(repeat(lambda: maj_boyermoore(T), number=1, repeat=3))

    print("Temps d'exécution:")
    print()
    print(" maj_simple:     {:15.10f} secs.".format(a))
    print(" maj_sansrep:    {:15.10f} secs.".format(b))
    print(" maj_boyermoore: {:15.10f} secs.".format(c))
    print()

    # Exemple de très grande taille avec une valeur majoritaire
    n = 1000000
    T = [choice(["a", "b", "c", "d", "e"]) for _ in range(n)]

    print("Majorité d'une séquence aléatoire "
          "de {} éléments parmi {{a, b, c, d, e}}...".format(n))

    a = min(repeat(lambda:    maj_sansrep(T), number=1, repeat=3))
    b = min(repeat(lambda: maj_boyermoore(T), number=1, repeat=3))

    print("Temps d'exécution:")
    print()
    print(" maj_sansrep:    {:15.10f} secs.".format(b))
    print(" maj_boyermoore: {:15.10f} secs.".format(c))
