#  Pré-condition: séquence ordonnée circulairement t.q. |s| = 1
#                 ou (|s| ≥ 2 et le premier élément diffère du dernier)
# Post-condition: max(s)
def max_circ(s):
    n = len(s)

    #  Pré-condition: lo < hi, s[lo] > s[hi] et s ord. circulairement
    # Post-condition: max(s[lo : hi])
    def aux(lo, hi):
        if hi - lo == 1:
           return s[lo]
        else:
            mid = (lo + hi) // 2

            if s[lo] > s[mid]:
                return aux(lo, mid)
            elif s[mid] > s[hi]:
                return aux(mid, hi)
            else:
                assert(False) # Impossible car s[lo] > s[hi]

    return aux(0, n - 1) if s[0] > s[n - 1] else s[n - 1]

# Exemples
if __name__ == "__main__":
    # Exemple des notes de cours
    s = [10, 12, 19, 1, 3, 4, 7]

    print("     s =", s)
    print("max(s) =", max_circ(s))
    print()

    # Exemple avec doublons mais pas aux deux bouts #    ##
    s = [6, 6, 7, 7, 0, 0, 1, 1, 2, 3, 5, 5]        #  ####
                                                    #  ####      ##
    print("     s =", s)                            #  ####      ##
    print("max(s) =", max_circ(s))                  #  ####     ###
    print()                                         #  ####    ####
                                                    #  ####  ######
                                                    #  ¯¯¯¯¯¯¯¯¯¯¯¯

    # Exemple avec doublons aux deux bouts          #   #
    s = [5, 7, 5]                                   #   #
                                                    #  ###
    print("     s =", s)                            #  ###
    print("max(s) =", max_circ(s))                  #  ###
    print("Oups...")                                #  ###
                                                    #  ###
                                                    #  ¯¯¯
