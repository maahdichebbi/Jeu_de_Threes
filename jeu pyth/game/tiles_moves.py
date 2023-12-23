from random import * 
from get_value  import *
from play import init_play
from is_game_over import check_game_over
def get_next_alea_tiles (p,mode): 
    a= 1 
    b= 1 
    d= 2 
    c= 1
    if mode == 'init' :
        while get_value(p,a,b) != 0 :
            a = randint(0,p['n']-1)
            b = randint(0,p['n']-1)
        while (get_value(p,c,d) != 0) and ((c != a ) or (d != b )): 
            c = randint(0,p['n']-1)
            d = randint(0,p['n']-1)
        return {'mode' : 'init', 
        '0': {'val': 2 , 'lig':a , 'col' : b },
        '1' :{'val': 1 , 'lig':c , 'col' : d },
        'check' : not check_game_over(p)}
    elif mode == 'encours' : 
        while get_value(p,a,b) != 0 :
            a = randint(0,p['n']-1)
            b = randint(0,p['n']-1) 
        return {'mode' : 'encours', 
        '0': {'val': randint(1,3) , 'lig':a , 'col' : b },
        'check' : not check_game_over(p)}
   
p = init_play()
print( get_next_alea_tiles(p,'init'))





        
