def somme_max_iter(s):
    somme_max = float("-inf")

    for i in range(len(s)):
        for j in range(i, len(s)):
            cumul = 0
            
            for k in range(i, j + 1):
                cumul += s[k]

            somme_max = max(somme_max, cumul)

    return somme_max

def somme_max_rec(s):
    if len(s) == 0:
        return float("-inf")
    elif len(s) == 1:
        return s[0]
    else:
        m = len(s) // 2

        gauche = s[:m]
        droite = s[m:]

        # Cumulatif maximal vers la droite
        c_droite = float("-inf")
        cumul    = 0

        for x in droite:
            cumul += x
            c_droite = max(c_droite, cumul)
        
        # Cumulatif maximal vers la gauche
        c_gauche = float("-inf")
        cumul    = 0

        for x in reversed(gauche):
            cumul += x
            c_gauche = max(c_gauche, cumul)

        # Somme maximale des deux côtés
        a = somme_max_rec(gauche)
        b = somme_max_rec(droite)

        # Somme maximale
        return max(a, b, c_gauche + c_droite)

# Exemple des notes de cours
if __name__ == "__main__":
    s = [3, 1, -5, 4, -2, 1, 6, -3]

    print("Somme contigüe maximale (itératif):", somme_max_iter(s))
    print("Somme contigüe maximale (récursif):", somme_max_rec(s))
