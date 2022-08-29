def mesure_centralite(sommets, adj, poids):
    # (a) Enraciner l'arbre (c.-à-d. extraire un arbre dirigé)
    racine = sommets[0]
    marque = {v: False for v in sommets}
    adj_   = {v: []    for v in sommets}

    def enraciner(v):
        marque[v] = True

        for w in adj[v]:
            if not marque[w]:
                adj_[v].append(w)
                enraciner(w)

    enraciner(racine)
    adj = adj_

    # (b) Calculer nombre descendants taille[v] du sous-arbre enraciné en v
    taille = {v: None for v in sommets}
    
    def calculer_taille(v):
        n = 1

        for w in adj[v]:
            calculer_taille(w)
            n += taille[w]
            
        taille[v] = n

    calculer_taille(racine)

    # (c) Calculer la mesure de centralité de la racine
    mesure = {v: None for v in sommets}

    def calculer_mesure_sousarbre(v):
        m = 0
        
        for w in adj[v]:
            m += calculer_mesure_sousarbre(w) + poids[v, w] * taille[w]

        return m

    mesure[racine] = calculer_mesure_sousarbre(racine)

    # (d) Calculer la mesure de centralité des autres sommets
    def calculer_mesure(v, parent):
        if parent != None:
            taille_sans_v = len(sommets) - taille[v]
            diff_mesure   = poids[parent, v] * (taille_sans_v - taille[v])
            mesure[v]     = mesure[parent] + diff_mesure

        for w in adj[v]:
            calculer_mesure(w, v)

    calculer_mesure(racine, None)

    # (e) Retourner les mesures    
    return mesure

# Exemples
if __name__ == "__main__":
    # Exemple des notes de cours
    sommets = [1, 2, 3, 4]
    adj     = {1: [2, 3],
               2: [1],
               3: [1, 4],
               4: [3]}
    poids   = {(1, 2): 3, (2, 1): 3,
               (1, 3): 1, (3, 1): 1,
               (3, 4): 2, (4, 2): 2}

    print(mesure_centralite(sommets, adj, poids))

    # Exemple de https://leetcode.com/problems/sum-of-distances-in-tree/
    sommets = [0, 1, 2, 3, 4, 5]
    adj     = {0: [1, 2],
               1: [0],
               2: [0, 3, 4, 5],
               3: [2],
               4: [2],
               5: [2]}
    poids   = {(u, v): 1 for u in sommets for v in adj[u]}

    print(mesure_centralite(sommets, adj, poids))
