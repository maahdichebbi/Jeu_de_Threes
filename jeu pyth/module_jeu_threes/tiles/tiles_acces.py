

def check_indice(plateau,indice):
    """ retourne True si indice correspond a un indice valide de case pour le plateau(entre 0 et n-1"""
    mot=True
    if indice>plateau['n'] or indice<0:
        mot=False
        assert mot<0,"ValueError"
    return mot  



def check_room(plateau,lig,col):
    """retourne True si (lig,col) est une case du plateau(lig et col sont des indice valides"""
    verrif=True
    if lig >plateau['n'] or lig<0:
        if col>plateau['n']  or col<0:
            verrif=False

        verrif=False
        assert verrif==(-1,3),'ValueError'
    return verrif

#-------------------------------------------------------------------------------------------------------

def get_value(plateau,lig,col):

    """retourne la valeur de la case (lig,col) genere une erreur si (lig,col) n'est pas valide"""

    if not(check_room(plateau,lig,col)):
        assert not True,"(lig,col) n'est pas carrect"
    valeur=lig*plateau['n']
    return plateau['tiles'][valeur + col]

#-------------------------------------------------------------------------------------------------------

def set_value(plateau , lig , col , val ) :

    """ Affecte la valeur val dans la case (lig,col) du plateau"""  

    if  check_room(plateau,lig,col) == False :
        return  " col / ligne invalide"
    
    indice =lig*plateau['n']  
    plateau['tiles'][indice + col] = val 

#-------------------------------------------------------------------------------------------------------

def is_room_empty( plateau , i , j ):

    """ Teste si une case du plateau est libre ou pas return True si la case est libre , False sinon """

    indice = i * plateau['n']  
    val = plateau['tiles'][indice + j] 
    if val == 0 :
        return True 
    else : 
        return False 

#-------------------------------------------------------------------------------------------------------


    