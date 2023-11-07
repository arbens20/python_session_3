

# pou afficher liste div2 de n

def list_div():
    # n = int(input('mete nomb lan : '))
    n = 10
    liste_divisible_par_2 = [i for i in range(n + 1) if i % 2 == 0]
    print (liste_divisible_par_2)
    
list_div()




#2 Convertir une liste en liste chaînée :
def liste_chaine():
    liste = [1, 2, 3, 4, 5]
    liste_chainee = ' -> '.join(map(str, liste))
    print(liste_chainee)
    
liste_chaine()



#3 Convertir une liste de chaînes en majuscules :

def liste_majiskil():
    liste_minuscules = ["a", "b", "c"]
    liste_majuscules = [mot.upper() for mot in liste_minuscules]
    print(liste_majuscules)
    
liste_majiskil()


#Créer une nouvelle liste avec des éléments à l'indice divisible par 3 :

def div3():
    liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nouvelle_liste = [element for index, element in enumerate(liste) if index % 3 == 0]
    print(nouvelle_liste)
    
div3()


#Regrouper les éléments de la liste par 3 dans des tuples :

def regroupe_3():
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    liste_tuples = [tuple(liste[i:i+3]) for i in range(0, len(liste), 3)]
    print(liste_tuples)
    
regroupe_3()


#Supprimer les doublons d'une liste :

def delete_doublons():
    liste = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7]
    liste_sans_doublons = list(set(liste))
    print(liste_sans_doublons)
    
delete_doublons()


#Trouver les éléments communs entre deux listes :

def element_commun():
    liste1 = [1, 2, 3, 4, 5]
    liste2 = [4, 5, 6, 7, 8]
    elements_communs = list(set(liste1) & set(liste2))
    print(elements_communs)
    
element_commun()


#Trouver les éléments distincts entre deux listes :

def element_distinct():
    liste1 = [1, 2, 3, 4, 5]
    liste2 = [4, 5, 6, 7, 8]
    elements_distincts = list(set(liste1) ^ set(liste2))
    print(elements_distincts)
    
element_distinct()

#Créer une liste des clés et une liste des valeurs à partir d'un dictionnaire :

def liste_dict():
    dictionnaire = {"a": 1, "b": 2, "c": 3}
    cles = list(dictionnaire.keys())
    valeurs = list(dictionnaire.values())
    print(valeurs)
    
liste_dict()


#Joindre trois listes ensemble sans doublons :

def joindre_3listes():
    liste1 = [1, 2, 3]
    liste2 = [3, 4, 5]
    liste3 = [5, 6, 7]
    listegroup = list(set(liste1 + liste2 + liste3))
    print(listegroup)
    
joindre_3listes()


