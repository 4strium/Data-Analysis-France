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



resultat1 = ajouter_dictionnaire(file_name, liste_des_descripteurs)


print('--------------------------------------------------------------------------------------------------------------------------------------')
lang = int(input('Select your langage (0 = english (default) / 1 = français) :\n'))

if lang == 1 :
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

    print('--------------------------------------------------------------------------------------------------------------------------------------')
    print('Voulez-vous exporter les résultats ? ( OUI / NON )\n')
    question_export = 'forloop'
    while True :
        question_export = str(input())
        if question_export == 'OUI' or question_export == 'NON' or question_export == 'oui' or question_export == 'non':
            break
    if question_export == 'OUI' or question_export == 'oui' :
        print('--------------------------------------------------------------------------------------------------------------------------------------')
        question_export_name = str(input('Sous quel nom de fichier voulez-vous exporter le résultat ? \n'))
        print('--------------------------------------------------------------------------------------------------------------------------------------')
        print('Toutes les données = 0 / Juste celles qui correspondent à ma recherche = 1')
        print("Quelle type d'exportation voulez-vous réaliser ?\n")
        question_export_type = 2
        while True :
            question_export_type = int(input())
            if question_export_type == 0 or question_export_type == 1 :
                break
        if  question_export_type == 0 :
            export_condition = resultat1
            ecrire_fichier_csv (question_export_name, export_condition)
        elif question_export_type == 1 :
            export_condition = resultat2
            ecrire_fichier_csv (question_export_name, export_condition)
        else :
            print('Exportation impossible.')

else :
    print('--------------------------------------------------------------------------------------------------------------------------------------')
    print('Department = 0 / Real name = 1 / Postal code = 2 / Municipality number = 3 / District = 4 / Population in 2012 = 5')
    question_desc = int(input('Please enter the number corresponding to your search mode:\n'))
    desc_cherche = liste_des_descripteurs[question_desc]
    print('--------------------------------------------------------------------------------------------------------------------------------------')
    print('Please enter the value of the data sought (',desc_cherche,') :')
    question_value = input()
    valeur_cherche = str(question_value)

    resultat2 = affiche_donnes(resultat1, desc_cherche, valeur_cherche)

    print('--------------------------------------------------------------------------------------------------------------------------------------')
    print('Here is the result of your search:\n',resultat2)

    print('--------------------------------------------------------------------------------------------------------------------------------------')
    print('Do you want to export the results? ( YES / NO )\n')
    question_export = 'forloop'
    while True:
        question_export = str(input())
        if question_export == 'YES' or question_export == 'NO' or question_export == 'yes' or question_export == 'no':
            break
    if question_export == 'YES' or question_export == 'yes' :
        print('--------------------------------------------------------------------------------------------------------------------------------------')
        question_export_name = str(input('Under what file name do you want to export the result? \n'))
        print('--------------------------------------------------------------------------------------------------------------------------------------')
        print('All data = 0 / Just those that match my search = 1')
        print("What kind of export do you want to do?\n")
        question_export_type = 2
        while True :
            question_export_type = int(input())
            if question_export_type == 0 or question_export_type == 1 :
                break
        if  question_export_type == 0 :
            export_condition = resultat1
            ecrire_fichier_csv (question_export_name, export_condition)
        elif question_export_type == 1 :
            export_condition = resultat2
            ecrire_fichier_csv (question_export_name, export_condition)
        else :
            print('Unable to export.')