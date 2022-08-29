def trier_seq_binaire(s):
    m = max(len(x) for x in s)

    for i in range(m):
        lo = [x for x in s if len(x) <= i or x[len(x)-i-1] == "0"]
        hi = [x for x in s if x not in lo]
        s  = lo + hi

    return s

def trier_nombres(s):
    l = max(s) if len(s) > 0 else 0
    m = 1

    while l > 1:
        l //= 2
        m += 1

    d = 1

    for i in range(m):
        lo = [k for k in s if k < d or (k // d) % 2 == 0]
        hi = [k for k in s if k not in lo]
        s  = lo + hi
        d *= 2

    return s

# Exemples
if __name__ == "__main__":
    s = ["111" , "011" , "101" , "1" , "10"]

    print("À trier:", s)
    print("Triée:  ", trier_seq_binaire(s))
    print()

    s = [7, 3, 5, 1, 2]

    print("À trier:", s)
    print("Triée:  ", trier_nombres(s))
