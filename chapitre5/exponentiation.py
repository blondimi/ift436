def exp_naive_rec(b, n):
    if n == 0:
        return 1
    else:
        return b * exp_naive_rec(b, n - 1)

def exp_naive_iter(b, n):
    r = 1

    for _ in range(n):
        r *= b

    return r

def exp_rapide(b, n):
    if n == 0:
        return 1
    else:
        m = exp_rapide(b, n // 2)
        k = b if n % 2 == 1 else 1
        
        return m * m * k

# Exemple
if __name__ == "__main__":
    b = 7
    n = 42

    r = [exp_naive_rec(b, n), exp_naive_iter(b, n), exp_rapide(b, n)]

    print("Exponentiation naïve (récursif): {}^{} = {}".format(b, n, r[0]))
    print("Exponentiation naïve (itératif): {}^{} = {}".format(b, n, r[1]))
    print("Exponentiation rapide:           {}^{} = {}".format(b, n, r[2]))
