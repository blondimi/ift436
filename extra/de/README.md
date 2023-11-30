
# Dé à six faces: analyse à l'aide d'un graphe de probabilités

Rappelons qu'en classe, nous avons implémenté algorithmiquement 
un dé à six faces à l'aide d'une pièce (non biaisée):

```
faire:
  choisir un bit y₀ avec la pièce
  choisir un bit y₁ avec la pièce
  choisir un bit y₂ avec la pièce
tant que y₀ = y₁ = y₂

retourner 2²·y₂ + 2¹·y₁ + 2⁰·y₀
```

## Analyse à l'aide d'un graphe de probabilités

En classe (A23), j'ai tenté en vain d'analyser la probabilité que
l'algorithme génère un nombre en particulier, à l'aide de ce graphe
de probabilités (mieux connu sous le nom savant de _[chaîne de Markov à temps
discret](https://fr.wikipedia.org/wiki/Cha%C3%AEne_de_Markov)_):

```                                  
  ┌─────────────────▸ (???) ◂─────────────────┐
  │             ½ ↙           ↘ ½             │
 ½│        (??0)                 (??1)        │½
  │     ½ ↙     ↘ ½           ½ ↙     ↘ ½     │
  └───(?00)     (?10)       (?01)     (?11)───┘
       ½↓      ½ ↙ ↘ ½     ½ ↙ ↘ ½      ↓½
      (100)  (010) (110) (001) (101)  (011)
```

Ici, chaque sommet de la forme ```(abc)``` indique que le bit _a_ a été
assigné à la variable _y₂_, que le bit _b_ a été assigné à la
variable _y₁_, et , que le bit _c_ a été assigné à la variable _y₀_,
où ```?``` signifie que rien n'a été assigné.

### Cycles

Voici une analyse qui fonctionne. Cherchons à identifier la
probabilité de débuter dans le sommet ```???``` et d'atteindre le
sommet ```100``` qui correspond au verdict ```4```. Il est possible
d'utiliser les cycles simples ```??? → ??0 → ?00 → ???``` et
```??? → ??1 → ?11 → ???``` un certain nombre de fois. Appelons ces deux
cycles ```g``` et ```d```. Il y a plusieurs façons de combiner ces cycles, par
ex. ```gddg``` indique qu'on tourne d'abord à gauche, puis deux fois à
droite, puis une dernière fois à gauche. Le nombre de façons de concaténer
_n_ cycles avec exactement _k_ occurrences de ```g``` correspond à [_k
parmi n_](https://fr.wikipedia.org/wiki/Coefficient_binomial). Par
exemple, pour _n = 4_ et _k = 2_, six choix s'offrent à nous:

```
ggdd
ddgg
gdgd
dgdg
gddg
dggd
```

De plus, la probabilité de produire un ```g```, c.-à-d. de choisir le
cycle de gauche, est de _1/2 · 1/2 · 1/2 = 1/8_. Similairement, la
probabilité de produire un ```d```, c.-à-d. de choisir le cycle de
droite, est de _1/8_.

### Probabilité d'obtenir ```4```

Pour atteindre le sommet ```100``` à partir du sommet ```???```, on doit:

* débuter en ```???``` et y revenir en combinant les deux cycles _n_
  fois en utilisant _k_ fois le cycle de gauche (pour certains _n_,
  _k_);
* suivre les trois arêtes vers le bas et la gauche: ```??? → ??0 → ?00 → 100```.

La probabilité d'obtenir ```4``` est donc de:

```
     ∞     n
    \¯¯   \¯¯     /n\ 
    /__   /__     \k/ · (1/8)ᵏ · (1/8)ⁿ⁻ᵏ · (1/2) · (1/2) · (1/2)
   n = 0 k = 0

            ∞     n
           \¯¯   \¯¯     /n\
= (1/8) ·  /__   /__     \k/ · (1/8)ᵏ · (1/8)ⁿ⁻ᵏ
           n = 0 k = 0

             ∞  
            \¯¯ 
= (1/8) ·   /__   (1/8 + 1/8)ⁿ    [par la formule du binôme de Newton avec x = 1/8 et y = 1/8]
           n = 0

               1  
= (1/8) ·  ---------              [car série géométrique de raison 2/8]
           (1 - 2/8)

= (1/8) · (4/3)

= 1/6.
```

Le raisonnement pour les cinq autres valeurs est similaire. Dans tous les cas, on obtient _1/6_ comme attendu.

### Liens

- [Formule du binôme de Newton](https://fr.wikipedia.org/wiki/Formule_du_binôme_de_Newton)
- [Séries géométriques](https://fr.wikipedia.org/wiki/S%C3%A9rie_g%C3%A9om%C3%A9trique)
