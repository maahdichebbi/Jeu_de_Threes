from play import*

def get_score(plateau):
    """retourne le score du plateau"""
    score=0
    i=0
    n=plateau['tiles']
    while i<len(n):
        score+=n[i]
        i+=1
    return score 
h=score=get_score(p)
print(h)


        
    