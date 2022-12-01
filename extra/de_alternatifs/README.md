# Simuler un dé à 6 faces: autres tentatives

Rappelons que le chapitre 8 présente cet algorithme afin de simuler un
dé à 6 faces à l'aide d'une pièce (non biaisée):

```
Entrée: —
Sortie: nombre distribué uniformément parmi [1..6]

  faire:
    choisir un bit y₂ à pile ou face
    choisir un bit y₁ à pile ou face
    choisir un bit y₀ à pile ou face
  tant que y₂ = y₁ = y₀

  retourner 4·y₂ + 2·y₁ + y₀
```

En classe (A22), des personnes ont suggéré des approches
alternatives pour gérer le cas où ``y₂ = y₁ = y₀``.

## Alternative 1

Dans la première approche alternative, on ne repige que ``y₂`` en cas
d'égalité:

```
Entrée: —
Sortie: nombre distribué uniformément parmi [1..6]

  choisir un bit y₂ à pile ou face
  choisir un bit y₁ à pile ou face
  choisir un bit y₀ à pile ou face

  tant que y₂ = y₁ = y₀:
    choisir un bit y₂ à pile ou face

  retourner 4·y₂ + 2·y₁ + y₀
```

La probabilité de générer 4, c.-à-d. la chaîne 100, n'est pas de 1/6,
mais bien de 1/4:

```
obtenir directement 100
    |
    | ou obtenir 000 puis remplacer le bit de poids fort
    |        |          en 1 ou 2 ou 3 ou ... itérations
    v        v
  (1/2)³ + (1/2)³ · ((1/2)¹ + (1/2)² + (1/2)³ + ...)
  
= 1/8 + 1/8 · 1

= 1/4
```

Néanmons, l'espérance du nombre de lancers de pièces est de 3.5, ce
qui est mieux que l'algorithme vu en classe dont l'espérance est 4:

```
           nombre de lancers initiaux
               |
               | probabilité d'obtenir 000 ou 111
               |     |
               |     |   espérance de la boucle
               |     |         |
               |     |         |
               v    vvv    vvvvvvvvvvvv
E[# lancers] = 3 + (1/4) · (1 / (1 / 2))
             = 3 + (1/4) · 2
             = 3.5
```

Pour les personnes intéressées, voici une modélisation dans le langage
de l'outil [PRISM](http://www.prismmodelchecker.org/):
``[sol2.prism](sol2.prism)``, ``[propietes.pctl](proprietes.pctl)``.