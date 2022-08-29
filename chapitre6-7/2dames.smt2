;; À copier/coller sur https://compsys-tools.ens-lyon.fr/z3/ ou
;;                                                        en ligne de commande
;;
;; Problème des n dames avec n = 2

(declare-const x11 Bool)
(declare-const x12 Bool)
(declare-const x21 Bool)
(declare-const x22 Bool)

(assert (or x11 x12))
(assert (or x21 x22))

(assert (or (not x11) (not x12)))
(assert (or (not x21) (not x22)))

(assert (or (not x11) (not x21)))
(assert (or (not x12) (not x22)))

(assert (or (not x12) (not x21)))
(assert (or (not x11) (not x22)))

(check-sat)

