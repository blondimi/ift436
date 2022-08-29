def num_bits(s):
    def premier_un(lo, hi):
        if lo == hi:
            return lo if s[lo] == 1 else None
        else:
            mid = (lo + hi) // 2

            if s[mid] == 0:
                return premier_un(mid + 1, hi)
            elif s[mid] == 1:
                return premier_un(lo, mid)

    pos = premier_un(0, len(s) - 1)

    return (len(s) - pos) if pos is not None else 0

def num_bits_alternatif(s):
    def premier_un(lo, hi):
        if lo == hi:
            return lo
        else:
            mid = (lo + hi) // 2

            if s[mid] == 0:
                return premier_un(mid + 1, hi)
            elif s[mid] == 1:
                return premier_un(lo, mid)

    if len(s) == 0 or s[-1] == 0:
        return 0
    else:
        return len(s) - premier_un(0, len(s) - 1)

# Exemple des notes de cours
if __name__ == "__main__":
    s = [0, 0, 0, 1, 1, 1, 1, 1]

    print("Séquence s =", s)
    print()
    print("Nombre de bits égaux à 1:", num_bits(s))
    print("Nombre de bits égaux à 1:", num_bits_alternatif(s))
