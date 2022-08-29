from heapq  import heapify, heappop
from random import choice, randint

def tri_insertion(s):
    for i in range(len(s)):
        j = i
        
        while j > 0 and s[j-1] > s[j]:
            s[j-1], s[j] = s[j], s[j-1]
            j -= 1

    return s

def tri_fusion(s):
    def fusion(x, y):
        i = j = 0
        z = []

        while i < len(x) and j < len(y):
            if x[i] <= y[j]:
                z.append(x[i])
                i += 1
            else:
                z.append(y[j])
                j += 1

        return z + x[i:] + y[j:]
    
    if len(s) <= 1:
        return s
    else:
        m = len(s) // 2

        return fusion(tri_fusion(s[:m]), tri_fusion(s[m:]))

def tri_monceau(s):
    t = []

    heapify(s)

    while len(s) > 0:
        t.append(heappop(s))

    return t

def tri_rapide(s):
    if len(s) == 0:
        return s
    else:
        pivot  = choice(s) # Choisir pivot aléatoirement
        
        gauche = [x for x in s if x <  pivot]
        milieu = [x for x in s if x == pivot]
        droite = [x for x in s if x >  pivot]
        
        return tri_rapide(gauche) + milieu + tri_rapide(droite)

def tri_rapide_surplace(s):
    def partition(lo, hi): # Partition de Lomuto
        x = s[hi]
        i = lo
        
        for j in range(lo, hi):
            if s[j] < x:
                s[i], s[j] = s[j], s[i]
                i += 1
                
        s[i], s[hi] = s[hi], s[i]
        
        return i

    def tri(lo, hi):
        if lo < hi:
            p = partition(lo, hi)

            tri(lo, p - 1)
            tri(p + 1, hi)

    tri(0, len(s) - 1)
    
    return s

# Exemples
if __name__ == "__main__":
    algos = [tri_insertion, tri_fusion, tri_monceau,
             tri_rapide, tri_rapide_surplace]
    seq   = [randint(0, 100) for _ in range(10)]

    print("À trier: s =", seq)
    print("Résultats:")
    print()
    
    for tri in algos:
        print("{:>19}(s) = {}".format(tri.__name__, tri(list(seq))))
