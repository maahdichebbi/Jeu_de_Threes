from play import * 
from check_rom import * 
def set_value(plateau , lig , col , val ) : 
    if  check_room(plateau,lig,col) == False :
        return  " col / ligne invalide"
    
    indice =lig*plateau['n']  
    plateau['tiles'][indice + col] = val 

p = init_play() 
print(set_value(p,0,0,8))
print(p)
