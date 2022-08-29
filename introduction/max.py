from random import randint
from timeit import repeat

def max_iter(x):
    i, m = 1, x[0]

    while i < len(x):
        if x[i] > m: m = x[i]
        i += 1

    return m

def max_rec(x):
    n = len(x)

    if n == 1:
        return x[0]
    else:
        m  = max(x[:n//2])
        m_ = max(x[n//2:])

        return m if m > m_ else m_

def max_rand(x):
    n = len(x) - 1
    i = randint(0, n)

    while True:
        j = randint(0, n)
        if x[j] > x[i]: i = j
        if x[i] != x[j]: break

    return x[i]

# Exemples
if __name__ == "__main__":
    ## Algorithmes déterministes
    x = [randint(0, 1000) for _ in range(randint(1, 15))]

    print("Maximum de", x)
    print()
    print(" max:     ", max(x))
    print(" max_iter:", max_iter(x))
    print(" max_rec: ", max_rec(x))
    print()

    ## Algorithme probabiliste vs. algorithmes déterministes
    n = 20000000
    x = [0] * (n // 2) + [1] * (n // 2)

    print("Maximum d'une séquence de {} occurrences de 0 et 1".format(n // 2))
    print("Calcul...")

    # Exécuter chaque algo. 10 fois et garder meilleur temps
    a = min(repeat(lambda:      max(x), number=1, repeat=10))
    b = min(repeat(lambda: max_iter(x), number=1, repeat=10))
    c = min(repeat(lambda:  max_rec(x), number=1, repeat=10))
    d = min(repeat(lambda: max_rand(x), number=1, repeat=10))

    print("Temps d'exécution:")
    print()
    print(" max:      {:15.10f} secs.".format(a))
    print(" max_iter: {:15.10f} secs.".format(b))
    print(" max_rec:  {:15.10f} secs.".format(c))
    print(" max_rand: {:15.10f} secs.".format(d))
