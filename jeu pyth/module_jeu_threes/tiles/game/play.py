
def init_play():
    plateau={'n':5,'nombre_cases_libres':6,'tiles':[6,2,3,2,0,2,6,2,0,2,2,0,1,0,0,0,1,2,3,4,5,6,7,8,9]}
    return plateau
    
#-------------------------------------------------------------------------------------------------------


"""retourne true si la partir est terminer, une partie est terminer ssi
le plateau(tiles) est remplie pas de zero dans la case"""

def check_game_over(plateau):
    rep = False
    gamover= get_nb_empty_room(plateau)
    if gamover == 0:
        rep=True
    return rep # rep est la reponse 

#-------------------------------------------------------------------------------------------------------

def get_score(plateau):
    """retourne le score du plateau"""
    score=0
    i=0
    n=plateau['tiles']
    while i<len(n):
        score+=n[i]
        i+=1
    return score 
def get_nb_empty_room (plateau): 

    """ Met a jour le dictionnaire  plateau avec le nombre de case libre  du plateau """

    l = 0  
    n = plateau['n'] 
    num = 0  
    while l < n   :
        c = 0  # 'c' est un compteur 
        while  c < n :
            if is_room_empty( plateau , l , c ) : 
                num += 1 
            c += 1
        l+= 1     
    return num # le nombre  de case libre 

#-------------------------------------------------------------------------------------------------------


    
