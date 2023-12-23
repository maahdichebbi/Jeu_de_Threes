from play import*
from check_rom import*
"""retourne la valeur de la case (lig,col) genere une erreur si (lig,col) n'est pas valide"""
def get_value(plateau,lig,col):
    if not(check_room(plateau,lig,col)):
        assert not True,"(lig,col) n'est pas carrect"
    valeur=lig*plateau['n']
    return plateau['tiles'][valeur + col]
        
    
  

    