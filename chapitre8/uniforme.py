from math   import ceil, log
from random import randint

def uniforme(c):
    k = ceil(log(c, 2))

    while True:
        x = 0

        for i in range(k):
            y  = randint(0, 1)
            x += 2**i * y

        if x < c:
            break

    return x

# Exemple: génération de nombres parmi [0, 1, 2, 3, 4]
if __name__ == "__main__":
    num_exp = 100000
    valeurs = [0, 1, 2, 3, 4]
    distrib = {x: 0 for x in valeurs}

    for _ in range(num_exp):
        x = uniforme(5)

        distrib[x] += 1

    for x in valeurs:
        print("{}: {}%".format(x, (100.0 * distrib[x]) / num_exp))
