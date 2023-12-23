from game.play import init_play 
p= init_play()

def aff_tab(t):
    i = 0
    ch=''
    while i < len(t) : 
        ch += str(t[i]) +' ' 
        i += 1 
    return ch 



def affich(p):
    n= p['n']
    i=0
    taille = n 
    j=0
    while i< n *n : 
        lig =  []
        while j < taille :
            lig.append(p['tiles'][j]) 
            j+=1
        print(aff_tab(lig))
        taille += n 
        i+= n  
affich(p)
