def tri_binaire(s):
    i = 0
    j = len(s) - 1

    while i < j:
        # Échanger s[i] et s[j] avec trois OU exclusifs
        s[i] = s[i] ^ s[j]
        s[j] = s[i] ^ s[j]
        s[i] = s[i] ^ s[j]

        i += not s[i]
        j -= s[j]

    return s

# Exemple
if __name__ == "__main__":
    s = [0, 1, 0, 0, 1, 0, 1]

    print("Avant tri:", s)
    print("Après tri:", tri_binaire(s))
