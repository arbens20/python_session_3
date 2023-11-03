


#1 mete tou let en miniskil
def minuscule():
    phrase = input('Entrer la phrase : ')
    result = phrase.lower()
    print (result)


minuscule()


#2 koupe chenn lan tout kote ki gen espace
def cut_string():
    phrase = input('Entrer la phrase : ')
    result = phrase.split()
    print (result)



cut_string()


# 3 mete premye let chak mo an majiskil

def premye_mo_majiskil():
    phrase = input('Entrer la phrase : ')
    result = ' '.join(word.capitalize() for word in phrase.split() )
    print(result)
  
  
premye_mo_majiskil()  
    
# rekipere premye let chak mo

def rekipere_premye_let():
    phrase = input('Entrer la phrase : ')
    result = ''.join(word[0] for word in phrase.split())
    print(result)




rekipere_premye_let()



# Ranplase tout karakte "a" ak "@"

def ranplase_let_a():
    phrase = input('Entrer la phrase : ')
    result = phrase.replace('a','@')
    print(result)
    
    
ranplase_let_a()
