***En construction***

# Tri pair-impair

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
