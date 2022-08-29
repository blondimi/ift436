def carre(n):
    c = 0
    m = 1

    for _ in range(n):
        c += m
        m += 2

    return c

# Exemples
if __name__ == "__main__":
    print("   1² =", carre(1))
    print("   2² =", carre(2))
    print("   3² =", carre(3))
    print("   4² =", carre(4))
    print("1000² =", carre(1000))
