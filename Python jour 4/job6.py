def echange_de_valeur(liste):
    if len(liste) >= 2:
        liste[0], liste[-1] = liste[-1], liste[0]

liste = [1, 2, 3, 4, 5]
print(liste)
echange_de_valeur(liste)
print(liste)