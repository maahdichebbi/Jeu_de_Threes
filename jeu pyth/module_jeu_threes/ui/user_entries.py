import sys

from afficharge import afficharge
from game.empty_rooms_num import get_nb_empty_room
from game.get_score import get_score
from game.is_game_over import check_game_over
from game.put_next_tiles import put_next_tiles
from game.tiles_moves import get_next_alea_tiles
from module_jeu_threes.life_cycle.play import restore_game, save_game
from module_jeu_threes.tiles.tiles_moves import play_move

sys.path.append( r"C:\Users\Moi\Desktop\module_jeu_threes\tiles")
from tiles_moves import * 
from game.play import *

def cycle_play( partie  ) :
    while  partie != None:
        afficharge(partie['plateau']) 
        print(partie['next tile']) 
        choix = get_user_move()
        if choix == 'm' : 
            get_user_menu(partie) 
        else : 
            play_move(partie['plateau'],choix) 
            partie['score']= get_score(partie['plateau']) 
            partie['next tile '] = put_next_tiles(partie['plateau'],get_next_alea_tiles(partie['plateau'],'encours'))
            partie['plateau']['nombre_cases_libres']= get_nb_empty_room(partie['plateau'])
            
        if check_game_over(partie['plateau']) : 
            return True   

def create_new_play() : 
    p = {'n':4,'nombre_cases_libres':16,'tiles':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]} 
    partie = {'plateau' : p , 'next tile' :  put_next_tiles(p,get_next_alea_tiles(p,'init')) , 'score': 0} 
    return partie


def get_user_move():
    saise = ' '
    while ( saise != 'h') and ( saise != 'b') and ( saise != 'd') and ( saise != 'g') and ( saise != 'm') :
        saise =  input(' "h" pour haut , "b" pour bas , "d" pour droite , g pour gauche , m pour menu ').lower()
    return saise

def get_user_menu (partie) : 
    choix = ''
    while ( choix != 'N') and ( choix != 'L') and ( choix != 'S') and ( choix != 'C') and ( choix != 'C')  and (choix!= 'Q'):
        choix = input('quel action souhaites vous effectuer "N" pour nouveau partie | "L" pour charger une partie   | "S" pour sauvegareder | "C" pour reprendre | "Q" pour quitter  ').upper()
    if choix == 'N' : 
        partie= create_new_play()          
        cycle_play(partie)
    elif choix == 'L' : 
        restore_game()    
    elif (choix == 'S' ) : 
        save_game(partie)
        if partie == None : 
            print('vous etes pas dns une partie merci de commencer une nouvelle partie ou charger une  ')  

    elif  choix == 'C' : 
        cycle_play(partie) 
    else:
        print('a bientot')
        return True

