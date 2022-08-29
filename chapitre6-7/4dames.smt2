;; À copier/coller sur https://compsys-tools.ens-lyon.fr/z3/ ou
;;                                                        en ligne de commande
;;
;; Problème des n dames avec n = 4


;; Déclaration des variables
(declare-const x_1_1 Bool)
(declare-const x_1_2 Bool)
(declare-const x_1_3 Bool)
(declare-const x_1_4 Bool)
(declare-const x_2_1 Bool)
(declare-const x_2_2 Bool)
(declare-const x_2_3 Bool)
(declare-const x_2_4 Bool)
(declare-const x_3_1 Bool)
(declare-const x_3_2 Bool)
(declare-const x_3_3 Bool)
(declare-const x_3_4 Bool)
(declare-const x_4_1 Bool)
(declare-const x_4_2 Bool)
(declare-const x_4_3 Bool)
(declare-const x_4_4 Bool)

;; Au moins une dame par ligne
(assert (or x_1_1 x_1_2 x_1_3 x_1_4))
(assert (or x_2_1 x_2_2 x_2_3 x_2_4))
(assert (or x_3_1 x_3_2 x_3_3 x_3_4))
(assert (or x_4_1 x_4_2 x_4_3 x_4_4))

;; Au plus une dame par ligne
(assert (and (or (not x_1_1) (not x_1_2)) (or (not x_1_1) (not x_1_3)) (or (not x_1_1) (not x_1_4))))
(assert (and (or (not x_1_2) (not x_1_3)) (or (not x_1_2) (not x_1_4))))
(assert (and (or (not x_1_3) (not x_1_4))))
(assert (and (or (not x_2_1) (not x_2_2)) (or (not x_2_1) (not x_2_3)) (or (not x_2_1) (not x_2_4))))
(assert (and (or (not x_2_2) (not x_2_3)) (or (not x_2_2) (not x_2_4))))
(assert (and (or (not x_2_3) (not x_2_4))))
(assert (and (or (not x_3_1) (not x_3_2)) (or (not x_3_1) (not x_3_3)) (or (not x_3_1) (not x_3_4))))
(assert (and (or (not x_3_2) (not x_3_3)) (or (not x_3_2) (not x_3_4))))
(assert (and (or (not x_3_3) (not x_3_4))))
(assert (and (or (not x_4_1) (not x_4_2)) (or (not x_4_1) (not x_4_3)) (or (not x_4_1) (not x_4_4))))
(assert (and (or (not x_4_2) (not x_4_3)) (or (not x_4_2) (not x_4_4))))
(assert (and (or (not x_4_3) (not x_4_4))))

;; Au plus une dame par colonne
(assert (and (or (not x_1_1) (not x_2_1)) (or (not x_1_1) (not x_3_1)) (or (not x_1_1) (not x_4_1))))
(assert (and (or (not x_2_1) (not x_3_1)) (or (not x_2_1) (not x_4_1))))
(assert (and (or (not x_3_1) (not x_4_1))))
(assert (and (or (not x_1_2) (not x_2_2)) (or (not x_1_2) (not x_3_2)) (or (not x_1_2) (not x_4_2))))
(assert (and (or (not x_2_2) (not x_3_2)) (or (not x_2_2) (not x_4_2))))
(assert (and (or (not x_3_2) (not x_4_2))))
(assert (and (or (not x_1_3) (not x_2_3)) (or (not x_1_3) (not x_3_3)) (or (not x_1_3) (not x_4_3))))
(assert (and (or (not x_2_3) (not x_3_3)) (or (not x_2_3) (not x_4_3))))
(assert (and (or (not x_3_3) (not x_4_3))))
(assert (and (or (not x_1_4) (not x_2_4)) (or (not x_1_4) (not x_3_4)) (or (not x_1_4) (not x_4_4))))
(assert (and (or (not x_2_4) (not x_3_4)) (or (not x_2_4) (not x_4_4))))
(assert (and (or (not x_3_4) (not x_4_4))))

;; Au plus une dame par diagonale
(assert (and (or (not x_1_2) (not x_2_1))))
(assert (and (or (not x_1_3) (not x_2_2)) (or (not x_1_3) (not x_3_1))))
(assert (and (or (not x_1_4) (not x_2_3)) (or (not x_1_4) (not x_3_2)) (or (not x_1_4) (not x_4_1))))
(assert (and (or (not x_2_2) (not x_3_1))))
(assert (and (or (not x_2_2) (not x_1_1))))
(assert (and (or (not x_2_3) (not x_3_2)) (or (not x_2_3) (not x_4_1))))
(assert (and (or (not x_2_3) (not x_1_2))))
(assert (and (or (not x_2_4) (not x_3_3)) (or (not x_2_4) (not x_4_2))))
(assert (and (or (not x_2_4) (not x_1_3))))
(assert (and (or (not x_3_2) (not x_4_1))))
(assert (and (or (not x_3_2) (not x_2_1))))
(assert (and (or (not x_3_3) (not x_4_2))))
(assert (and (or (not x_3_3) (not x_1_1)) (or (not x_3_3) (not x_2_2))))
(assert (and (or (not x_3_4) (not x_4_3))))
(assert (and (or (not x_3_4) (not x_1_2)) (or (not x_3_4) (not x_2_3))))
(assert (and (or (not x_4_2) (not x_3_1))))
(assert (and (or (not x_4_3) (not x_2_1)) (or (not x_4_3) (not x_3_2))))
(assert (and (or (not x_4_4) (not x_1_1)) (or (not x_4_4) (not x_2_2)) (or (not x_4_4) (not x_3_3))))

(check-sat)

(get-model)
