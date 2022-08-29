from timeit import repeat

def monnaie_iter(v, m):
    # v = sorted(v, reverse=True)
    r, sol, i = m, 0, 0

    while r > 0:
        if r >= v[i]:
            sol += 1
            r   -= v[i]
        else:
            i += 1

    return sol

def monnaie_mod(v, m):
    # v = sorted(v, reverse=True)
    r, sol = m, 0

    for i in range(len(v)):
        sol += r // v[i]
        r   %= v[i]

    return sol

# Exemples
if __name__ == "__main__":
    ## Exemple des diapos
    v = [200, 100, 25, 10, 5, 1]
    m = 582

    print("Nombre minimal de pièces afin de rendre {}¢".format(m))
    print()
    print(" monnaie_iter:", monnaie_iter(v, m))
    print(" monnaie_mod :",  monnaie_mod(v, m))
    print()

    ## Algo. sans modulo vs. avec modulo
    m = 987656789

    print("Nombre minimal de pièces afin de rendre {}¢".format(m))
    print("Calcul...")

    # Exécuter chaque algo. 10 fois et garder meilleur temps
    a = min(repeat(lambda: monnaie_iter(v, m), number=1, repeat=10))
    b = min(repeat(lambda:  monnaie_mod(v, m), number=1, repeat=10))

    print("Temps d'exécution:")
    print()
    print(" monnaie_iter: {:15.10f} secs.".format(a))
    print(" monnaie_mod:  {:15.10f} secs.".format(b))
