##### IMPORT
import random
import time

lettres_trouvees = set()
coups = 0
lettres_deja_essayees = set()
coups_ratés = 0

#####Main

with open("mots.odt", "r", encoding="utf-8") as f:
    mots = [ligne.strip() for ligne in f]

mot_secret = random.choice(mots)

affichage = "".join([lettre if lettre in lettres_trouvees else "_" for lettre in mot_secret])
print("Mot :", affichage)
        
while True:
    print("")
    lettre = input("Entrez une lettre : ").strip().upper()

    if lettre in lettres_deja_essayees:
        print("Vous avez déjà essayé cette lettre. Essayez une autre.")
        continue

    if not len(lettre) == 1 and lettre.isalpha():  # Vérifie que c'est une lettre
        print("Erreur ! Vous devez entrer UNE seule lettre.")
        continue
    

    if lettre in mot_secret:
        print("Bonne réponse ! 🎉")
        lettres_trouvees.add(lettre)  # Ajoute la lettre trouvée
    else:
        print("Mauvaise réponse. ❌")
        coups_ratés += 1
        
    coups += 1
    lettres_deja_essayees.add(lettre)

    affichage = "".join([lettre if lettre in lettres_trouvees else "_" for lettre in mot_secret])
    
    print("Mot :", affichage)

    if "_" not in affichage:
        print("🎉Félicitations, vous avez trouvé le mot en " + str(coups) + " coups !🎉")
        print("Vous avez fait " + str(coups_ratés) + " erreurs!")
        pourcentage_reussite = (len(lettres_trouvees) / coups) * 100
        print("Pourcentage de réussite : " + str(pourcentage_reussite) + "%")
        break
    
time.sleep(5)
