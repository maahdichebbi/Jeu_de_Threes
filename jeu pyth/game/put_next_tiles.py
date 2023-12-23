from tiles_moves import get_next_alea_tiles  
from set_value import*
from play import init_play
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

p = init_play()
print(p)
put_next_tiles(p,get_next_alea_tiles(p,'encours'))
print(p)


         
        
        
    
    