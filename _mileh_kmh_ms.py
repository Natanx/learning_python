#L'utilisateur entre sa vitesse en miles/h et il s'agit de convertir la valeur en km/h puis en m/s puis de la retourner à 
#l'utilisateur

mile = input ("Votre vitesse en miles/h : ")
km = float(mile)*1.609
ms = km/3.6

print("Vous allez donc à une vitesse de ",km," km/h ou encore mieux ! A ",ms," m/s !")
