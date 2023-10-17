***En construction***

# Tri pair-impair

```
Proposition ?. Au début de la passe i+1, les i plus grands éléments sont d-progressifs.
```

Soit y l'un des i plus grands éléments au début de la passe i. Nous devons montrer que y
est d-progressif après l'exécution de la passe i.

Premier cas: après l'exécution de la passe i, y est
complètement à droite.

Dans ce cas, y est trivialement d-progressif.

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
