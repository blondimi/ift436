# Installer z3 avec «bindings» pour Python: https://github.com/Z3Prover/z3
# (ou bien tenter "sudo apt-get install z3" sur Ubuntu/Debian)
import z3

solveur = z3.Optimize()

# Déclare trois variables entières (identifiées par une chaîne unique)
x = z3.Int("x") # nombre de pièces valant 1
y = z3.Int("y") # nombre de pièces valant 5
z = z3.Int("z") # nombre de pièces valant 7

# On ne peut pas retourner un nombre négatif de pièces
solveur.add(x >= 0)
solveur.add(y >= 0)
solveur.add(z >= 0)

# On cherche à rendre 10 unités d'argent...
solveur.add(1*x + 5*y + 7*z == 10)

# ... avec le moins de pièces possible
objectif = solveur.minimize(x + y + z)

# Solution?
solveur.check()
print("Pièces utilisées:", solveur.model())
print("Nombre de pièces:", solveur.lower(objectif))
