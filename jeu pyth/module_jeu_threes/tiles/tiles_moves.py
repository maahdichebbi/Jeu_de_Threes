
from random import * 
import sys
sys.path.append( r"C:\Users\Moi\Desktop\module_jeu_threes")
from ui.play_display import afficharge
from tiles.tiles_acces import * 


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
def check_game_over(plateau):
    rep = False
    gamover= get_nb_empty_room(plateau)
    if gamover == 0:
        rep=True
    return rep # rep est la reponse 


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

#----------------------------------------------------------------------------------------------------------------

def put_next_tiles(p,tiles):
    """permet de placer une ou deux tuiles dans le plateau
:paran p: plateau de jeu: paran tiles:dictionnaire
sous forme de celui renvoyé par la fonction get_next_alea_tiles"""
    if tiles["mode"] == 'encours' : 

        lig=tiles["0"]["lig"]
        col=tiles["0"]["col"]
        val=tiles["0"]["val"]
        set_value(p,lig,col,val)
        return p 
    
    elif tiles["mode"]=="init":
         lig1=tiles['0']['lig'] 
         col1=tiles["0"]["col"]
         val1=tiles["0"]["val"]

         lig2=tiles['1']['lig'] 
         col2=tiles["1"]["col"]
         val2=tiles["1"]["val"]
         set_value(p,lig1,col1,val1)
         set_value(p,lig2,col2,val2)

    return p
#-----------------------------------------------------------------------------------------------------------------




def line_pack(p,lig,debut,sens): 
    if sens  == 1 and (debut >0) : 
        val = get_value(p,lig,debut) 
        if val == get_value(p,lig,debut -1) : 
            valf = val + get_value(p,lig,debut-1 )
            set_value(p,lig,debut,0)
        elif is_room_empty(p,lig,debut-1) : 
            valf = val 
            set_value(p,lig,debut,0)
        else : 
            valf = get_value(p,lig,debut -1)  
        
        return set_value(p,lig,debut-1,valf) 
    elif sens == 0 and (debut < 3) : 
        val = get_value(p,lig,debut) 
        if val == get_value(p,lig,debut +1) : 
            valf = val + get_value(p,lig,debut+1) 
            set_value(p,lig,debut,0)
        elif is_room_empty(p,lig,debut +1) : 
            valf = val 
            set_value(p,lig,debut,0)
        else : 
            valf = get_value(p,lig,debut +1)     
        return set_value(p,lig,debut+1,valf) 

#-------------------------------------------------------------------------------------------------------
def column_pack(p,col,debut,sens): 
    if sens  == 1 and (debut >0) : 
        val = get_value(p,debut,col) 
        if val == get_value(p,debut -1,col) : 
            valf = val + get_value(p,debut-1,col )
            set_value(p,debut,col,0)
        elif is_room_empty(p,debut-1,col) : 
            valf = val 
            set_value(p,debut,col,0)
        else : 
            valf = get_value(p,debut-1,col)  
        
        return set_value(p,debut-1,col,valf) 
    elif sens == 0 and (debut < 3) : 
        val = get_value(p,debut,col) 
        if val == get_value(p,debut +1,col) : 
            valf = val + get_value(p,debut+1,col) 
            set_value(p,debut,col,0)
        elif is_room_empty(p,debut +1,col) : 
            valf = val 
            set_value(p,debut,col,0)
        else : 
            valf = get_value(p,debut +1,col)     
        return set_value(p,debut+1,col,valf) 

#-----------------------------------------------------------------------------------------------------------

def line_move(p,lig,sens):
    if sens == 1 : 
        i=0
        while i <= p['n']-1 : 
            line_pack(p,lig,i,sens)
            i+=1 
    else : 
        i= p['n']-1
        while i > -1 : 
            line_pack(p,lig,i,sens)
            i-=1 
#-------------------------------------------------------------------------------------------------------
def line_move(p,lig,sens):
    if sens == 1 : 
        i=0
        while i <= p['n']-1 : 
            line_pack(p,lig,i,sens)
            i+=1 
    else : 
        i= p['n']-1
        while i > -1 : 
            line_pack(p,lig,i,sens)
            i-=1 
#------------------------------------------------------------------------------------------------------
def column_move(p,col,sens):
    if sens == 1 : 
        i=0
        while i <= p['n']-1 : 
            column_pack(p,col,i,sens)
            i+=1 
    else : 
        i= p['n']-1
        while i > -1 : 
            column_pack(p,col,i,sens)
            i-=1 

#-------------------------------------------------------------------------------------------------------------
def lines_move(p,sens): 
    i=0
    while i < p['n']:
        line_move(p,i,sens)
        i+=1

#-------------------------------------------------------------------------------------------------------------

def columns_move(p,sens): 
    i=0
    while i < p['n']:
        column_move(p,i,sens)
        i+=1

#------------------------------------------------------------------------------------------------

def play_move(p,sens): 
    if sens == 'b' : 
        columns_move(p,0)
    elif sens == 'h':
         columns_move(p,1)
    elif sens == 'd':
        lines_move(p,0)
    elif sens == 'g':
        lines_move(p,1)
    else : print('erreur choix ')






            

        




       

