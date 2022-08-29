# Problème de maximisation de cours pour une unique salle

Rappelons le problème de la question 4(c) de l'examen périodique de
2020. Étant donné un horaire de cours _H = [(i₁, j₁), ... (iₙ, jₙ)]_,
nous cherchons à déterminer la quantité maximale de cours que l'on
peut assigner à une unique salle sans créer de conflit. Par exemple,
si _H = [(0, 3), (2, 4), (3, 6)]_, alors la solution optimale est
_[(0, 3), (3, 6)]_ et ainsi la valeur optimale est _2_.

Afin de simplifier la notation, étant donné un cours _c = (i, j)_,
définissons _début(c) := i_ et _fin(c) := j_.  Tel qu'annoncé dans le
solutionnaire de l'examen, il est possible de résoudre le problème à
l'aide de cette approche gloutonne:

```
S ← ∅

tant que H n'est pas vide:
  sélectionner c ∊ H tel que fin(c) est minimal dans H
  retirer c de H
  
  si c ne crée pas de conflit dans S:
    ajouter c à S
    
retourner |S|
```

Dans le reste de ce billet, nous allons montrer que cet algorithme
fonctionne correctement. Rappelons qu'on ne devait pas donner une
telle preuve à l'examen, et que cela dépasse nettement le niveau
attendu, même dans un devoir!

## Observations 

Soit _S*_ une solution optimale et soit _S_ une solution retournée par
l'algorithme glouton. Soient _c₁, ..., c<sub>|S|</sub>_ les cours dans
l'ordre où ils ont été ajoutés à _S_ par l'algorithme
glouton. Remarquons d'abord que:

* Si _S* ⊆ S_, alors _S_ est aussi optimale et nous avons
  terminé. Autrement, il existe _c* ∊ S* ∖ S_. Choisissons un tel _c*_
  qui minimise _début(c*)_.
* Si _S ⊆ S*_, alors il y a une contradiction, car l'algorithme
  glouton aurait pu ajouter plus de cours à _S_ sans créer de
  conflit. Ainsi, il existe _cₖ ∊ S ∖ S*_. Choisissons le premier tel
  indice _k_.

```
Proposition 1. fin(cₖ) ≤ fin(c*).
```

Nous faisons les observations suivantes:

* Les cours _c₁, ..., c<sub>k-1</sub>_ appartiennent tous à _S*_ (par
  minimalité de _k_);
* Aucun des cours _c₁, ..., c<sub>k-1</sub>_ n'est _c*_ (car _c*_
  n'appartient pas à _S_);
* Le cours _c*_ n'est pas en conflit avec les cours _c₁, ...,
  c<sub>k-1</sub>_ (car _S*_ les contient tous et est une solution);

Par ces observations, nous déduisons que _fin(cₖ) ≤ fin(c*)_, car
autrement l'algorithme glouton aurait sélectionné _c*_ plutôt que
_cₖ_. □

## Changement de solution

```
Proposition 2. L'ensemble S** := S* ∖ {c*} ∪ {cₖ} est une solution optimale.
```

Clairement, si _S**_ est une solution, alors elle est optimale car
elle possède la même taille que _S*_.  Il suffit donc de montrer que
_cₖ_ n'est en conflit avec aucun cours de _S* ∖ {c*}_.

Soit _d* ∊ S* ∖ {c*}_. Nous devons montrer que _cₖ_ et _d*_ ne sont
pas en conflit.  Si _d* ∊ S_, alors nous avons terminé car _S_ ne
contient pas de conflit. Considérons donc le cas où _d* ∉ S_.  Par
minimalité de _début(c*)_, nous avons _début(c*) ≤ début(d*)_. Comme
_c*_ et _d*_ appartiennent tous deux à _S*_, ils ne sont pas en
conflit. Ainsi, _fin(c*) ≤ début(d*)_.  Par la proposition 1, nous
avons _fin(cₖ) ≤ fin(c*)_. Nous obtenons donc _fin(cₖ) ≤ fin(c*) ≤
début(d*)_, ce qui signifie que _cₖ_ et _d*_ ne sont pas en conflit. □

## Correction

```
Théorème. L'algorithme est correct.
```

Par la proposition 2, nous pouvons convertir la solution optimale _S*_
en une autre solution optimale _S**_ qui possède un cours de plus en
commun avec _S_. Ainsi, en répétant cet argument un nombre fini de
fois, on obtient une solution optimale _S**<sup>…</sup>*_ égale à
_S_. Par conséquent, _S_ est optimale. □
