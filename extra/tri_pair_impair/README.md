***En construction***

Un élément est _d-progressif_ si...

# Tri pair-impair

```
Proposition A. Au début de la passe i+1, les i occurrences de 2 les plus à droite sont d-progressifs.
```

Démonstration. Nous procédons par induction sur i.

Si i = 1, alors il faut considérer l'occurrence de 2 la plus à droite. Si elle est à la fin de la
séquence, alors elle ne bougera plus jamais, ce qui la rend immédiatement d-progressive. Si elle
est suivie d'un 0, alors l'occurrence de 2 est ou bien déjà d-progressif ou bien le sera à la passe
suivante.

Soit i > 1 et soit _j ∈ [1..i]_. Considérons la _j_-ème occurrence de 2 la plus à droite avant la passe _i_.
Regardons où elle se déplace après la passe. Si tous les éléments à sa droite sont des 2, alors
elle ne bouge pas et nous avons donc terminé. Supposons donc qu'il existe au moins une occurrence
de 0 à sa droite. Par hypothèse d'induction, toutes les occurrences de 2 à sa droite sont
d-progressive.

Nous utilserons ces notations:

* x* afin de dénoter le motif x répété zéro, une ou plusieurs fois;
* xᙾ afin de dénoter le motif x répété un nombre pair de fois (incluant zéro fois);
* ⌀ afin de dénoter un chiffre parmi 0 et 1.

En insecptant les dispositions possibles, on remarque, qu'après la passe _i_, la _j_-ème occurrence
devient en effet d-progressive:

*Cas 1: l'occurrence est d'un côté gauche*
```
      j-ème occ.
         v
Avant: ⋯ 2↔⌀ (⌀ᙾ 2 ⌀)* ⌀* 2*
Après: ⋯ ⌀ 2↔(⌀ᙾ ⌀ 2)* ⌀* 2*
           ^
        j-ème occ.
```
*Cas 2: l'occurrence est au début ou d'un côté droit*
```
      j-ème occ.
         v
Avant: ⋯⇿2 (⌀ᙾ 2 ⌀)* ⌀* 2*
Après: ⋯ 2↔(⌀ᙾ ⌀ 2)* ⌀* 2*
         ^
      j-ème occ.                                □
```

```
Proposition B. Soit k la quantité de 2. Au début de la passe k+2, l'unique 1 est d-progressif.
```

Démonstration. Par la proposition A, au début de la passe k+1, tous les 2 sont d-progressifs.

*Cas 1.A: l'occurrence est d'un côté gauche*
```
         v
Avant: ⋯ 1↔0 (0ᙾ 2 0)* 0* 2*
Après: ⋯ 0 1↔(0ᙾ 0 2)* 0* 2*
           ^
```
*Cas 1.B: l'occurrence est d'un côté gauche*
```
         v
Avant: ⋯ 1—2 2*
Après: ⋯ 1—2 2*
         ^
```
*Cas 2.A: l'occurrence est d'un côté droit*
```
           v
Avant: ⋯ 0↔1 (0ᙾ 2 0)* 0* 2*
Après: ⋯ 0 1↔(0ᙾ 0 2)* 0* 2*
           ^
```
*Cas 2.B: l'occurrence est d'un côté droit*
```
           v
Avant: ⋯ 2↔1 (0ᙾ 2 0)* 0* 2*
Après: ⋯⇿1 2 (0ᙾ 0 2)* 0* 2*
         ^
                                                □
```

Contre-exemple: 1 n'est pas d-progressif au début de l'itér. 3:

20 00 01 00 00 
2 00 00 01 00 0
20 00 00 01 00


1 x--y ... Si x = 0, OK. Si x = 2, alors y = 2, OK.

... 2--1  y--z...
... 1  2--y--z...


Soit j la position de l'une des i occurrences de 2 les plus à droite au début de la passe i.

*Cas 1*
```
                   j
                   v
 Avant la passe i: 2 x—y ⋯
 Après la passe i: 2—min(x, y) max(x, y)⋯
```

Si 2 > min(x, y), alors l'élément est d-progressif. Sinon, nous avons 2 = min(x, y) et ainsi x = y = 2.
Cela signifie que y était d-progressif au début de la passe. Par hypothèse d'induction, tous les éléments
à la droite de y sont des 2. Cela signifie que la séquence ne contient que des 2, ce qui est une contradiction.

*Cas 2*
```
                     v
 Avant la passe i: ⋯ 2—2 y⋯
 Après la passe i: ⋯ 2 2—y ⋯
```

```
                     v
 Avant la passe i: ⋯ 2—x y—z ⋯
 Après la passe i: ⋯ x 2—y z⋯
                       ^
```



des i plus grands éléments au début de la passe i. Nous devons montrer que x
est d-progressif après l'exécution de la passe i. Nous considérons tous les cas de
configurations avant la passe i.

 ⋯ 2—0 0* 2—0 0* ⋯ 2—0 0* 2 2 ⋯ 2





```
Proposition ?. Au début de la passe i+1, les i plus grands éléments sont d-progressifs.
```

Soit x l'un des i plus grands éléments au début de la passe i. Nous devons montrer que x
est d-progressif après l'exécution de la passe i. Nous considérons tous les cas de
configurations avant la passe i.

*Cas 1: x y—z ⋯.*

Après la passe i, nous avons x—min(y, z) max(y, z)⋯. Si x > min(y, z), alors x
est d-progressif. Supposons donc que x ≤ min(y, z). En particulier, x ≤ z. Donc,
z est l'un des i-1 plus grands éléments. Par hypothèse d'induction, il était
d-progressif avant la passe. Donc, tous les éléments à la droite de z lui étaient
supérieurs ou égaux. Nous en concluons donc que tous les éléments à la droite
de x lui sont maintenant supérieurs ou égaux. Ainsi, x est d-progressif.

Cas 2: ⋯ y—z x.

Après la passe i, x est encore le dernier élément. Il est donc trivialement
d-progressif.

Cas 3: ⋯ x—y ⋯.

Si x ≤ y, alors y est l'un des i-1 plus grands éléments. Par hypothèse d'induction,
y est d-progressif, ce qui implique que tous les éléments à sa droite lui sont
supérieurs ou égaux. À la passe i, x et y demeurent inchangés. Ainsi, tous les
éléments à la droite de x lui sont supérieurs ou égaux. Par conséquent, x
est d-progressif.

Cas 3.A: ⋯ x—y et x > y.

Après la passe i, x est le dernier élément. Il est donc trivialement d-progressif.

Cas 3.B: ⋯ x—y z et x > y.

Après la passe i, nous avons ⋯ y x—z. Si x > z, alors x est d-progressif.
Si x ≤ z, alors x est aussi d-progressif comme les éléments à sa droite lui
sont supérieurs ou égaux.

Cas 3.C: ⋯ x—y z—w ⋯ et x > y.

Après la passe i, nous avons ⋯y x—min(z, w) max(z, w)⋯. Si, x > min(z, w)
alors x est d-progressif. Sinon, x ≤ z et x ≤ w. En particulier, w est donc
l'un des i-1 plus grands éléments. Par hypothèse d'induction, il était
d-progressif. Ainsi, tous les éléments à sa droite lui étaient supérieurs
ou égaux. Par conséquent, tous les éléments à la droite de x lui sont
maintenant supérieurs ou égaux. Ainsi, x est d-progressif.

Cas 4: ⋯ y—x ⋯.

Si y ≤ x, alors après la passe i nous avons ⋯y x⋯ [OK, ce cas se gère...]

Si y > x

Avant:  y—z x ⋯
Avant:  ⋯ y—x ⋯
Après:   ⋯x y⋯

---

Cas 4: ⋯ x—y z⋯.

Si x ≤ y, alors y est l'un des i-1 plus grands éléments. Par hypothèse d'induction,
il est donc d-progressif. Donc, tous les éléments à la droite de y lui sont
supérieurs ou égaux. Ainsi, après la passe i, x est d-progressif.

Supposons donc que x > y. Après la passe i, nous avons:

  ⋯ y—x w⋯

Si, x > w, alors x est d-progressif. Autrement, nous avons x ≤ w.



alors après la passe i, nous avons


, alors après la passe i, nous avons:

Après la passe i, il y a deux scénarios possibles.


Deuxième cas: après l'exécution de la passe i, y est le premier élément
et nous avons

  y z--...

Avant l'exécution, nous avions:

  y--z ...
  
Si y > z

Deuxième cas: après l'exécution de la passe i nous avons

  ... y--z ...

Si y > z, ou si y ≤ z et z est le dernier élément, alors y est d-progressif.

Sinon, y ≤ z et il y a au moins un élément à droite de z. Remarquons que
z est l'un des i-1 plus grands éléments. Avant la passe i, z était ou bien
à cette même position, ou bien une position plus à droite. Dans les deux
cas, par hypothèse d'induction, cela implique que z est maintenant
inférieur ou égal à tous les éléments à sa droite. Par conséquent,
c'est aussi le cas de y. Ainsi, y est d-progressif.

Troisième cas: après l'exécution de la passe i nous avons

  ... x--y ...


Dans ce cas, x est trivialement d-progressif.

Quatrième cas: 


```
Proposition A. Si x ≤ y, alors fₐ(x) ≤ fₐ(y).
```

Nous prouvons la proposition en considérant tous les cas.

* Cas _x < a_ et _y < a_. Nous avons _fₐ(x) = 0 = fₐ(y)_.
* Cas _x < a_ et _y = a_. Nous avons _fₐ(x) = 0 ≤ 1 = fₐ(y)_.
* Cas _x = a_ et _y = a_. Nous avons _fₐ(x) = 1 = fₐ(y)_.
* Cas _x = a_ et _y > a_. Nous avons _fₐ(x) = 1 ≤ 2 = fₐ(y)_.
* Cas _x > a_ et _y > a_. Nous avons _fₐ(x) = 2 = fₐ(y)_. □

```
Proposition B. Soit s une séquence d'entiers et soit a un élément de s. Si l'algorithme, sur entrée fₐ(s),
termine en k passes, alors l'algorithme, sur entrée s, fixe l'élément a en k passes.
```

Remarquons que si (i, j) est une inversion de s, alors (i, j) est une inversion de fₐ(s). En effet, par la
proposition A, si s[i] > s[j], alors fₐ(s[i]) > fₐ(s[j])...
