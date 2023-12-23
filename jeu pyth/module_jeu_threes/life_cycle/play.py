import sys
sys.path.append( r"C:\Users\Moi\Desktop\module_jeu_threes")
from ui.play_display import afficharge
from ui.user_entries import get_user_move
from tiles.tiles_moves import play_move , put_next_tiles,get_next_alea_tiles ,get_nb_empty_room
from tiles.game.play import get_score , check_game_over 
from game.play import create_new_play
import json

def cycle_play( partie  ) :
    while  partie != None:
        afficharge(partie['plateau']) 
        print(partie['next tile']) 
        choix = get_user_move()
        if choix == 'm' : 
            return False  
        else : 
            play_move(partie['plateau'],choix) 
            partie['score']= get_score(partie['plateau']) 
            partie['next tile '] = put_next_tiles(partie['plateau'],get_next_alea_tiles(partie['plateau'],'encours'))
            partie['plateau']['nombre_cases_libres']= get_nb_empty_room(partie['plateau'])
            
        if check_game_over(partie['plateau']) : 
            return True   


def save_game(partie):
    data= json.dumps(partie)
    with open('saved_game.json' , 'w') as f  : 
        f.write(data)  
        f.close(data) 
    
    

def restore_game() : 
    partie = json.load(open ('saved_game.json' )) 
    return partie 

