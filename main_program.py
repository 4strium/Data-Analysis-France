import csv


def ecrire_descripteur_csv(nom_fichier, liste_des_descripteurs):
    file = open(nom_fichier, 'w')
    for i in range(len(liste_des_descripteurs)):
        file.write(liste_des_descripteurs[i] + ";")
    file.write('\n')
    file.close()

def ajouter_dictionnaire(nom_fichier, liste_des_descripteurs):
    liste = []  # Creation d'une liste vide
    file = open(nom_fichier, 'r', encoding='utf-8') # Ouverture du fichier contenant les données à exploiter.
    lignes = file.readlines()   # Lecture de toutes les lignes du fichier CSV
    for i in lignes :
        lst = i.rstrip().split(',') # Supression d'éventuels caractères superflus (ex:"\n",...) puis séparation en ligne à la rencontre d'une virgule (séparateur)
        
        # Dans les lignes suivantes je défini un dictionnaire 'ligne_temp' contenant seulement les données correspondantes aux différents descripteurs de l'exo précédent
        # je récupére alors l'index de chacun des descripteurs dans la liste précedemment créée.
        # La fonction .strip('"') me permet de supprimer d'éventuels guillemets en trop dans les données pour pouvoir effectuer des recherches pertinentes par la suite.
        ligne_temp = {liste_des_descripteurs[0] : lst[1].strip('"'),    
                      liste_des_descripteurs[1] : lst[5].strip('"'),
                      liste_des_descripteurs[2] : lst[8].strip('"'),
                      liste_des_descripteurs[3] : lst[9].strip('"'),
                      liste_des_descripteurs[4] : lst[11].strip('"'),
                      liste_des_descripteurs[5] : lst[16].strip('"')}
        liste.append(ligne_temp)        # J'ajoute chaque dictionnaire dans ma liste finale.
    return liste                        # Je retourne ma liste contenant tous les dictionnaires.

def affiche_donnes(liste, descripteur, valeur):
    tabl_recherche = []
    for i in range(len(liste)):
        for key, value in liste[i].items():
            if key == descripteur and value == valeur:
                tabl_recherche.append(liste[i]) 
    return tabl_recherche 

def ecrire_fichier_csv(nom_fichier, liste) :
    keys = liste[0].keys()
    if nom_fichier.endswith('.csv') == False:
        csv_file =  nom_fichier + '.csv'
    else :
        csv_file =  nom_fichier
    with open(csv_file, 'w', newline='', encoding = 'utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, delimiter = ';')
        dict_writer.writeheader()
        dict_writer.writerows(liste)
    output_file.close()


liste_des_descripteurs = ['Département', 'Nom reel', 'Code postal', 'Numéro de commune', 'Arrondissement', 'Population en 2012']


file_name = 'villes_france.csv'


# Exercice 4 :

resultat1 = ajouter_dictionnaire(file_name, liste_des_descripteurs)


# Exercice 5 :

print('--------------------------------------------------------------------------------------------------------------------------------------')
print('Département = 0 / Nom reel = 1 / Code postal = 2 / Numéro de commune = 3 / Arrondissement = 4 / Population en 2012 = 5')
question_desc = int(input('Veuillez entrer le numéro correspondant à votre mode de recherche :\n'))
desc_cherche = liste_des_descripteurs[question_desc]
print('--------------------------------------------------------------------------------------------------------------------------------------')
print('Veuillez entrer la valeur de la donnée recherchée (',desc_cherche,') :')
question_value = input()
valeur_cherche = str(question_value)

resultat2 = affiche_donnes(resultat1, desc_cherche, valeur_cherche)

print('--------------------------------------------------------------------------------------------------------------------------------------')
print('Voici le résultat de votre recherche :\n',resultat2)


# Exercice 6 :

print('--------------------------------------------------------------------------------------------------------------------------------------')
question_export_name = str(input('Sous quel nom de fichier voulez-vous exporter le résultat ? \n'))
print('--------------------------------------------------------------------------------------------------------------------------------------')
print('Toutes les données = 0 / Juste celles qui correspondent à ma recherche = 1')
question_export_type = int(input("Quelle type d'exportation voulez-vous réaliser ?\n"))

if  question_export_type == 0 :
    export_condition = resultat1
elif question_export_type == 1 :
    export_condition = resultat2
else :
    print('Exportation impossible.')

ecrire_fichier_csv (question_export_name, export_condition)