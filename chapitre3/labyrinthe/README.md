# Génération de labyrinthe

## Version script

Afin de générer un labyrinthe en PDF:

1. Convertir la grille en LaTeX: `python3 exporter.py > labyrinthe.tex`
2. Compiler: par ex.             `pdflatex labyrinthe.tex`
3. Ouvrir `labyrinthe.pdf`

_La compilation requiert le package TikZ pour LaTeX._

## Version web

L'algorithme peut être testé sur [cette page](http://info.usherbrooke.ca/mblondin/ift436/labyrinthe/) ou en lançant `labyrinthe.html` localement.