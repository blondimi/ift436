def num_inversions_iter(s):
    c = 0

    for i in range(len(s)):
        for j in range(len(s)):
            if i < j and s[i] > s[j]:
                c += 1

    return c

def num_inversions_rec(s):
    def fusion(x, y):
        i = j = c = 0
        z = []

        while i < len(x) and j < len(y):
            if x[i] <= y[j]:
                z.append(x[i])
                i += 1
            else:
                z.append(y[j])
                j += 1
                c += len(x) - i
                
        return (z + x[i:] + y[j:], c)

    def tri_inversions(t):
        if len(t) <= 1:
            return (t, 0)
        else:
            m = len(t) // 2
            
            gauche, a = tri_inversions(t[:m])
            droite, b = tri_inversions(t[m:])
            triee,  c = fusion(gauche, droite)
            
            return (triee, a + b + c)

    return tri_inversions(s)[1]

# Exemple des notes de cours
if __name__ == "__main__":
    s = [30, 50, 10, 40, 20]

    print("Séquence s =", s)
    print()
    print("Nombre d'inversions (itératif):", num_inversions_iter(s))
    print("Nombre d'inversions (récursif):", num_inversions_rec(s))
