from collections import deque

def hanoi(piles):
    deplacements = []

    # (Notation sous pseudocode avec indices à partir de 1)
    #
    # Pré-condition:  - les trois piles sont valides (c.-à-d. ordonnées)
    #                 - |piles[src]| ≥ k
    #                 - piles[src][1:k] est empilable par-dessus piles[dst]
    #                                              et par-dessus piles[tmp]
    #
    # Post-condition: - piles[dst]' = piles[src][1:k] + piles[dst]
    #                 - piles[src]' = piles[src][k+1:]
    #                 - piles[tmp]' = piles[tmp]
    def rec(k, src, dst, tmp):
        if k > 0:
            # Déplacer k - 1 disques de piles[src] vers piles[tmp]
            rec(k - 1, src, tmp, dst)

            # Déplacer un disque de piles[src] vers piles[dst]
            piles[dst].appendleft(piles[src].popleft())
            deplacements.append((src, dst))
            
            # Déplacer k - 1 disques de piles[tmp] vers piles[dst]
            rec(k - 1, tmp, dst, src)

    # Déplacer piles[0] vers piles[1]
    n = len(piles[0])
    
    rec(n, 0, 1, 2)

    return deplacements

# Exemple
if __name__ == "__main__":
    n = 3
    piles = (deque(range(1, n + 1)), deque(), deque())

    print("Piles avant:", piles)

    deplacements = hanoi(piles)
    
    print("Piles après:", piles)
    print("Obtenu avec ces déplacements:")
    print()
    
    for (x,  y) in deplacements:
        print("  Pile {} →  Pile {}".format(x + 1, y + 1))

    print()
