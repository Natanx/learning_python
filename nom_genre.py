#Demander à l'utilisateur son nom et son sexe (M ou F). En fonction de ces données, afficher « Cher Monsieur » ou « Chère Mademoiselle » suivi du nom de la personne.

a, b = input("Quel est votre nom ? "), input("Veuillez préciser votre sexe. M pour mâle et F pour femelle. ")

if b=="M":
    print("Cher Monsieur ", a)
else:
    print("Chère Madame ", a)
