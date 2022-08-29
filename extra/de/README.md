# Simuler un dé à 6 faces avec un lancer de pièce par itération

Rappelons qu'en classe un étudiant a demandé si l'algorithme ci-dessous
fait mieux que les deux algorithmes du #5(a) de l'[examen final de 2020](https://info.usherbrooke.ca/mblondin/cours/ift436_a21/etude/final_a20.pdf).
Voyons si c'est le cas.

```
Entrée: —
Sortie: nombre distribué uniformément parmi [1..6]

  choisir un bit y₂ à pile ou face
  choisir un bit y₀ à pile ou face
  
  faire:
    choisir un bit y₁ à pile ou face
  tant que y₂ = y₁ = y₀

  retourner 4·y₂ + 2·y₁ + y₀
```

## Espérance du nombre de pièces lancées

Avec probabilité _2·(1/4·1/4) = 1/2_, on pige une chaîne de bits de la forme ```0?1``` ou ```1?0```.
Dans ce cas, il n'y a qu'une seule itération de la boucle à coup sûr.

Avec probabilité _2·(1/4·1/4) = 1/2_, on pige une chaîne de bits de la forme ```0?0``` ou ```1?1```.
Dans ce cas, la probabilité de quitter la boucle est de _1/2_ (car il faut piger le bit inverse). Ainsi,
dans ce cas, le nombre de tours de boucle espéré est _1 / (1/2) = 2_.

Soit _X_ le nombre de pièces lancées par l'algorithme, nous avons:

```
𝔼[X] = 2 + (1/2·1 + 1/2·2) = 2 + 3/2 = 7/2 = 3,5.
```

L'algorithme lance donc moins de pièces en moyenne que les deux
algorithmes de l'examen antérieur (respectivement 4 et 
11/3 = 3,66···). 

## Distribution des sorties

Toutefois, l'algorithme ne simule pas correctement un dé à 6 faces.
En effet, chacune des chaînes de _{```001```, ```011```, ```100```, ```110```}_ est choisie
avec probabilité 1/2·1/2·1/2 = 1/8, et chacune des chaînes de _{```010```, ```101```}_
est choisie avec probabilité 1/4. Par exemple, la probabilité de
choisir ```010``` est:
```
choisir y₂ = 0    choisir y₀ = 0              choisir y₁ = 1
   v                 v                           v
  1/2       ·       1/2       ·       (1/2 + 1/4 + 1/8 + 1/16 + ...)

= 1/4 · ((1 / (1 - 1/2)) - 1)     [série géométrique de raison 1/2 sans le terme (1/2)⁰]

= 1/4 · (2 - 1)

= 1/4.
```

Ainsi, la sortie de l'algorithme est distribuée comme suit:

| *Valeur*      |*Probabilité*|
|:-------------:|:-----------:|
| 1             | 1/8         |
| 2             | 1/4         |
| 3             | 1/8         |
| 4             | 1/8         |
| 5             | 1/4         |
| 6             | 1/8         |
