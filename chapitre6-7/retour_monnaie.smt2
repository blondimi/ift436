;; À copier/coller sur https://compsys-tools.ens-lyon.fr/z3/ ou
;;                                                        en ligne de commande
;;
;; Problème du retour de monnaie avec s = [1, 5, 7] et m = 10

(declare-const x Int)
(declare-const y Int)
(declare-const z Int)

(assert (>= x 0))
(assert (>= y 0))
(assert (>= z 0))

(assert (= 10 (+ x (* 5 y) (* 7 z))))

(minimize (+ x y z))
(check-sat)
(get-model)
