# Insère la spatule sous la crêpe i et renverse la pile
def renverser(crepes, i):
    j = 0
    
    while j < i - j:
        crepes[j], crepes[i - j] = crepes[i - j], crepes[j]
        j += 1

# Trie une pile de crêpes en O(n) insertions de spatule
def tri_crepes(crepes):
    i = len(crepes)

    while i > 0:
        # Identifier la position j de la prochaine plus grande crêpes
        j = i - 1

        for k in range(i - 1):
            if crepes[k] > crepes[j]:
                j = k

        # Mettre la crêpe j sur le dessus de la pile
        renverser(crepes, j)

        # Mettre la crêpe j à sa position finale
        i -= 1
        renverser(crepes, i)

# Affiche une pile de crêpes graphiquement
def afficher(crepes):
    if len(crepes) > 0:
        m = max(crepes)
    
        print("\n".join(" " * ((m - c) // 2) +
                        "-" * c +
                        " " * ((m - c + 1) // 2) for c in crepes))

# Exemple
if __name__ == "__main__":
    crepes = [9, 3, 1, 5, 7]    #   ---------           -
                                #      ---             ---
    print("Avant tri:", crepes) #       -      ==>    -----
    afficher(crepes)            #     -----          -------
    print()                     #    -------        ---------

    tri_crepes(crepes)
    print("Après tri:", crepes)
    afficher(crepes)
