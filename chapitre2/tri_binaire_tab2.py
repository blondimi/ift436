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
    def prochain(i, x):
        for j in range(i, len(s)):
            if s[j] == x:
                return j

        return len(s)
    
    a = Bloc()
    b = Bloc()
    i = 0

    while True:
        a.deb = prochain(i, 1)
        b.deb = prochain(a.deb, 0)
        a.fin = b.deb - 1
        b.fin = prochain(b.deb, 1) - 1

        echanger(s, a, b)
        
        if b.deb == len(s) and i == 0:
            break
        else:
            i = prochain(b.fin + 1, 0) % len(s)
            
# Exemple
if __name__ == "__main__":
    s = [0, 1, 0, 0, 1, 0, 1]

    print("Avant tri:", s)

    tri_binaire_tab(s)
    
    print("Après tri:", s)
