

# pou afficher liste div2 de n

def list_div():
    # n = int(input('mete nomb lan : '))
    n = 10
    liste_divisible_par_2 = [i for i in range(n + 1) if i % 2 == 0]
    print (liste_divisible_par_2)
    
list_div()