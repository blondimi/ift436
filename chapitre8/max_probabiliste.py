from random import randrange, shuffle

def max_las_vegas(s):
    while True:
        i = randrange(len(s))

        if s[i] > s[0]:
            return s[i]
        elif s[i] < s[0]:
            return s[0]

def max_monte_carlo(s):
    for _ in range(300):
        i = randrange(len(s))

        if s[i] > s[0]:
            return s[i]

    return s[0]

if __name__ == "__main__":
    # Choisir deux nombres a et b aléatoirement
    v = list(range(0, 99))

    shuffle(v)
    
    a, b = v[:2]

    # Générer s
    n = 200
    s = [a] * (n // 2) + [b] * (n // 2)

    shuffle(s)

    print("Recherche du max. de s =", s)
    print()
    print("Las Vegas:  ", max_las_vegas(s))
    print("Monte Carlo:", max_monte_carlo(s))
