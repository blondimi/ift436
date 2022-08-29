from random import randint

def pile_face(piece_biaisee):
    while True:
        x = piece_biaisee()
        y = piece_biaisee()

        if x != y:
            break

    return x

# Exemples
if __name__ == "__main__":
    num_tirages = 10000

    def tirer(piece):
        pile = 0

        for _ in range(num_tirages):
            if pile_face(piece) == 0:
                pile += 1

        return pile / num_tirages

    piece1 = lambda: 0 if randint(1,   3) == 1 else 1 # p = 1/3
    piece2 = lambda: 0 if randint(1, 100) == 1 else 1 # p = 1/100
    pile1  = tirer(piece1)
    pile2  = tirer(piece2)

    print(f"Distribution de la pièce simulée, sur {num_tirages} tirages")
    print()
    print("Avec pièce biaisée où p = 1/3")
    print(" pile: {}%".format(100 * pile1))
    print(" face: {}%".format(100 * (1 - pile1)))
    print()
    print("Avec pièce biaisée où p = 1/100")
    print(" pile: {}%".format(100 * pile2))
    print(" face: {}%".format(100 * (1 - pile2)))
