import sys
sys.path.append( r"C:\Users\Moi\Desktop\module_jeu_threes\tiles")
from tiles_moves import  put_next_tiles , get_next_alea_tiles, get_nb_empty_room



def create_new_play() : 
    p = {'n':4,'nombre_cases_libres':16,'tiles':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]} 
    partie = {'plateau' : p , 'next tile' :  put_next_tiles(p,get_next_alea_tiles(p,'init')) , 'score': 0} 
    return partie




