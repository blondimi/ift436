from collections import deque

def  gauche(b): return b[0]
def hauteur(b): return b[1]
def  droite(b): return b[2]

def decouper(blocs):
    def inserer(q, bloc):
        if gauche(bloc) != droite(bloc):
            q.appendleft(bloc)

    if len(blocs) <= 1:
        return blocs
    else:
        m = len(blocs) // 2
        x = deque(decouper(blocs[:m]))
        y = deque(decouper(blocs[m:]))
        z = []

        # Fusionner blocs de x et y dans z
        while len(x) > 0 and len(y) > 0:
            a = x.popleft()
            b = y.popleft()

            if gauche(b) < gauche(a):
                a, b = b, a
                x, y = y, x

            if droite(a) <= gauche(b):
                z.append(a)
                inserer(y, b)
            else:
                if droite(a) <= droite(b):
                    if hauteur(a) <= hauteur(b):
                        inserer(x, (gauche(a), hauteur(a), gauche(b)))
                        inserer(y, b)
                    else:
                        inserer(x, a)
                        inserer(y, (droite(a), hauteur(b), droite(b)))
                else:
                    if hauteur(a) <= hauteur(b):
                        inserer(x, (droite(b), hauteur(a), droite(a)))
                        inserer(x, (gauche(a), hauteur(a), gauche(b)))
                        inserer(y, b)
                    else:
                        inserer(x, a)

        # Ajouter blocs restants
        z.extend(x)
        z.extend(y)
        
        return z

def surface(blocs):
    acc = 0

    for b in blocs:
        acc += hauteur(b) * (droite(b) - gauche(b))

    return acc

# Exemple des notes de cours
if __name__ == "__main__":
    paysage   = [ (1, 2,  3),  (2, 1,  5),  (3, 4,  8), (9, 3, 10),
                 (11, 2, 12), (11, 1, 15), (13, 2, 17)]
    decoupage = decouper(paysage)

    print(f"Paysage:  \n\n{paysage}\n")
    print(f"Découpage:\n\n{decoupage}\n")
    print("Surface:", surface(decoupage))
