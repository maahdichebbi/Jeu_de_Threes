from empty_rooms_num import * 
"""retourne true si la partir est terminer, une partie est terminer ssi
le plateau(tiles) est remplie pas de zero dans la case"""
def check_game_over(plateau):
    rep=False
    gamover= get_nb_empty_room(plateau)
    if gamover==0:
        rep=True
    return rep
