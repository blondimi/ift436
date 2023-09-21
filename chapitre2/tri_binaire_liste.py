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
    tete = s
    ptr  = s
    pred = None
    
    while ptr is not None:
        if pred is not None and ptr.val == 0:
            pred.succ = ptr.succ            
            ptr.succ  = tete
            tete      = ptr
            ptr       = pred.succ
        else:        
            pred = ptr
            ptr  = ptr.succ

    return tete

# Exemple
if __name__ == "__main__":
    s = Elem(0, Elem(1, Elem(0, Elem(0, Elem(1, Elem(0, Elem(1)))))))

    print(s)
    print(tri_binaire_liste(s))
