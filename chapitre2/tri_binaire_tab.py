class Bloc:
    def __init__(self, i=None, j=None):
        self.deb = i
        self.fin = j

def renverser(s, b):
    i, j = b.deb, b.fin

    while (i < j):
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

def echanger(s, a, b):
    renverser(s, a)
    renverser(s, b)
    renverser(s, Bloc(a.deb, b.fin))

def tri_binaire_tab(s):
    def trier(i, j):
        if i == j:
            return i if s[i] == 1 else i + 1
        else:
            m = (i + j) // 2

            x = trier(i, m)
            y = trier(m + 1, j)

            echanger(s, Bloc(x, m), Bloc(m + 1, y - 1))
            
            return x + y - (m + 1)

    if len(s) > 0:
        trier(0, len(s) - 1)

# Exemple
if __name__ == "__main__":
    s = [0, 1, 0, 0, 1, 0, 1]

    print("Avant tri:", s)

    tri_binaire_tab(s)
    
    print("Après tri:", s)
