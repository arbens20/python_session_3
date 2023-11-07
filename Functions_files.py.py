import random
import string
    
#pou inverse mot    
def inverse_mot():
    #mot = input('rentrer le mot : ')
    mot = 'bonjour'
    result = mot[::-1]
    print(result)
    
    
inverse_mot()


#pou genere code alpha
def genere_code_alpha(n):
    ca = ''.join(random.choice(string.ascii_letters) for _ in range(n))
    print(ca)
    
    
#genere_code_alpha(int(input('n')))






def genere_code_sans_repet(n):
    if n > 52:  # 26 let minis 26 let majiskil
        print("Kantite a tro gran pou jenere kòd sa")
    
    cas = ''.join(random.sample(string.ascii_letters, n))
    print (cas)


genere_code_sans_repet(int(input('mete n : ')))











def separe_vig(mot):
    separ = '-'.join(mot)
    print (separ)
    
    
separe_vig(str(input('mete mo : ')))
 


def cripte_ind(mot):
    code = '-'.join(str(ord(c) - ord('A')) for c in mot.upper())
    print (code)
    
    
cripte_ind(str(input('mete mot : ')))


def pran_2_para(paramèt1, paramèt2):
    print (paramèt1, paramèt2)
    

pran_2_para(nom,prenom)



def non_an_kod_init(non):
    non_an = non.split('-')
    inisyal = ''.join(word[0].upper() for word in non_an)
    print (inisyal)
    
    
non_an_kod_init(str(input('mete non nh : ')))

