from random import randint

def lancer_de():
    while True:
        y0 = randint(0, 1)
        y1 = randint(0, 1)
        y2 = randint(0, 1)

        if not (y2 == y1 == y0):
            break

    return 4 * y2 + 2 * y1 + y0

if __name__ == "__main__":
    num_exp = 100000
    valeurs = [1, 2, 3, 4, 5, 6]
    distrib = {x: 0 for x in valeurs}

    for _ in range(num_exp):
        x = lancer_de()

        distrib[x] += 1

    for x in valeurs:
        print("{}: {}%".format(x, (100.0 * distrib[x]) / num_exp))
