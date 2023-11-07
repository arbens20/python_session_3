import copy


#Récupérer toutes les valeurs d'un dictionnaire :

def recup_val():
    dictionnaire = {"a": 1, "b": 2, "c": 3}
    valeurs = list(dictionnaire.values())
    print(valeurs)
    
recup_val()


#Vérifier si une chaîne a des accolades avant et après :

def a_des_accolades(chaine):
    return chaine.startswith("{") and chaine.endswith("}")


#Récupérer toutes les clés d'un dictionnaire :
def cle_dict():
    dictionnaire = {"a": 1, "b": 2, "c": 3}
    cles = list(dictionnaire.keys())
    print(cles)
    
    
cle_dict()

#Récupérer toutes les valeurs d'un dictionnaire :

def recup_val():
    dictionnaire = {"a": 1, "b": 2, "c": 3}
    valeurs = list(dictionnaire.values())
    print(valeurs)
    
    
recup_val()


#Créer une copie d'un dictionnaire :

def copie_dict():

    dictionnaire_original = {"a": 1, "b": 2}
    dictionnaire_copie = copy.copy(dictionnaire_original)
    print(dictionnaire_copie)
    
copie_dict()


#Ajouter des traits de soulignement avant et après les valeurs de type chaîne dans un dictionnaire :

def ajout():
    dictionnaire = {"name": "Lubens", "age": 44, "assets": ["laptop", "phone"]}
    dictionnaire_modifie = {cle: f"_{valeur}_" if isinstance(valeur, str) else valeur for cle, valeur in dictionnaire.items()}
    print(dictionnaire_modifie)
    
    
ajout()

# nouveau dictionnaire 
def nouveau_dict():
    dictionnaire_original = {"a": 1, "b": "deux", "c": 3, "d": "quatre"}

    dictionnaire_numerique = {cle: valeur for cle, valeur in dictionnaire_original.items() if isinstance(valeur, (int, float))}

    print(dictionnaire_numerique)
    
    
nouveau_dict()