def tri_binaire(s):
    i = 0
    j = 1

    # Invariant: i < j et s[0   : i-1] ne contient que des 0 et
    #                     s[i+1 : j-1] ne contient que des 1
    while j < len(s):
        if s[i] == 0:
            i += 1
        elif s[j] == 1:
            j += 1
        else:
            s[i], s[j] = s[j], s[i]

        if j <= i:
            j = i + 1

    return s
            
# Exemple
if __name__ == "__main__":
    s = [0, 1, 0, 0, 1, 0, 1]

    print("Avant tri:", s)
    print("Après tri:", tri_binaire(s))
