from fractions import Fraction

def glouton_fractionnel(c, v, p):
    ratio   = lambda i: Fraction(v[i], p[i])
    indices = sorted(range(len(v)), key=ratio, reverse=True)
    valeur  = 0
    poids   = 0

    x = [0 for _ in v]

    for i in indices:
        if poids + p[i] <= c:
            valeur += v[i]
            poids  += p[i]
            x[i]    = 1
        else:
            coeff   = Fraction(c - poids, p[i])
            valeur += coeff * v[i]
            poids  += coeff * p[i]
            x[i]    = coeff

    return x

def approximation(c, v, p):
    ratio   = lambda i: Fraction(v[i], p[i])
    indices = sorted(range(len(v)), key=ratio, reverse=True)
    valeur  = 0
    poids   = 0

    x = [0 for _ in v]
    n = len(indices)
    i = 0

    while (i < n) and (poids + p[indices[i]] <= c):
        j = indices[i]
        
        valeur += v[j]
        poids  += p[j]

        x[j] = 1
        i   += 1

    if (i >= n) or (valeur > v[indices[i]]):
        return x
    else:
        return [1 if j == indices[i] else 0 for j in range(n)]

# Exemples
if __name__ == "__main__":
    prod = lambda x, y: sum(a * b for (a, b) in zip(x, y))

    # Exemple des notes de cours
    v = [ 50,   5,  65, 10,  12,  20]
    p = [700, 320, 845, 70, 420, 180]
    c = 900
    
    # Algorithme glouton
    x = glouton_fractionnel(c, v, p)
    
    print("Algorithme glouton (variante fractionnelle):")
    print(" Solution:", x)
    print(" Poids:   ", prod(x, p))
    print(" Valeur:  ", prod(x, v))
    print()

    # Algorithme d'approximation
    x = approximation(c, v, p)
    
    print("Algorithme d'approximation (variante discrète):")
    print(" Solution:", x)
    print(" Poids:   ", prod(x, p))
    print(" Valeur:  ", prod(x, v))
