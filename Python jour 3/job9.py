def moyenne(note1, note2, note3):
    moyenne_etudiant=((note1+note2+note3)/3)
    print(moyenne_etudiant)
    if 0 <= moyenne_etudiant <= 7:
        print("élève devrait faire des efforts si la moyenne est comprise entre 0 et 7.")
    elif 8 <= moyenne_etudiant <=  10:
        print("élève moyen si la moyenne est comprise entre 10 et 8")
    elif 11 <= moyenne_etudiant <= 14:
        print("bon élève si la moyenne est comprise entre 11 et 14")
    elif 15 <= moyenne_etudiant <= 20:
        print("très bon élève si la moyenne est comprise entre 15 et 20")
    else:
        if -0.0001>moyenne_etudiant or moyenne_etudiant>20:
            print("la moyenne doit être comprise entre 0 et 20")
            
moyenne(10,8,14)
moyenne(15.3,14,15.5)
moyenne(0,15,4)
moyenne(20,20,19)
moyenne(100,129,48)