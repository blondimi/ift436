from itertools import permutations

def max_iter(s):                   # Décompte du nombre d'opérations élémentaires:
    i = 1                          ; nb_oper_elem  = 1 # affectation
    m = s[0]                       ; nb_oper_elem += 2 # affectation + accès

    pass                           ; nb_oper_elem += 1 # condition (1ère fois)

    while i < len(s):
        pass                       ; nb_oper_elem += 2 # accès + comparaison
        if s[i] > m:
            m = s[i]               ; nb_oper_elem += 2 # affectation + accès
            
        i = i + 1                  ; nb_oper_elem += 2 # affectation + addition
        pass                       ; nb_oper_elem += 1 # condition (autre fois)

    return (m, nb_oper_elem)

if __name__ == "__main__":
    # Exemple du nombre d'opérations élémentaires exécutées sur les
    # entrées de taille 1, 2 et 3
    for n in range(1, 3+1):
        entrees_taille_n = map(list, permutations(range(1, n+1)))

        for s in entrees_taille_n:
            m, nb_oper = max_iter(s)
            
            print("Entrée:", s, "  Sortie:", m, "  Nombre opér. élém.:", nb_oper)

        print()
