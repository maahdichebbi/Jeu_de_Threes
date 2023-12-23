from get_value import * 
from play import * 

def is_room_empty( plateau , i , j ):
    indice =i * plateau['n']  
    val = plateau['tiles'][indice + j] 
    if val == 0 :
        return True 
    else : 
        return False 
    
p = init_play() 

print(is_room_empty(p,0,2))

