


#1 mete tou let en miniskil
def minuscule():
    # phrase = input('Entrer la phrase : ')
    phrase =('HELLO WORD')
    result = phrase.lower()
    print (result)


minuscule()


#2 koupe chenn lan tout kote ki gen espace
def cut_string():
    # phrase = input('Entrer la phrase : ')
    phrase =('HELLO WORD welcome to the party')
    result = phrase.split()
    print (result)



cut_string()


# 3 mete premye let chak mo an majiskil

def premye_mo_majiskil():
    # phrase = input('Entrer la phrase : ')
    phrase =('Hello world, welcome to the party')
    result = ' '.join(word.capitalize() for word in phrase.split() )
    print(result)
  
  
premye_mo_majiskil()  
    
# 4 rekipere premye let chak mo

def rekipere_premye_let():
    # phrase = input('Entrer la phrase : ')
    phrase =('Hello world, welcome to the party')
    result = ''.join(word[0] for word in phrase.split())
    print(result)




rekipere_premye_let()



# 5 Ranplase tout karakte "a" ak "@"

def ranplase_let_a():
    # phrase = input('Entrer la phrase : ')
    phrase =('Nous avons avec Nous au bord de la piscine mr andre')
    result = phrase.replace('a','@')
    print(result)
    
    
ranplase_let_a()

# 6 mete let an majiskil
def majiskil():
    # phrase = input('mete fraz lan : ')
    phrase = (" il faut ebtreprendre et innover")
    result = phrase.upper()
    print(result)
    
    
majiskil()


# 7 Jwenn index premye a

def jwenn_index():
     # phrase = input('Entrer la phrase : ')
    phrase =('Nous avons avec Nous au bord de la piscine mr andre')
    result = phrase.find('a')
    print(result)
    
jwenn_index()


# 8 jwenn index tout a yo

def jwenn_index_tout_a():
     # phrase = input('Entrer la phrase : ')
    phrase =('Nous avons avec Nous au bord de la piscine mr andre')
    result =phrase.lower().count("a")
    print(result)
    
jwenn_index_tout_a()



# 9 tout index a minuscule
def a_min():
     # phrase = input('Entrer la phrase : ')
    phrase =('Nous avons avec Nous au bord de la piscine mr andre')
    result =[i for i, char in enumerate(phrase) if char == "a"]
    print(result)
    
a_min()

# 10 supprimer espace
def supp_space():
     # phrase = input('Entrer la phrase : ')
    phrase =('Nous avons avec Nous au bord de la piscine mr andre')
    result =phrase.replace(" ", "") + str(len(phrase) - phrase.count(" "))
    print(result)
    
supp_space()