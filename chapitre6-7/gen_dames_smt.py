def var(i, j):
    return "x_{}_{}".format(i + 1, j + 1)

def decl_var(n):
    code  = [";; Déclaration des variables"]
    code += ["(declare-const {} Bool)".format(var(i, j))
             for i in range(n) for j in range(n)]
    
    return "\n".join(code)

def au_moins_une_par_ligne(n):
    code = [";; Au moins une dame par ligne"]

    for i in range(n):
        lit = [var(i, j) for j in range(n)]

        code.append("(assert (or " + " ".join(lit) + "))")

    return "\n".join(code)

def au_plus_une_par_ligne(n):
    code = [";; Au plus une dame par ligne"]

    for i in range(n):
        for j in range(n - 1):
            clauses = ["(or (not {}) (not {}))".format(var(i, j), var(i, k))
                       for k in range(j + 1, n)]

            code.append("(assert (and " + " ".join(clauses) + "))")

    return "\n".join(code)

def au_plus_une_par_colonne(n):
    code = [";; Au plus une dame par colonne"]

    for i in range(n):
        for j in range(n - 1):
            clauses = ["(or (not {}) (not {}))".format(var(j, i), var(k, i))
                       for k in range(j + 1, n)]

            code.append("(assert (and " + " ".join(clauses) + "))")

    return "\n".join(code)

def au_plus_une_par_diagonale(n):
    code = [";; Au plus une dame par diagonale"]

    for i in range(n):
        for j in range(n):
            # Première direction
            I_ = [i_ for i_ in range(n)
                  if (i, j) != (i_, i + j - i_) and 0 <= i + j - i_ <= j]
            
            clauses = ["(or (not {}) (not {}))".format(var(i, j),
                                                       var(i_, i + j - i_))
                       for i_ in I_]

            if len(I_) > 0:
                code.append("(assert (and " + " ".join(clauses) + "))")

            # Deuxième direction
            I_ = [i_ for i_ in range(n)
                  if (i, j) != (i_, i + j - i_) and 0 <= i_ - i + j <= j]
            
            clauses = ["(or (not {}) (not {}))".format(var(i, j),
                                                       var(i_, i_ - i + j))
                       for i_ in I_]

            if len(I_) > 0:
                code.append("(assert (and " + " ".join(clauses) + "))")

    return "\n".join(code)

def gen(n):
    code = [decl_var(n), au_moins_une_par_ligne(n),
            au_plus_une_par_ligne(n), au_plus_une_par_colonne(n),
            au_plus_une_par_diagonale(n),
            "(check-sat)", "(get-model)"]

    return "\n\n".join(code)

# Génère une formula SMT du problème des n dames
if __name__ == "__main__":
    n = 4

    print(gen(n))
