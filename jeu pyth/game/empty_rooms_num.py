from is_room_vide import * 
from play import * 
def get_nb_empty_room (plateau): 
    l = 0 
    n = plateau['n']
    num = 0 
    while l < n   :
        c = 0 
        while  c < n :
            if is_room_empty( plateau , l , c ) : 
                num += 1 
            c += 1
        l+= 1     
    return num 

