class Elem:
    def __init__(self, val, succ=None):
        self.val  = val
        self.succ = succ

    def __str__(self):
        acc = []
        ptr = self

        while ptr is not None:
            acc.append(str(ptr.val))

            ptr = ptr.succ

        return " →  ".join(acc)

def tri_binaire_liste(s):
    tete  = [None, None]
    queue = [None, None]
    ptr   = s

    # Créer deux listes pour les 0 et 1
    while ptr is not None:
        i = ptr.val
        
        if tete[i] is None:
            tete[i]  = ptr
        else:
            queue[i].succ = ptr

        queue[i] = ptr
        ptr      = ptr.succ

    # Connecter les deux listes
    if tete[0] is None:
        return tete[1]
    else:
        queue[0].succ = tete[1]

        if queue[1] is not None:
            queue[1].succ = None

        return tete[0]

# Exemple
if __name__ == "__main__":
    s = Elem(0, Elem(1, Elem(0, Elem(0, Elem(1, Elem(0, Elem(1)))))))

    print(s)
    print(tri_binaire_liste(s))
