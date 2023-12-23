from game.play import init_play 


def aff_tab(t):
    """ cette fn permet du mettre le contenu d'un tableau dns une chaine de caractére """
    i = 0
    ch=''
    while i < len(t) : 
        ch += str(t[i]) + ' | ' 
        i += 1 
    return ch 



def afficharge(plat):
    n= plat['n']
    i=0
    l=''
    while i < n  :
        l += '----' 
        i+=1
    i = 0 
    tail = n 
    j=0
    while i< n *n : 
        lig =  []
        print(l)
        
        while j < tail :
            lig.append(p['tiles'][j]) 
            j+=1
        print(aff_tab(lig))
        tail += n 
        i+= n  
