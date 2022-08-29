from pavage import Region, paver

def points(t):
    p = set()

    for c in t:
        p |= {(c[1],     c[0]),
              (c[1] + 1, c[0]),
              (c[1] + 1, c[0] - 1),
              (c[1],     c[0] - 1)}
        
    return p

def est_voisin(c, d):
    return (((c[0] == d[0]) and abs(c[1] - d[1]) == 1) or
            ((c[1] == d[1]) and abs(c[0] - d[0]) == 1))

def est_adjacent(c, d):
    return (c[0] == d[0]) == (c[1] != d[1])

def coins(t):
    p = points(t)

    def adj(c):
        return [d for d in p if est_voisin(c, d)]
    
    return {c for c in p if len(adj(c)) % 2 == 0}

def contour(t):
    cor = list(coins(t))
    bor = [cor[0]]
    cor = cor[1:]

    while len(cor) > 1:
        last = bor[-1]
        new  = [x for x in cor if est_adjacent(x, last)][0]

        cor.remove(new)
        bor.append(new)

    return bor + cor

def latex(tuiles, trou):
    col = ["red", "blue", "orange", "green", "yellow", "brown",
           "pink", "lime", "cyan", "purple", "olive", "violet"]
    
    def polygon(bor, c):
        s = "".join(["({0}, {1}) -- ".format(i, -j) for (i, j) in bor])
        
        return ("\\fill[draw, white, fill={1}, line width=2pt] "
                "{0} cycle;").format(s, c)

    acc = []

    acc.append("\\documentclass{standalone}")
    acc.append("\\usepackage{tikz}")
    acc.append("")
    acc.append("\\begin{document}")
    acc.append("")
    acc.append("\\begin{tikzpicture}")
    acc.append("")
    acc.append(polygon(contour({trou}), "black"))
    
    i = 0
    
    for t in tuiles:
        acc += [polygon(contour(t), col[i])]
        i = (i + 1) % len(col)

    acc.append("\\end{tikzpicture}")
    acc.append("")
    acc.append("\\end{document}")

    return "\n".join(acc)

# Exemple
if __name__ == "__main__":
    n = 6
    
    region = Region(1, 2**n, 1, 2**n)
    trou   = (2, 2)
    tuiles = paver(region, trou)

    print(latex(tuiles, trou))
