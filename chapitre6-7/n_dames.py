def dames(n):
    def diag(sol):
        sud  = set()
        nord = set()

        for (i, j) in enumerate(sol):
            if i + j in nord:
                return False
            else:
                nord.add(i + j)

            if i - j in sud:
                return False
            else:
                sud.add(i - j)

        return True    

    def dames_(sol):
        if len(sol) == n:
            return sol
        else:
            for j in set(range(n)) - set(sol):
                if diag(sol + [j]):
                    r = dames_(sol + [j])

                    if r is not None:
                        return r

            return None

    return dames_([])

# Exemple
if __name__ == "__main__":
    for n in range(9):
        print(f"Solution pour n = {n}:", dames(n))
