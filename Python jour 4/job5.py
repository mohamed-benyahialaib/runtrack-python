def valeur(liste, index):
   if index > 0 and index < len(liste) - 1:
      remplacer_valeur = liste[index - 1] + liste[index + 1]
      liste[index] = remplacer_valeur

L = [1, 2, 3, 4, 5]

deuxième_valeur = L[1]
print(L, deuxième_valeur)

valeur(L, 3)
print(L)

dernière_valeur = L[-1]
print(dernière_valeur)