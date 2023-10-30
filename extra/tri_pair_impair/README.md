***En construction***

# Tri pair-impair

Dans le reste du billet, nous considérons que _s_ est une séquence d'entiers distincts.

## Suivre le progrès d'un élément en particulier

À titre d'exemple, considérons la séquence _s = [`10`, `40`, `30`, `50`, `20`]_ et l'élément _x = `30`_. Afin de suivre l'évolution de _x_, on peut
substituer tous les éléments inférieurs à _x_ par `0`, tous les éléments supérieurs à _x_ par `2`, et _x_ par `1`. Appelons cette séquence _fₓ(s)_.
Nous avons _fₓ(s) = [`0`, `2`, `1`, `2`, `0`]_. Regardons l'exécution de l'algorithme de tri sur ces deux entrées:

```
Début passe 1:        10↔40 30↔50 20        0↔2 1↔2 0
Début passe 2:        10 40↔30 50↔20        0 2↔1 2↔0
Début passe 3:        10 30↔40 20↔50        0 1↔2 0↔2
Début passe 4:        10↔30 40↔20 50        0↔1 2↔0 2
Début passe 5:        10 30↔20 40↔50        0 1↔0 2↔2
Début passe 6:        10↔20 30↔40 50        0↔0 1↔2 2
```

On observe que l'algorithme préserve la transformation _fₓ_ dans le sens où la position des éléments inférieurs, égaux et supérieurs à _x_ correspond
toujours à des occurrences de `0`, `1` et `2`. Plus formellement, nous avons:

***Proposition A.*** *Soit _s'_ la séquence obtenue après l'exécution de _k_ passes sur _s_, et soit _s''_ la séquence
obtenue après l'exécution de _k_ passes sur _fₓ(s)_. Nous avons _fₓ(s') = s''_.*

Ainsi, afin de suivre le progrès de _x_ dans _s_, il suffit de suivre le progrès de `1` dans _fₓ(s)_.

Un élément est _progressif_ si...

***Proposition B.*** *Sur entrée _fₓ(s)_, au début de la passe _i+1_, les _i_ occurrences de `2` les plus à droite sont progressives.*

*Démonstration.* Nous procédons par induction sur _i_.

Si _i = 1_, alors il faut considérer l'occurrence de `2` la plus à droite. Si elle est à la fin de la
séquence, alors elle ne bougera plus jamais, ce qui la rend immédiatement progressive. Si elle
est suivie d'un `0` ou `1`, alors l'occurrence de `2` est ou bien déjà progressive ou bien le sera à la passe
suivante.

Soit _i > 1_ et soit _j ∈ [1..i]_. Considérons la _j_-ème occurrence de `2` la plus à droite avant la passe _i_.
Regardons où elle se déplace après la passe. Si tous les éléments à sa droite sont des `2`, alors
elle ne bouge pas et nous avons donc terminé. Supposons donc qu'il existe au moins un élément inférieur à sa droite.
Par hypothèse d'induction, toutes les occurrences de `2` à sa droite sont progressives.

Nous utilserons ces notations:

* `x*` afin de dénoter le motif `x` répété zéro, une ou plusieurs fois;
* `xᙾ` afin de dénoter le motif `x` répété un nombre pair de fois (possiblement nul);
* `⌀` afin de dénoter un chiffre parmi `0` et `1`.

En inspectant les dispositions possibles, on remarque, qu'après la passe _i_, la _j_-ème occurrence
devient en effet progressive:

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

***Proposition C.*** *La séquence _fₓ(s)_ est triée en au plus _2n_ passes.*

*Démonstration.* Soit _k_ la quantité de `2`. Par la proposition B, au début de la passe _k+1_, tous les `2` sont
progressifs. Ainsi, en au plus _k_ autres passes, tous les `2` sont bien positionnés, et ainsi la séquence devient
de cette forme:

```
 0* 1 0* 2 ⋯ 2.
         ^^^^^
         k fois
```

Après une autre passe, l'occurence de `1` est forcément progressive. Ainsi, en au plus _n - k - 1_ autres passes,
la séquence devient triée.

Au total, nous effectuons donc au plus _k + k + 1 + (n - k - 1) = n + k ≤ 2n_ passes. □

## Temps d'exécution de l'algorithme

***Proposition D.*** *Soit _x_ un élément de _s_. Si l'algorithme, sur entrée _fₓ(s)_, termine en _k_ passes, alors l'algorithme,
sur entrée _s_, fixe l'élément _x_ en _k_ passes.*

Démonstration. Imaginons que l'on exécute l'algorithme sur entrée __s d'une part, et sur entrée _fₓ(s)_ d'autre part. Appelons  _s'_
et _s''_ les séquences obtenues après _k_ passes des deux exécutions respectives. Par la proposition A, nous avons _fₓ(s') = s''_.
Par hypothèse, _s''_ est triée. Ainsi la position de l'unique `1` dans _s''_ correspond à la position de _x_ dans _s'_. Par conséquent,
tous les éléments à la droite de _x_ sont plus grands que lui, et tous les éléments à la droite de _x_ sont plus petits que lui.
Il ne bougera donc plus jamais. □

***Théorème.*** *L'algorithme trie s en au plus _2n_ passes.*

*Démonstration.* Soit _x_ un élément de _s_. Par la proposition C, la séquence _fₓ(s)_ est triée en au plus _2n_ passes.
Par la proposition D, cela signifie que, sur entrée _s_, l'algorithme fixe _x_ en au plus _2n_ passes. □

## Détails

***Lemme A.*** *Si _a ≤ b_, alors _fₓ(a) ≤ fₓ(b)_.*

*Démonstration.* Nous prouvons la proposition en considérant tous les cas.

* Cas _a < x_ et _b < x_. Nous avons _fₓ(a) = 0 = fₓ(b)_.
* Cas _a < x_ et _b = x_. Nous avons _fₓ(a) = 0 ≤ 1 = fₓ(b)_.
* Cas _a = x_ et _b = x_. Nous avons _fₓ(a) = 1 = fₓ(b)_.
* Cas _a = x_ et _b > x_. Nous avons _fₓ(a) = 1 ≤ 2 = fₓ(b)_.
* Cas _a > x_ et _b > x_. Nous avons _fₓ(a) = 2 = fₓ(b)_. □
  
***Lemme B.*** *Soient _x_ un élément et _i_ une position de _s_. Soit _s'_ la séquence obtenue en corrigeant _(i, i+1)_ au besoin dans _s_.
Soit _s''_ la séquence obtenue en corrigeant _(i, i+1)_ au besoin dans _fₓ(s)_. Nous avons _s'' = fₓ(s')_.*



