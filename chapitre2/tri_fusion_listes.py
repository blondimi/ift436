class Elem:
    def __init__(self, val, succ = None):
        self.val  = val
        self.succ = succ

    def __str__(self):
        s = []
        x = self

        while (x is not None):
            s.append(x.val)
            x = x.succ

        return " -> ".join(map(str, s))

def fusion(x, y):
    if x is None:
        return y
    elif y is None:
        return x
    else:
        # Identifier la première valeur de la liste fusionnée
        if x.val <= y.val:
            z = x
            x = x.succ
        else:
            z = y
            y = y.succ

        # Construire le reste de la liste fusionnée
        debut = z

        while (x is not None) or (y is not None):
            if (y is None) or (x is not None and x.val <= y.val):
                z.succ = x
                x      = x.succ                
            else:
                z.succ = y
                y      = y.succ

            z = z.succ
        
        return debut
    
def tri_fusion(s):
    if (s is None) or (s.succ is None):
        return s
    else:
        # Trouver le centre de s
        x = s
        y = s.succ

        while (y is not None) and (y.succ is not None):
            x = x.succ
            y = y.succ.succ

        # Scinder s en deux: x et y
        y      = x.succ
        x.succ = None
        x      = s

        # Trier x et y récursivement, puis fusionner
        return fusion(tri_fusion(x), tri_fusion(y))

# Exemple
if __name__ == "__main__":
    s = Elem(3, Elem(1, Elem(4, Elem(5, Elem(2, Elem(6))))))

    print("Liste avant tri: ", s)
    print("Liste triée:     ", tri_fusion(s))
