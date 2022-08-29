def mult_rapide(n, x, y):
    if n == 1:
        return x * y
    else:
        k = (n + 1) // 2

        a, b = x // 10**k, x % 10**k
        c, d = y // 10**k, y % 10**k

        e = mult_rapide(k, a, c)
        f = mult_rapide(k, b, d)        
        g = mult_rapide(k, a - b, c - d)

        return (10**(2*k) * e) + (10**k * (e + f - g)) + f

# Exemple
if __name__ == "__main__":
    n = 13
    x = 1234567890123
    y = 8765432109876

    print("Mult. usuelle: {} · {} = {}".format(x, y, x * y))
    print("Mult. rapide:  {} · {} = {}".format(x, y, mult_rapide(n, x, y)))
